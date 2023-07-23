import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
@chache_data

def preprocess_data(data):
    # Gather All Items of Each Transactions into Numpy Array
    transaction = []
    for i in range(0, data.shape[0]):
        for j in range(0, data.shape[1]):
            transaction.append(data.values[i, j])
    # Convert to numpy array
    transaction = np.array(transaction)
    # Transform them into a Pandas DataFrame
    df = pd.DataFrame(transaction, columns=["items"])
    # Put 1 to each item for making a countable table
    df["incident_count"] = 1
    # Delete NaN items from the dataset
    indexNames = df[df['items'] == "nan"].index
    df.drop(indexNames, inplace=True)
    # Make a new appropriate Pandas DataFrame for visualizations
    df_table = df.groupby("items").sum().sort_values("incident_count", ascending=False).reset_index()

    return df_table

def main():
    st.title("Apriori Frequent Itemset Mining Web App")

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV data
        dataset = pd.read_csv(uploaded_file)

        # Display the columns and few rows using head
        st.subheader("Columns and Few Rows of the Dataset")
        st.dataframe(dataset.head())

        # Data preprocessing
        df_table = preprocess_data(dataset)

        # Display the top 5 items
        st.subheader("Top 5 Items")
        st.dataframe(df_table.head(5).style.background_gradient(cmap='Blues'))

        # Create and display a Treemap using Plotly
        st.subheader("Top 50 Items Treemap")
        df_table["all"] = "Top 50 items"
        fig = px.treemap(df_table.head(50), path=['all', "items"], values='incident_count',
                         color=df_table["incident_count"].head(50), hover_data=['items'],
                         color_continuous_scale='Blues')
        st.plotly_chart(fig)

        # Extract top 30 items and perform FP-Growth
        first30 = df_table["items"].head(30).values
        transaction = []
        for i in range(dataset.shape[0]):
            transaction.append([str(dataset.values[i, j]) for j in range(dataset.shape[1])])
        transaction = np.array(transaction)
        te = TransactionEncoder()
        te_ary = te.fit(transaction).transform(transaction)
        dataset_encoded = pd.DataFrame(te_ary, columns=te.columns_)
        dataset_encoded = dataset_encoded.loc[:, first30]

        # Perform FP-Growth
        st.subheader("FP-Growth Algorithm")
        min_support = st.slider("Minimum Support", min_value=0.05, max_value=0.5, step=0.01, value=0.1)
        frequent_itemsets = fpgrowth(dataset_encoded, min_support=min_support, use_colnames=True)

        # Display the top frequent itemsets
        st.subheader("Top Frequent Itemsets")
        st.dataframe(frequent_itemsets.head(10))

        # Association Rules
        st.subheader("Association Rules")
        min_confidence = st.slider("Minimum Confidence", min_value=0.1, max_value=1.0, step=0.1, value=0.5)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

        # Sort association rules based on confidence
        sorted_rules = rules.sort_values("confidence", ascending=False)

        # Display the top association rules based on confidence
        st.subheader("Top Association Rules based on Confidence")
        st.dataframe(sorted_rules)

if __name__ == "__main__":
    main()
