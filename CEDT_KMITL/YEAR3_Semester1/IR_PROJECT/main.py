# ติดตั้งไลบรารีที่จำเป็น
# !pip install numpy scipy scikit-learn

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline

# 1. เตรียมชุดเอกสาร (Corpus)
documents = [
    "The car is driven on the road.",
    "The truck is driven on the highway.",
    "The train runs on the rails.",
    "Cars and trucks are types of vehicles.",
    "Trains are a mode of transportation.",
]

# 2. สร้าง Term-Document Matrix (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# 3. ใช้ Singular Value Decomposition (SVD) ในการลดมิติ
# กำหนดจำนวนมิติหรือแนวคิด (n_components) ที่เราต้องการเก็บ
n_components = 2  # ปกติจะมากกว่านี้ แต่เพื่อความง่ายในการทดลองใช้ 2
svd = TruncatedSVD(n_components)
normalizer = Normalizer(copy=False)
lsa = make_pipeline(svd, normalizer)

# ใช้ LSA model กับชุดข้อมูล
X_lsa = lsa.fit_transform(X)

# 4. แสดงผลค่าน้ำหนักหรือแนวคิดที่ถูกลดมิติแล้ว
print("Latent Semantic Analysis (LSA) Components:")
print(svd.components_)

# แสดงเอกสารที่ถูกลดมิติใน Concept Space
print("\nDocuments in reduced LSA space:")
print(X_lsa)

# 5. ทดลองค้นหาคำใน LSI Model
query = ["car"]  # คำค้นหา
query_vector = vectorizer.transform(query)
query_lsa = lsa.transform(query_vector)

# คำนวณความคล้ายคลึงระหว่างคำค้นหากับเอกสาร (Cosine Similarity)
similarities = np.dot(X_lsa, query_lsa.T).flatten()
print("\nSimilarity scores:")
print(similarities)

# 6. จัดอันดับเอกสารที่เกี่ยวข้องกับคำค้น
top_document_indices = similarities.argsort()[::-1]
print("\nDocuments ranked by relevance to the query:")
for index in top_document_indices:
    print(f"Document {index+1}: {documents[index]} (Score: {similarities[index]:.4f})")
