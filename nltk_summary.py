import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
import re

def summarizer(raw_text, option) :
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', raw_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    formatted_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_text = re.sub(r'\s+', ' ', formatted_text)

    #breaking text into sentences
    sentence_list = sent_tokenize(article_text)
    stopwords = nltk.corpus.stopwords.words('english')

    #calculating frequency of occurrence of relevant word
    word_frequencies = {}
    for word in word_tokenize(formatted_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
        maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    #calculating sentences score for each sentence by summing the word frequencies
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    if(option == 1) :
        summary_sentences = heapq.nlargest(15, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary
    else :
        #Display the top 7 sentences with maximum score
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary