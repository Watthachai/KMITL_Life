import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Define the documents
documents = [
    "bird cat cat dog dog bird tiger tiger",  # Document 1
    "cat tiger cat dog",  # Document 2
    "dog bird bird cat",  # Document 3
    "cat tiger cat dog",  # Document 4
    "tiger tiger dog tiger",  # Document 5
    "cat cat tiger tiger",  # Document 6
    "bird cat bird",  # Document 7
    "dog cat bird",  # Document 8
    "cat dog tiger",  # Document 9
    "tiger tiger tiger",  # Document 10
    "dog cat cat dog tiger",  # Document 11
    "tiger tiger bird cat dog dog",  # Document 12
    "dog dog cat dog tiger cat",  # Document 13
    "cat bird dog bird cat",  # Document 14
    "tiger tiger dog cat cat tiger"  # Document 15
]

# Streamlit app title
st.title("Document Similarity Analysis with TF, DF, IDF, TF-IDF, SVD, and Cosine Similarity")

# Step 1: Display Document-Term Matrix with raw term counts
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
df_term_matrix = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out(), index=[f"D{i+1}" for i in range(len(documents))])
st.markdown("<h2>Step 1: Term Frequency (TF) Matrix</h2>", unsafe_allow_html=True)
st.dataframe(df_term_matrix.style.set_properties(**{'text-align': 'center'}))

# Step 2: Calculate Document Frequencies (DF)
doc_counts = (df_term_matrix > 0).sum(axis=0)
st.markdown("<h2>Step 2: Document Frequency (DF) per Term</h2>", unsafe_allow_html=True)
st.write(doc_counts)

# Step 3: Calculate Inverse Document Frequency (IDF)
total_docs = len(documents)
idf_values = np.log10(total_docs / doc_counts)
idf_df = pd.DataFrame(idf_values, columns=["IDF"]).T
st.markdown("<h2>Step 3: Inverse Document Frequency (IDF) Values</h2>", unsafe_allow_html=True)
st.dataframe(idf_df.style.set_properties(**{'text-align': 'center'}))

# Step 4: Apply TF-IDF to the matrix
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(documents)
df_tfidf_matrix = pd.DataFrame(X_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out(), index=[f"D{i+1}" for i in range(len(documents))])
st.markdown("<h2>Step 4: TF-IDF Matrix</h2>", unsafe_allow_html=True)
st.dataframe(df_tfidf_matrix.style.set_properties(**{'text-align': 'center'}))

# Step 5: Singular Value Decomposition (SVD)
svd = TruncatedSVD(n_components=2)  # Adjust the number of components if needed
X_svd = svd.fit_transform(X_tfidf)
df_svd_matrix = pd.DataFrame(X_svd, columns=["Component 1", "Component 2"], index=[f"D{i+1}" for i in range(len(documents))])
st.markdown("<h2>Step 5: SVD Projection (Top 2 Components)</h2>", unsafe_allow_html=True)
st.dataframe(df_svd_matrix.style.set_properties(**{'text-align': 'center'}))

# Step 6: Convert Query to Vector, apply TF-IDF and SVD
query = st.text_input("Enter a query to compare with the documents:")
if query:
    query_vector_tfidf = tfidf_vectorizer.transform([query])
    query_vector_svd = svd.transform(query_vector_tfidf)

    # Step 7: Calculate similarity of the query to each document using cosine similarity
    similarity_scores = cosine_similarity(query_vector_svd, X_svd)[0]
    df_similarity = pd.DataFrame(similarity_scores, columns=["Similarity Score"], index=[f"D{i+1}" for i in range(len(documents))])
    df_similarity = df_similarity.sort_values(by="Similarity Score", ascending=False)
    
    st.markdown("<h2>Step 7: Similarity Scores</h2>", unsafe_allow_html=True)
    st.dataframe(df_similarity.style.set_properties(**{'text-align': 'center'}))

    # Plotting the ranked similarity scores
    st.markdown("<h2>Ranked Similarity Scores</h2>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    plt.bar(df_similarity.index, df_similarity["Similarity Score"], color="skyblue")
    plt.xlabel("Document")
    plt.ylabel("Similarity Score")
    plt.title("Query Similarity to Each Document")
    st.pyplot(plt)
