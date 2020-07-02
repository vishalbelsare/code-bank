# TEXT AS DATA

Goals:

- Show a large spectrum of tools for NLP and how to use it:
    - NLTK
    - SpaCy
    - Gensim
    - Flair
    - Transformers
    - (PyTorch + TF)
    - Mention Textblob, Textacy

- Show all the different areas of NLP; data gathering; data pre-processing; text data visualization; text classification; (eventually: translation, summarization)


## Demos

### 1. Data preprocessing and EDA

#### 1.1 Data extraction
Goal: get the text data


**PDF text extraction**

1. Preparation: generate a collection of PDF-reviews
2. Load PDF data and extract information
  1.1 Compare results from "image pdf" vs "digital pdf"

Tools:
PDFMiner, PyPDF2

**Data scraping**

 Motivation: often we need to obtain the data ourself

- Scrapy: bot to scrape HTML files from websites
- Beautifulsoup4 to extract specific fields
Example with Scraping data from the Yelp website (mentioning it might be not permitted?)


#### 1.2 Text Exploratory Data Analysis
Goal: start understanding the data

1. Show top words (most common words)
2. Aggregate by tabular field such as "business"/"reviews" rating and check different top words
Can take inspiration from: [Kaggle notebook](https://www.kaggle.com/suzanaiacob/sentiment-analysis-of-the-yelp-reviews-data)
… (dataset-specific)

#### 1.3 Data cleaning
Goal: data cleaning is time-consuming but inevitable; often domain-specific


**Regular expressions** (regex) 

Suggested tutorial website: https://www.regular-expressions.info/

Goal: Understand what is regex ("we might know the wildcard notation \*.pdf)

Show an example: extract all words and digits from a string

**Removal of stopwords**

1. There are many approaches to remove stop words. NLTK is often used (we do not recommend it but probably we need to cite it)
2. Alternative: SpaCy 
3. Compare the lists of SpaCy / NLTK with just removing top words; which approach is better?


**Tokenization**

Simplest approach: split by space.

What’s the main problem? -> Appollo 13

Compare it with SpaCy -> might be slow for large datasets. We need to find a balance between execution time/accuracy.

### 2. NLP: core ideas

#### 2.1 SpaCy
Goal: explain the basics of linguistic analysis with the aid of SpaCy. Mention it exists also NLTK, but SpaCy is more powerful and faster.
Stemming/Lemming (mention)

1. Entity extraction and visualization (places, other?), idea: add a new column with the found data; might be useful during text classification.

#### 2.2 Topic modelling
Goal/theory: topic modeling with LDA.

1. LDA with Gensim + visualize and play with pyLDAvis

#### 2.3 The vector space
Goal: introduce the vector space, TF-IDF and K-means. Show the difference between supervised and unsupervised learning for text data.

Theory: metrics used for comparing cluster algorithms; clustering accuracy (purity), Normalized Mutual Information (NMI), and Adjusted Rand Index (ARI)?

**TF-IDF**
1. From scratch using a simple example. First count, then add IDF
2. Show the vector space; color by business/reviews

**K-means**
1. Apply K-means
2. Compare the results with the business labels + cluster metrics
3. Show the importance of text cleaning/preprocessing (by comparing the obtained results from the raw approach)

### 3. Text representation
Goal: once we map words into vectors; we can analyze the vector space; look for similarity, look at the latent space, ...

#### 3.1 Text similarity / Latent space
Goal: play with the previously obtained vector space
Theory: cosine similarity vs euclidean distance vs ... 

1. Given a review; find similar
2. ...

#### 3.2 Word2vec
Goal: introduce word representation using the distributional hypothesis

Theory: Word2Vec (skip-gram vs CBOW, distributional semantics, negative sampling, ...) https://en.wikipedia.org/wiki/Distributional_semantics

1. Train a small example from scratch (Probably it will be with Gensim … Alternative: https://github.com/danielfrg/word2vec)
2. Arithmetics on the vectors

#### 3.2 More embeddings
Goal: play around with any embeddings and document embeddings
Theory: introducing contextualized word embeddings (Elmo: -- Deep contextualized word representations  https://arxiv.org/abs/1802.05365), FastText (subwords), ...

1. Load FastText/Glove/Elmo embeddings with Flair
(cite) Doc2vec
2. Generate document embedding by pooling separate word embeddings

TODO: this section (3.2) might be also moved later in section 4 as the obtained embeddings from Flair might are tensors and can be fine-tuned on neural network tasks. 

### 4. Deep learning
Goal: introduce deep learning for text classification; show evolution; show improvements from baseline

With Keras as it's simple and requires less code.
Mention it exists PyTorch + torchtext

#### 4.1 From naives Bayes to simple NN
Goal: start with a simple baseline using TF-IDF + Naives Bayes. Generally, this is a very good baseline

1. TF-IDF of the whole corpus; discussion on Sparsity
2. Pick the right metric (f1? accuracy? auc-roc?)
3. Apply naives Bayes with Scikit-learn
4. Save metrics as baseline
5. Construct and train a simple NN (2 or 3 feed-forward layers )

#### 4.2 Recurrent neural network
Goal: add *memory cell* into the neural network

Theory: LSTM, GRU, …, as the input is a sequence, we want to look back into the past when making a decision

1. Construct and train a model with GRU (often preferable to LSTM as it is faster)
2. Technical discussion on“[Sequence Bucketing](https://www.kaggle.com/bminixhofer/speed-up-your-rnn-with-sequence-bucketing) to speed-up training; the main idea is to concatenate input strings.
3. Construct and train a char-level RNN. Very interesting as the model learn just by looking at sequences of characters

#### 4.3 Language Models + Transformers
Goal: explain the importance of pre-training models and transfer learning in neural networks, as well as attention

Theory: from n-grams language models to Transformers, Attention is all you need, subword algorithms: BPE, vs Wordpiece

1. Familiarize with HuggingFace website
2. Sub-tokenization; tokenizers library
3. Load BERT and add text-classification head on top
4. Train BERT (TODO we need GPUs ...)
5. Show how easy we can add other Transformer models (RoBERTa, Albert)

#### 4.4 (Extra material if necessary)

**Text translation**
from encoder/decoder models to attention


**Text summarization**
 from rule-based approach until [BART](https://arxiv.org/abs/1910.13461)


## Other ideas

- Add an extra section with even more resources; for instance:
    - [The Big Bad NLP Database](https://datasets.quantumstat.com/), a collection of 500+ NLP datasets
    - [keon/awesome-nlp](https://github.com/keon/awesome-nlp), a curated list of resources dedicated to NLP
    - ...


## Preparation

Python level
[Getting started with Jupyter Notebooks](https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46)
