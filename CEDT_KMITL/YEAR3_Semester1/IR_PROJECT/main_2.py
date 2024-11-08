#Python-Script (2.7) for LSI (Latent Semantic Indexing) Document Matching (Example)
#Author: Franziska Weng
#License: Attribution 4.0 International (CC BY 4.0)
#License-URL: https://creativecommons.org/licenses/by/4.0/
#Language: English


#PACKAGES
import nltk
import re
import numpy as np
from gensim import corpora, similarities
from gensim.models import LsiModel
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download("wordnet")


#FUNCTIONS

#function to filter out stopwords and apply word stemming
def filter_words_and_get_word_stems(document, word_tokenizer, word_stemmer,
                                    stopword_set, pattern_to_match_words=r"[^\w]",
                                    word_length_minimum_n_chars=2):
    """Remove multiple white spaces and all non word content from text and
    extract words. Then filter out stopwords and words with a length smaller
    than word_length_minimum and apply word stemmer to get wordstems. Finally
    return word stems.
    """
    document = re.sub(pattern_to_match_words, r" ", document)
    document = re.sub(r"\s+", r" ", document)
    words = word_tokenizer.tokenize(document)
    words_filtered = [word.lower()
                      for word in words
                      if word.lower() not in stopword_set and len(word) >= word_length_minimum_n_chars]
    word_stems = [word_stemmer.lemmatize(word) for word in words_filtered]
    return(word_stems)


#INPUT

#training text data to calculate TF-IDF model from
documents_train = [
  "She goes to school.",
  "She runs to the shop.",
  "I go to school and he goes to the shop."]

#test data text data to match 
document_test = "He runs to school."


#PREPROCESS

#set stopword set, word stemmer and word tokenizer
stopword_set = set(stopwords.words("english"))
word_tokenizer = nltk.tokenize.WordPunctTokenizer()
word_stemmer =  nltk.WordNetLemmatizer()

#apply cleaning, filtering and word stemming to training documents
word_stem_arrays_train = [
        filter_words_and_get_word_stems(
                str(document),
                word_tokenizer,
                word_stemmer,
                stopword_set
                ) for document in documents_train]
print("Word Stems of Training Documents:", word_stem_arrays_train)

#apply cleaning, filtering and word stemming to test document
word_stem_array_test = filter_words_and_get_word_stems(
        document_test,
        word_tokenizer,
        word_stemmer,
        stopword_set)
print("Word Stems of Test Document:", word_stem_array_test)


#PROCESS

#create dictionary containing unique word stems of training documents
#TF (term frequencies) or "global weights"
dictionary = corpora.Dictionary(
  word_stem_array_train
  for word_stem_array_train in word_stem_arrays_train)
print("Dictionary :", dictionary)

#create corpus containing word stem id from dictionary and word stem count
#for each word in each document
#DF (document frequencies, for all terms in each document) or "local weights"
corpus = [
  dictionary.doc2bow(word_stem_array_train)
  for word_stem_array_train in word_stem_arrays_train]
print("Corpus :", corpus)

#create LSI model (Latent Semantic Indexing) from corpus and dictionary
#LSI model consists of Singular Value Decomposition (SVD) of
#Term Document Matrix M: M = T x S x D'
#and dimensionality reductions of T, S and D ("Derivation")
lsi_model = LsiModel(
        corpus=corpus,
        id2word=dictionary #, num_topics = 2 #(opt. setting for explicit dim. change)
        )
print("Derivation of Term Matrix T of Training Document Word Stems: ",
      lsi_model.get_topics())
#Derivation of Term Document Matrix of Training Document Word Stems = M' x [Derivation of T]
print("LSI Vectors of Training Document Word Stems: ",
      [lsi_model[document_word_stems] for document_word_stems in corpus])

#calculate cosine similarity matrix for all training document LSI vectors
cosine_similarity_matrix = similarities.MatrixSimilarity(lsi_model[corpus])
print("Cosine Similarities of LSI Vectors of Training Documents:",
      [row for row in cosine_similarity_matrix])

#calculate LSI vector from word stem counts of the test document and the LSI model content
vector_lsi_test = lsi_model[dictionary.doc2bow(word_stem_array_test)]
print("LSI Vector Test Document:", vector_lsi_test)

#perform a similarity query against the corpus
cosine_similarities_test = cosine_similarity_matrix[vector_lsi_test]
print("Cosine Similarities of Test Document LSI Vectors to Training Documents LSI Vectors:",
      cosine_similarities_test)


#OUTPUT

#get text of test documents most similar training document
most_similar_document_test = documents_train[np.argmax(cosine_similarities_test)]
print("Most similar Training Document to Test Document:", most_similar_document_test)