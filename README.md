# Structure Based Hate Speech Detection

Contributors: Ravsimar Singh, Ishita Vohra, Aniket Shrimal, Harsh Shukla

## Usage
All source code is in the `src` folder. Most of our code is in the form of jupyter notebooks

## Problem Statement 
Traditional methods for hate speech detection use tons of training data to mine the hateful structure but due to disproportionate use of different terms they are prone towards learning bias against specific objects, personalities or groups. Idea is to propose a method that takes into account the grammatical structure of the sentence to predict hatefulness.

## Data
We are using already available data on Twitter for hate speech recognition consisting of around 25,000 tweets. Each tweet is classified into 3 categories - Hate speech, Offensive, or neither. We use this information to build a classifier for new tweets.

| Class | No of Tweets  |
| ------- | --- |
| Hate Speech | 1431 |
| Offensive | 19190 |
| Neither | 4163 |

## Preprocessing
We have used the following techniques for preprocessing:
- Stopword Removal - A stop word is a commonly used word (such as “the”, “a”, “an”, “in”). These are usually removed as a part of preprocessing since they do not convey any meaning, but instead, are used to provide fluidity to the sentence.
- Removing excess letters, other twitter specific data (URLs, @mentions, hashtags) - Particularly in social media, these types of words are unique and must be removed, since they do not contribute much to actual meaning being conveyed in the sentence.

## Feature Extraction
*Vectorization* - We call vectorization the general process of turning a collection of text documents into numerical feature vectors. This specific strategy (tokenization, counting and normalization) is called the Bag of Words or “Bag of n-grams” representation. Documents are described by word occurrences while completely ignoring the relative position information of the words in the document. Scikit-learn provides utilities for the most common ways to extract numerical features from text content, namely:
  * tokenizing strings and giving an integer id for each possible token, for instance by using white-spaces and punctuation as token separators.
  * counting the occurrences of tokens in each document.
  * normalizing and weighting with diminishing importance tokens that occur in the majority of samples/documents.
We used the following features:
* CountVectorizer - It counts the number of times a token shows up in the document and uses this value as its weight.
* TfIdfVectorizer - TF-IDF stands for "term frequency-inverse document frequency", meaning the weight assigned to each token not only depends on its frequency in a document but also how recurrent that term is in the entire corpora.It converts the text documents to a matrix of tfidf features. The combinations of n grams which we used are as follows: 
  * Unigrams
  * Unigrams and Bigrams
  * Unigrams, Bigrams and Trigrams
* POS Tagging - 

## Model Architecture
Our baseline models include models such as Logistic Regression, SVMs and LSTMs. Our final code implements a more complex model, TreeLSTM, to incorporate structure into our models. Using TreeLSTM, we are able to use the Dependency Parse Trees as features in our model. Traditionally, LSTMs are sequential in nature and giving tree like non-linear inputs is a challenge. We are able to solve this using TreeLSTM, which actually utilizes the parent-child relationship of the tree nodes to learn about the structure of the given sentence.
![TreeLSTM](docs/treelstm.png)

