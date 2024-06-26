# Seach Engine
This project is my implementation of a task assigned during the Computation Methods course at AGH UST.
## Lab report
[Lab report (with search examples)](report.pdf)
## Project description
The project's goal is to develop a search engine utilizing Natural Language Processing (NLP) techniques to efficiently retrieve relevant documents from a large corpus of text data. Singular Value Decomposition (SVD) is employed for low-rank approximation of the term-by-document matrix to enhance information retrieval and reduce noise.

There were several key steps during development of this project:
- Data collection 
- Data preprocessing
- Data extraction/indexing/vectorization
- Calculating term by document matrix, and it's low rank approximation
- Querying the matrix

## Technologies used
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

## How to run
To crawl some articles: \
`python app/engine/data_generation/wikipedia_crawler_2.py` \
To process the articles: \
`python app/engine/data_processing/MainDataProcessor.py` 

If you want to run the console based search engine: \
`python app/engine/search_engine.py` \
If you want to run the web based search engine: \
`python -m flask --app app.backend run` \
The application should be available on http://localhost:5000

## Demo

https://github.com/szpn/SearchEngine/assets/41589231/5449207f-4ce3-40c5-99fe-8a7747d1218f

## Structure overview
The project is split into 3 parts, the app directory contains three pieces:
- frontend - contains the react based user interface
- backend - contains the flask server
- engine - contains the core logic of the search engine

## Engine details
The engine directory is the most important directory as it contains essential files for logic of the engine.

### Data generation
Inside the `data_generation` module, there are two wikipedia crawlers, first one was a slow prototype to get familiar with wikipedia library, the second one is faster due to multithreading. \
The wikipedia crawler works by visiting one article, and then following every link it finds on that article until max depth is reached. It saves the raw text from the article into a folder.

### Data processing
The `data_processing` module comprises scripts for processing downloaded Wikipedia articles.

#### ArticleProcessor.py
Responsible for sanitizing and processing raw article text by removing stop words, punctuation, and stemming words. Processed text is then saved onto disk.
#### DictionaryCreator.py
Generates the dictionary of words to be indexed by the engine. It adds every word from processed articles and removes less common words (occurring less than 15 times).
#### ArticleLookupMapCreator.py
Creates an array of article names to map engine results to article names.
#### ArticleVectorizer.py
Creates the term-by-document matrix using the generated dictionary. It iterates over processed articles, creating matrix rows with word occurrences. Columns are then multiplied by the Inverse Document Frequency (IDF) of each word to reduce common word significance. Finally, matrix rows are normalized and the matrix is saved onto disk.
#### ArticleVectorSVD.py
Performs low-rank approximation of the term-by-document matrix using the SVD algorithm. \
Due to RAM limitations on my PC, the result is saved as (U * S) matrix and Vh matrix. It would be better to fully compute the U * S * Vh matrix and return it, but my PC couldn't process the data I had.
#### MainDataProcessor.py
Aggregates all processing scripts, executing each to process, index, and vectorize the data.

### search_engine.py
Utilizes the generated term-by-document matrix, dictionary, and article lookup map to query articles. The user-provided query (Q) is normalized, and M * Q is computed, where M represents the term-by-document matrix. The resulting vector contains cosine similarity values for each article. By default, the engine returns the top 10 results with the highest similarity scores.
