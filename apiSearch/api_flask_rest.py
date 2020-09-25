from flask import Flask, request
from flask_restful import Api, Resource
import elasticSearchPy as ela
import summariseApi as summ
import os
import SummarisationBert as summBert

app = Flask(__name__)
api = Api(app)

UD = "./file_example"


class DocumentFromKeywork(Resource):
    def get(self, keyword):
        """Returns json of all the documents that contains a keyword"""
        documents = ela.search_documents_keyword(keyword)
        return {'doc_id': documents["hits"]["hits"]}, 200 if documents else 404


class Document(Resource):
    def get(self):
        """Returns json of all the documents"""
        documents = ela.search_all_document()
        return {'doc_id': documents["hits"]["hits"]}, 200 if documents else 404


class DocumentFromId(Resource):
    def get(self, id):
        """Returns json of the document with the specific id"""
        document = ela.search_document_by_id(id)
        data = document['hits']['hits'][0]['_source']['text']
        return {'doc': data}, 200 if data else 404


class DocumentUploadFromFile(Resource):
    def post(self, fname):
        """Post a document from a file, should be a text file with attribute title first line, text second line, will be indexed in the elastisearch server"""
        f = open(os.path.join(UD, fname))
        title = f.readlines(1)
        text = f.readlines(2)
        ela.index_a_document(title, text)
        return {'title': title, 'text': text}, 201 if title else 404


class DocumentUploadFromSpringer(Resource):
    def post(self, keyword):
        """Post a document from a document springer, with the title and abstract, will be indexed in the elastisearch server"""
        out = ela.index_document_from_springer(keyword)
        return {'new document uploaded into the elastisearch from springer': out}, 201


class DocumentUploadFromArgument(Resource):
    def post(self):
        """Post a document from the argument in the url"""
        ela.index_a_document(request.args.get('title'), request.args.get('text'))
        return {'title': request.args.get('title'), 'text': request.args.get('text')}, 201


class DocumentSummarisation(Resource):
    def get(self, id):
        """get summarisation from document id"""
        document = ela.search_document_by_id(id)
        data = document['hits']['hits'][0]['_source']['text']
        #summary = summ.summarisation_document(data)
        summary = summBert.summarise(data)
        return {'summary': summary}, 200 if summary else 404




api.add_resource(DocumentFromKeywork, '/Document/<string:keyword>')
api.add_resource(Document, '/Document/')
api.add_resource(DocumentFromId, '/DocumentFromID/<string:id>')
api.add_resource(DocumentUploadFromFile, '/DocumentUpload/<fname>')
api.add_resource(DocumentUploadFromSpringer, '/DocumentFromSpringer/<string:keyword>')
api.add_resource(DocumentUploadFromArgument, '/DocumentUpload/')
api.add_resource(DocumentSummarisation, '/DocumentSummarisation/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
