# Supermind Task

This is a submission to a task given by Supermind for the role of Data Science intern.

## The Problem

Extracting crypto related words from conversational text messages.

## The solution

### Part 1:

The dataset provided with contains a corpus of crypto related words is limited. Increasing the number of words would be an extremely cumbersome task because it would require a manual updation of the list every time.\

I’ve proposed a solution to significantly increase the ease of finding new crypto related words using an unsupervised approach.

##The approach:
Latent Dirichlet Allocation (LDA) is a generative probabilistic model that assumes each topic is a mixture over an underlying set of words, and each document is a mixture of over a set of topic probabilities.\
Here the topic is only one (crypto) and for documents, I’ve taken each document to be a separate crypto group on telegram.

### Step 1

I’ve created a script scrape_telegram.py to scrape for obtaining the messages  
from targeted groups on telegram using an open source library called telethon.
Few of the groups I scrapped from are below.

![1](./images/1.png)

I have all the messages on each group in a separate row of the dataframe data_scrapped.csv

![2](./images/2.png)

### Step 2:

For preprocessing, I’ve used the stopwords provided by nltk library as well as my custom list that is saved in stopwords.txt. I’ve gone ahead and additionally removed wallet ID and numbers from the text.

![3](./images/3.png)

### Step 3:

For the inputs to the LDA algorithm, I’ve used a count vectorizer that stores the count of each word across documents. Additionally I’ve also used bigrams as well. Bigrams are two consecutive words that are considered as part of the corpus.\

For example: In the sentence, “Espresso is awesome, and user-friendly” the bigrams are :
“Espresso is”
“is awesome”
“and user”
“user friendly”
