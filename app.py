

from flask import Flask, render_template,request

import bs4 as bs
import urllib.request
import re

from nltk_summary import summarizer

app = Flask(__name__)

def get_text_from_url(url) :
    scraped_data = urllib.request.urlopen(url)
    article = scraped_data.read()
    soup = bs.BeautifulSoup(article,'lxml')
    raw_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    return raw_text

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/analyze_url',methods=['GET','POST'])
def analyze_url():
    if request.method == 'POST':
        url = request.form['raw_url']
        raw_text = get_text_from_url(url)
        #raw_text = re.sub(r'\[[0-9]*\]', ' ', raw_text)
        summary = summarizer(raw_text,1)

    return render_template('index.html', input_text = raw_text, summary=summary)

@app.route('/analyze_text',methods=['GET','POST'])
def analyze_text():
    if request.method == 'POST':
        raw_text = request.form['raw_text']
        summary = summarizer(raw_text,2)

    return render_template('index.html', input_text = raw_text, summary=summary)


if __name__ == '__main__':  
   app.run(debug = True)  