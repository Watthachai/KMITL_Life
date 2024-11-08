import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.linalg import svd
import pandas as pd
np.set_printoptions(precision=3, suppress=True)

class DetailedLSIModel:
    def __init__(self, n_components=3):
        self.n_components = n_components
        self.count_vectorizer = CountVectorizer(stop_words=None)
        self.tfidf_vectorizer = TfidfVectorizer(stop_words=None)
    
    def calculate_cosine_similarity(self, vec1, vec2):
        """
        คำนวณ Cosine Similarity ระหว่างสองเวกเตอร์
        
        cosine_similarity = dot_product(vec1, vec2) / (norm(vec1) * norm(vec2))
        """
        # คำนวณ dot product
        dot_product = np.dot(vec1, vec2)
        
        # คำนวณ norm (magnitude) ของแต่ละเวกเตอร์
        norm_vec1 = np.sqrt(np.sum(vec1**2))
        norm_vec2 = np.sqrt(np.sum(vec2**2))
        
        # คำนวณ cosine similarity
        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0
        
        similarity = dot_product / (norm_vec1 * norm_vec2)
        return similarity
    
    def process_documents(self, documents, query):
        """ประมวลผลเอกสารและคำค้นหาทั้งหมด แสดงรายละเอียดทุกขั้นตอน"""
        
        print("\n1. สร้างเมทริกซ์ TF-IDF")
        print("="*80)
        # แปลงเอกสารเป็นเมทริกซ์ TF-IDF
        tfidf_matrix = self.tfidf_vectorizer.fit_transform(documents)
        terms = self.tfidf_vectorizer.get_feature_names_out()
        
        # แสดงเมทริกซ์ TF-IDF
        tfidf_df = pd.DataFrame(
            tfidf_matrix.toarray(),
            columns=terms,
            index=[f'D{i+1}' for i in range(len(documents))]
        )
        print("\nTF-IDF Matrix:")
        print(tfidf_df)
        
        print("\n2. SVD Decomposition")
        print("="*80)
        # ทำ SVD
        U, S, VT = svd(tfidf_matrix.toarray(), full_matrices=False)
        
        # ลดมิติ
        U_reduced = U[:, :self.n_components]
        S_reduced = S[:self.n_components]
        VT_reduced = VT[:self.n_components, :]
        
        print("\nSingular Values:")
        print(S_reduced)
        
        print("\n3. แปลงเอกสารและ Query เข้าสู่ LSI Space")
        print("="*80)
        # แปลง query
        query_vec = self.tfidf_vectorizer.transform([query]).toarray()
        
        # Project เข้าสู่ LSI space
        doc_lsi = np.dot(tfidf_matrix.toarray(), VT_reduced.T @ np.diag(1/S_reduced))
        query_lsi = np.dot(query_vec, VT_reduced.T @ np.diag(1/S_reduced))
        
        print("\nDocument vectors in LSI space:")
        lsi_df = pd.DataFrame(
            doc_lsi,
            columns=[f'Dimension {i+1}' for i in range(self.n_components)],
            index=[f'D{i+1}' for i in range(len(documents))]
        )
        print(lsi_df)
        
        print("\nQuery vector in LSI space:")
        query_lsi_df = pd.DataFrame(
            query_lsi,
            columns=[f'Dimension {i+1}' for i in range(self.n_components)],
            index=['Query']
        )
        print(query_lsi_df)
        
        print("\n4. คำนวณ Cosine Similarity")
        print("="*80)
        similarities = []
        detailed_calcs = []
        
        for i, doc_vec in enumerate(doc_lsi):
            # คำนวณ dot product
            dot_product = np.dot(doc_vec, query_lsi[0])
            
            # คำนวณ norms
            doc_norm = np.sqrt(np.sum(doc_vec**2))
            query_norm = np.sqrt(np.sum(query_lsi[0]**2))
            
            # คำนวณ similarity
            similarity = self.calculate_cosine_similarity(doc_vec, query_lsi[0])
            similarities.append(similarity)
            
            # เก็บรายละเอียดการคำนวณ
            calc_details = {
                'Document': f'D{i+1}',
                'Doc Vector': doc_vec,
                'Dot Product': dot_product,
                'Doc Norm': doc_norm,
                'Query Norm': query_norm,
                'Similarity': similarity
            }
            detailed_calcs.append(calc_details)
        
        # แสดงรายละเอียดการคำนวณ
        print("\nDetailed Cosine Similarity Calculations:")
        for calc in detailed_calcs:
            print(f"\nDocument: {calc['Document']}")
            print(f"Document Vector: {calc['Doc Vector']}")
            print(f"Dot Product with Query: {calc['Dot Product']:.4f}")
            print(f"Document Norm: {calc['Doc Norm']:.4f}")
            print(f"Query Norm: {calc['Query Norm']:.4f}")
            print(f"Cosine Similarity = {calc['Dot Product']:.4f} / ({calc['Doc Norm']:.4f} * {calc['Query Norm']:.4f})")
            print(f"                  = {calc['Similarity']:.4f}")
        
        print("\n5. จัดอันดับเอกสาร")
        print("="*80)
        rankings = []
        for i, sim in enumerate(similarities):
            rankings.append({
                'Document_ID': f'D{i+1}',
                'Content': documents[i],
                'Similarity': sim
            })
        
        rankings_df = pd.DataFrame(rankings).sort_values('Similarity', ascending=False)
        print("\nDocument Rankings:")
        print(rankings_df)
        
        return rankings_df, detailed_calcs

# ข้อมูลตัวอย่าง
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

query = "I was sitting in the forest looking at tiger and bird"

# สร้างโมเดลและประมวลผล
lsi_model = DetailedLSIModel(n_components=3)
rankings, detailed_calcs = lsi_model.process_documents(documents, query)

# แสดงผลลัพธ์สุดท้าย
print("\nสรุปผลการค้นหา")
print("="*80)
print("\nTop 5 Most Relevant Documents:")
for idx, row in rankings.head().iterrows():
    print(f"\nDocument {row['Document_ID']} (Similarity: {row['Similarity']:.4f}):")
    print(f"Content: {row['Content']}")
    # นับจำนวนคำสำคัญ
    tiger_count = row['Content'].count('tiger')
    bird_count = row['Content'].count('bird')
    print(f"Tiger count: {tiger_count}")
    print(f"Bird count: {bird_count}")