from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

# ชุดเอกสารที่กำหนด
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


# คำค้นหา
query = "I was sitting in the forest looking at tiger and bird"

# สร้าง TF*IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# แสดงค่าของ TF*IDF
tfidf_matrix_array = tfidf_matrix.toarray()
terms = vectorizer.get_feature_names_out()
print("คำที่ปรากฏในเอกสาร:", terms)
print("\nเมทริกซ์ TF*IDF:\n", tfidf_matrix_array)


# Step 2: สร้างเมทริกซ์ TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
print("เมทริกซ์ TF-IDF (Term-Document Matrix):")
print(X.toarray())
print("คำศัพท์ (Vocabulary):", vectorizer.get_feature_names_out())

# Step 3: ลดมิติด้วย SVD
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X)
print("\nเมทริกซ์ TF-IDF หลังจากลดมิติด้วย SVD:")
print(X_reduced)

# Step 4: แปลงคำค้นหาเป็นเวกเตอร์ TF-IDF
query_vec = vectorizer.transform([query])
print("\nเวกเตอร์ TF-IDF ของคำค้นหา:")
print(query_vec.toarray())

# Step 5: ย้ายคำค้นหาเข้าสู่ Concept Space
query_reduced = svd.transform(query_vec)
print("\nเวกเตอร์ของคำค้นหาใน Concept Space:")
print(query_reduced)

# Step 6: คำนวณความคล้ายคลึงระหว่าง Query กับเอกสาร
similarity = cosine_similarity(query_reduced, X_reduced)
similarity_scores = similarity[0]
print("\nค่าความคล้ายคลึงระหว่าง Query กับเอกสารแต่ละฉบับ:")
for idx, score in enumerate(similarity_scores):
    print(f"Document {idx+1}: Similarity Score = {score:.4f}")

# Step 7: จัดอันดับเอกสารตามความคล้ายคลึง
sorted_indices = similarity_scores.argsort()[::-1]
print("\nอันดับเอกสารตามความเกี่ยวข้องกับ Query:")
for rank, idx in enumerate(sorted_indices, start=1):
    print(f"อันดับ {rank}: Document {idx+1} (Similarity Score = {similarity_scores[idx]:.4f})")
