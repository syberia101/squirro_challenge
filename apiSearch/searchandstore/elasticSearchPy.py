import json
import logging
from datetime import datetime
import random
from elasticsearch import Elasticsearch
from apiSearch.searchandstore import documentGetter


# connect to elastisearch
def connect_elasticsearch():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if es.ping():
        print('It is connected')
    else:
        print('Seems to be not connected')
    return es


# create_index if not already created
def create_index(es_object, index_name):
    created = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "document": {
                "properties": {
                    "date_up": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                    },
                    "title": {
                        "type": "text"
                    },
                    "text": {
                        "type": "text"
                    },
                    "summary": {
                        "type": "text"
                    }

                }

            }
        }
    }
    try:
        if not es_object.indices.exists(index_name):
            es_object.indices.create(index=index_name, ignore=400, body=settings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


def search_all_document():
    es = connect_elasticsearch()
    resultat = es.search(index="document", body={'size': 10000, 'query': {'match_all': {}}})
    return resultat


def search_documents_keyword(query_text):
    es = connect_elasticsearch()
    if es is not None:
        result = es.search(index='document', body={'query': {'match': {'text': query_text}}})
    return result


def search_document_by_id(id):
    es = connect_elasticsearch()
    if es is not None:
        result = es.search(index='document', body={'query': {'match': {'_id': id}}})
    return result


def index_a_document(title, abstract):
    es = connect_elasticsearch()
    if es is not None:
        if create_index(es, 'document'):
            document = create_document(title, abstract)
            j = json.dumps(document)
            out = store_record(es, 'document', j)
            print('Data indexed successfully ', out)
    return out


# index the data
def store_record(elastic_object, index_name, record):
    is_stored = True
    try:
        outcome = elastic_object.index(index=index_name, body=record)
        print(outcome)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))
        is_stored = False
    finally:
        return is_stored


# create a document that could be indexed
def create_document(title, text):
    date_json = datetime.now().isoformat()
    doc = {'title': title, 'text': text, "date": date_json}
    return doc


# convert the time for JSON
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def index_document_from_springer(keywork):
    # get a random number for the test to return one document to index it
    n_document = random.randint(1, 100)
    title, abstract = documentGetter.get_document_from_springer(keywork, n_document)
    logging.basicConfig(level=logging.ERROR)
    es = connect_elasticsearch()
    if es is not None:
        if create_index(es, 'document'):
            document = create_document(title, abstract)
            j = json.dumps(document)
            out = store_record(es, 'document', j)
            return out


def return_id_formated(results):
    data = [doc for doc in results['hits']['hits']]
    all_id = []
    for doc in data:
        doc_id = doc['_id']
        print('id_document: ', doc_id)
        print('title: ', doc['_source']['title'])
        print('text: ', doc['_source']['text'])
        all_id.append(doc_id)
    return all_id


def update_document(id,summary):
    es = connect_elasticsearch()
    print(summary['summary'])
    out = es.update(index='document', id=id, body={"doc": {"summary" : summary['summary']}} )
    print(out)

