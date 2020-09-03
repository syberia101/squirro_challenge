# LittleSearchProjectDerib

##Description
This is a small application for the hiring process of Squirro.
The aim of this application is to create a small project to create a HTTP REST service that will store and retrieve a large english text.
And in another request, to retrieve the summary of it.

This application is using Elasticsearch to store and index the text. I will be really happy to discuss of my choice for Elasticsearch to store and index the

###Requirements
see requirements file for python packages
Install elasticsearch on the machine : 

Linux:
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.0-linux-x86_64.tar.gz
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.0-linux-x86_64.tar.gz.sha512
shasum -a 512 -c elasticsearch-7.9.0-linux-x86_64.tar.gz.sha512 
tar -xzf elasticsearch-7.9.0-linux-x86_64.tar.gz
cd elasticsearch-7.9.0/ 

Mac:
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.0-darwin-x86_64.tar.gz
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.0-darwin-x86_64.tar.gz.sha512
shasum -a 512 -c elasticsearch-7.9.0-darwin-x86_64.tar.gz.sha512 
tar -xzf elasticsearch-7.9.0-darwin-x86_64.tar.gz
cd elasticsearch-7.9.0/ 

####Example for the API usage: 
Get all the documents
curl -X GET http://127.0.0.1:5000/Document/

Get one document from the id of the document:
curl -X GET http://127.0.0.1:5000/DocumentFromID/Uj2FUHQB9msvMyFURqWy

Get the summarisation from an id:
curl -X GET http://127.0.0.1:5000/DocumentSummarisation/Uj2FUHQB9msvMyFURqWy

Post a document (Json):
curl --location --request POST 'http://127.0.0.1:5000/DocumentUpload/?title=this%20is%20the%20title&text=this%20is%20the%20text'

Post a document(file):
curl -L -X POST 'http://127.0.0.1:5000/DocumentUpload/text1.txt'

Post a document(Springer):
curl -L -X POST 'http://127.0.0.1:5000/DocumentFromSpringer/deRibaupierre'
