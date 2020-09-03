# import flask
# import elasticsearch
# from flask import request,jsonify
#
# from searchandstore.elasticSearchPy import search_document_keyword
#
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True
#
#
#
# @app.route('/api/v1/resources/document/all', methods=['GET'])
# def api_all():
#     all = search_document_keyword("saturn")
#     print(all)
#     return jsonify(all)
#
#
# @app.route('/api/v1/resources/document/all', methods=['GET'])
# def api_all():
#     all = search_document_keyword("saturn")
#     print(all)
#     return jsonify(all)
#
# app.run()
