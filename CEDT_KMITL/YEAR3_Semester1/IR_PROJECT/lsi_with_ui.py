import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.linalg import svd

# Set numpy options for better readability
np.set_printoptions(precision=3, suppress=True)

# LSI Model class definition
class DetailedLSIModel:
    def __init__(self, n_components=3):
        self.n_components = n_components
        self.count_vectorizer = CountVectorizer(stop_words=None)
        self.tfidf_vectorizer = TfidfVectorizer(stop_words=None)
     
    def step1_create_tdm(self, documents):
        tdm = self.count_vectorizer.fit_transform(documents)
        terms = self.count_vectorizer.get_feature_names_out()
        tdm_df = pd.DataFrame(tdm.toarray(), columns=terms, index=[f'Document {i+1}' for i in range(len(documents))])
        return tdm_df, terms

    def step2_tfidf_transform(self, documents):
        tfidf_matrix = self.tfidf_vectorizer.fit_transform(documents)
        terms = self.tfidf_vectorizer.get_feature_names_out()
        tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=terms, index=[f'Document {i+1}' for i in range(len(documents))])
        return tfidf_df, tfidf_matrix.toarray(), terms
     
    def step3_svd_decomposition(self, tfidf_matrix):
        U, S, VT = svd(tfidf_matrix, full_matrices=False)
        return U[:, :self.n_components], S[:self.n_components], VT[:self.n_components, :]

    def step4_process_query(self, query):
        query_vec = self.tfidf_vectorizer.transform([query]).toarray()
        return query_vec
     
    def step5_calculate_similarity(self, query_vec, doc_matrix):
        doc_norms = np.linalg.norm(doc_matrix, axis=1)
        query_norm = np.linalg.norm(query_vec)
        return np.dot(doc_matrix, query_vec.T).flatten() / (doc_norms * query_norm)

    def step6_rank_documents(self, similarities, documents):
        results = [{'Document_ID': f'Document {i+1}', 'Content': doc, 'Similarity': sim} for i, (doc, sim) in enumerate(zip(documents, similarities))]
        return pd.DataFrame(results).sort_values('Similarity', ascending=False)

# Initialize model and documents
documents = [
    "bird cat cat dog dog bird tiger tiger",  # D1
    "cat tiger cat dog",                      # D2
    "dog bird bird cat",                      # D3
    "cat tiger cat dog",                      # D4
    "tiger tiger dog tiger",                  # D5
    "cat cat tiger tiger",                    # D6
    "bird cat bird",                          # D7
    "dog cat bird",                           # D8 
    "cat dog tiger",                          # D9
    "tiger tiger tiger",                      # D10
    "tiger tiger tiger dog cat cat cat",      # D11
    "bird cat tiger dog dog dog",             # D12
    "tiger tiger dog dog",                    # D13
    "cat cat cat",                            # D14
    "bird bird bird bird dog"                 # D15
]
query = "cat cat cat"
lsi_model = DetailedLSIModel(n_components=3)

# Streamlit UI Components
st.title("LSI Model Document Ranking")
st.subheader("1. Term-Document Matrix")
tdm_df, terms = lsi_model.step1_create_tdm(documents)
st.dataframe(tdm_df)

st.subheader("2. TF-IDF Matrix")
tfidf_df, tfidf_matrix, terms = lsi_model.step2_tfidf_transform(documents)
st.dataframe(tfidf_df)

st.subheader("3. SVD Decomposition")
U, S, VT = lsi_model.step3_svd_decomposition(tfidf_matrix)
topic_df = pd.DataFrame(VT, columns=terms, index=[f'Topic {i+1}' for i in range(lsi_model.n_components)])
st.dataframe(topic_df)

st.subheader("4. Query Processing")
query_vec = lsi_model.step4_process_query(query)
query_df = pd.DataFrame(query_vec, columns=terms, index=['Query'])
st.dataframe(query_df)

st.subheader("5. Document Similarity Calculation")
doc_lsi = np.dot(tfidf_matrix, VT.T @ np.diag(1/S))
query_lsi = np.dot(query_vec, VT.T @ np.diag(1/S))
similarities = lsi_model.step5_calculate_similarity(query_lsi, doc_lsi)
similarity_df = pd.DataFrame({"Document": [f'Document {i+1}' for i in range(len(documents))], "Similarity": similarities})
st.dataframe(similarity_df)

st.subheader("6. Ranked Documents")
rankings = lsi_model.step6_rank_documents(similarities, documents)
st.dataframe(rankings)

st.subheader("Detailed Analysis of Top 5 Documents")
for idx, row in rankings.head().iterrows():
    st.write(f"**{row['Document_ID']}** (Similarity: {row['Similarity']:.4f})")
    st.write(f"Content: {row['Content']}")
    tiger_count = row['Content'].count('tiger')
    bird_count = row['Content'].count('bird')
    st.write(f"Tiger count: {tiger_count}, Bird count: {bird_count}")
    st.write("\n")

