from gensim import corpora, models, similarities
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import nltk
import matplotlib.pyplot as plt

# Download the necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

print("@@@@@@@@@@@@@@@@@@@@@@ START DOC SECTION!! @@@@@@@@@@@@@@@@@@@@@@@")
"""documents = [
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
    "cat cat cat",  # D14
    "bird bird bird bird dog"  # D15
]"""

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

# Tokenization and preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
translator = str.maketrans('', '', string.punctuation)

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

# Preprocess documents
preprocessed_documents = [preprocess_text(doc) for doc in documents]


print("@@@@@@@@@@@@@@@@@@@@@@ END DOC SECTION!! @@@@@@@@@@@@@@@@@@@@@@@")

print("@@@@@@@@@@@@@@@@@@@@@# Preprocess documents@@@@@@@@@@@@@@@@@@@@@@@")
print(preprocessed_documents)
print("@@@@@@@@@@@@@@@@@@@@@# Preprocess documents@@@@@@@@@@@@@@@@@@@@@@@@")

dictionary = corpora.Dictionary(preprocessed_documents)
print("@@@@@@@@@@@@@@@@@@@@@@@@dictionary@@@@@@@@@@@@@@@@@@@@@")
print(dictionary)
print("@@@@@@@@@@@@@@@@@@@@@@dictionary@@@@@@@@@@@@@@@@@@@@@@@")

corpus = [dictionary.doc2bow(doc) for doc in preprocessed_documents]

# Train the LSI model
lsi_model = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
print("@@@@@@@@@@@@@@@@@@# Train the LSI model@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(lsi_model[corpus])
print("@@@@@@@@@@@@@@@@@@# Train the LSI model@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# Create index
index = similarities.MatrixSimilarity(lsi_model[corpus])
print("@@@@@@@@@@@@@@@@@@# Create index@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(index)
print("@@@@@@@@@@@@@@@@@@# Create index@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# Function to get most similar documents to a query
def get_similar_documents(query, top_n=16):
    query_bow = dictionary.doc2bow(preprocess_text(query))
    query_lsi = lsi_model[query_bow]
    sims = index[query_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    similar_docs = [(i, score) for i, score in sims[:top_n]]  # Keep i as an integer
    return similar_docs

query_temp = "I am looking for a domestic animal like a cat or dog."
query_t = "I was sitting in the forest looking at tiger and bird."
query = "The dogs are sleeping under the tree. Cats are playing with birds, and there are tigers. Look at the dogs."
print("INPUT QUERY = ", query)

similar_docs = get_similar_documents(query)
print("@@@@@@@@@@@@@@@@@@@@@similar_docs@@@@@@@@@@@@@@@@@@@@@@@@")
for doc_number, sim_score in similar_docs:
    print(f"Document {doc_number + 1} (D{doc_number + 1}): Similarity = {sim_score:.4f}")
print("@@@@@@@@@@@@@@@@@@@@@similar_docs@@@@@@@@@@@@@@@@@@@@@@@@")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("Most similar document:")
print(documents[similar_docs[0][0]])  # Print the content of the most similar document
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


# Prepare data for plotting
doc_labels = [f"D{doc_number + 1}" for doc_number, _ in similar_docs]
similarity_scores = [sim_score for _, sim_score in similar_docs]

# Plotting the ranked similarity scores
plt.figure(figsize=(10, 6))
plt.barh(doc_labels, similarity_scores, color="skyblue")
plt.xlabel("Similarity Score")
plt.ylabel("Documents")
plt.title("Documents ranked by similarity to the query")
plt.gca().invert_yaxis()  # Invert y-axis for descending order
plt.show()
