from flask import Flask
from flask import render_template
from flask import request

MarvelImageRecognition = Flask(__name__)

@MarvelImageRecognition.route('/')
def home():
  return render_template('marvel_search.html')

@MarvelImageRecognition.route('/search-results', methods=['POST'])
def process_results():
  search_query = request.form['marvel-query']
  return render_template('search_results.html')
