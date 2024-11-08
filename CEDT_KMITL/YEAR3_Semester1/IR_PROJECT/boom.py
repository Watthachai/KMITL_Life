import matplotlib.pyplot as plt
from gensim import corpora, models, similarities

# Define the new documents
documents = [
    "bird cat cat dog dog bird tiger tiger",  # D1
    "cat tiger cat dog",  # D2
    "dog bird bird cat",  # D3
    "cat tiger cat dog",  # D4
    "tiger tiger dog tiger",  # D5
    "cat cat tiger tiger",  # D6
    "bird cat bird",  # D7
    "dog cat bird",  # D8 
    "cat dog tiger",  # D9
    "tiger tiger tiger",  # D10
    "tiger tiger tiger dog cat cat cat",  # D11
    "bird cat tiger dog dog dog",  # D12
    "tiger tiger dog dog",  # D13
    "cat cat cat ",  # D14
    "bird bird bird bird dog"  # D15
]

# Preprocess documents
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

# Remove words that appear only once
all_tokens = []
for text in texts:
    all_tokens.extend(text)
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

# Create a dictionary and corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Create TF-IDF and LSI models
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus_tfidf]

# Define the query and preprocess it
query_text = input("Please type your search term. : ")
query_words = [word for word in query_text.lower().split() if word not in stoplist]
query_bow = dictionary.doc2bow(query_words)
query_lsi = lsi[tfidf[query_bow]]

# Calculate the similarity of the query to each document
index = similarities.MatrixSimilarity(lsi[corpus_tfidf])
sims = index[query_lsi]

# Sort documents by similarity score in descending order
sorted_sims = sorted(enumerate(sims), key=lambda item: -item[1])

# Display similarity results in descending order
print("\nDocuments ranked by similarity to the query:")
for doc_number, sim_score in sorted_sims:
    print(f"Document {doc_number + 1} (D{doc_number + 1}): Similarity = {sim_score:.4f}")

# Prepare data for plotting
doc_labels = [f"D{doc_number + 1}" for doc_number, _ in sorted_sims]
similarity_scores = [sim_score for _, sim_score in sorted_sims]

# Plotting the ranked similarity scores
plt.figure(figsize=(10, 6))
plt.barh(doc_labels, similarity_scores, color="skyblue")
plt.xlabel("Similarity Score")
plt.ylabel("Documents")
plt.title("Documents ranked by similarity to the query")
plt.gca().invert_yaxis()  # Invert y-axis for descending order
plt.show()