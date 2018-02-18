import json
from flask import Flask
from flask import render_template
from flask import request
from flask import json
from elasticsearch import Elasticsearch

MarvelImageRecognition = Flask(__name__)

es = Elasticsearch("http://10.19.189.64:9200")

@MarvelImageRecognition.route('/',  methods=['GET'])
def home():
  return render_template('marvel_search.html')

@MarvelImageRecognition.route('/search-results', methods=['GET', 'POST'])
def process_results():
  query_object = request.args.get('q')

  body = {
    'query': {
      'match': {
        'objects': 'gun'
      }
    }
  }

  res = es.search(index="marvel", body=body)

  print(res)

  images = {}

  for index, hit in enumerate(res['hits']['hits']):
    images[index] = hit["_source"]["url"]

  # print '***********************'
  # print images

  return json.dumps({'status': 'OK'})
