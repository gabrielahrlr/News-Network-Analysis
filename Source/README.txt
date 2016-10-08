=====README====

News-networks script was creates in Python3.4 using the following packages:
sklearn version 0.0
newspaper version 0.0.9.8
ntlk version  3.0.1
networkx version  1.10

This folder contains 7 python scripts for different tasks:

1. extractor: Gets the news by mainstreaming the articles from the news websites. It extracts
the information needed and gives a dictionary.

2. text_processing: It contains the functions to process the text, clean it and create tokens from the text.

3. tfidf_cosine: contains two functions one to get the tf-idf of each document among a corpus (or collenction of texts)
and the cosine similarity function.

4. Network Analysis: Contains the functions to get the average shorthest path, average degree and clustering coefficient 
of the networks.

5. news-graph: Constructs the graph by giving the cosine similarity measure.

6. communities: Apply the Louvain method to a network to return its communities.

7. Example: shows examples on how to join all of them together to get the figures and results we have gotten.
 