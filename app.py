import json
from flask import Flask
from flask.ext.jsonpify import jsonify
from flask import render_template
from flask import request
from flask import json
from elasticsearch import Elasticsearch

MarvelImageRecognition = Flask(__name__)

es = Elasticsearch("http://10.21.154.54:9200")

@MarvelImageRecognition.route('/',  methods=['GET'])
def home():
  return render_template('marvel_search.html')

@MarvelImageRecognition.route('/search-results', methods=['GET', 'POST'])
def process_results():
  query_object = request.args.get('q')

  body = {
    'query': {
      'match': {
        'objects': query_object
      }
    }
  }

  res = es.search(index="marvel", body=body)

  images = {}
  for index, hit in enumerate(res['hits']['hits']):
    images[index] = hit["_source"]["url"]

  return jsonify(images)
