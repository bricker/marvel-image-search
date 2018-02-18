from flask import Flask
from flask import render_template
from flask import request
from elasticsearch import Elasticsearch

MarvelImageRecognition = Flask(__name__)
es = Elasticsearch("http://10.19.189.64:9200")

@MarvelImageRecognition.route('/')
def home():
  return render_template('marvel_search.html')

@MarvelImageRecognition.route('/search-results', methods=['POST'])
def process_results():
  search_object = request.form['marvel-query']
  body = {
    'query': {
      'match': {
        'objects': search_object
      }
    }
  }

  res = es.search(index="marvel", body=body)
  images = []

  for hit in res['hits']['hits']:
    images.append(hit["_source"]["url"])

  return render_template('search_results.html', images=images)
