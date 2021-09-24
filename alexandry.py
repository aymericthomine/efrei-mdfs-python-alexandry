from flask import Flask,jsonify,request
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><h1>BOOK API</h1></p>"

# THIS ROUTE DISPLAYS ALL THE BOOKS IN THE JSON FILE
@app.route('/books', methods=['GET'])
def all_books():
    # WE READ THE JSON FILE AND STORE IT IN THE DATA VARIALBE
    with open('books.json') as json_file:
        data = json.load(json_file)  
        return jsonify(data)
 
# THIS ROUTE ALLOWS YOU TO ADD A BOOK AND CHECK THAT IT DOES NOT EXIST
@app.route("/add-book", methods=["POST"])
def post_book():
    check = True
    data = request.get_json()
    with open('books.json') as json_file:
        localData = json.load(json_file)
        for index in range(len(localData['books'])):  
            if localData['books'][index]['title'] == data['title']:
                return "ERROR: This book already exist."
    if(check):
        localData['books'].append(data)
    with open('books.json','w') as json_file:
        json.dump(localData,json_file,indent=4)
    
    return jsonify(data)
    
# THIS ROUTE ALLOWS YOU TO MODIFY THE PARAMETERS OF A BOOK
@app.route("/uptade-book", methods=["PUT"])
def update_book():
    updated = False
    data = request.get_json()
    with open('books.json') as json_file:
        localData = json.load(json_file)
        for index in range(len(localData['books'])):  
            if localData['books'][index]['title'] == data['title']:
                localData['books'][index] = data
                updated = True
    if not updated:
        localData['books'].append(data)
    with open('books.json','w') as json_file:
        json.dump(localData,json_file,indent=4)
    
    return jsonify(data)

# THIS ROUTE ALLOWS YOU TO DELETE A BOOK
@app.route("/delete-book", methods=["DELETE"])
def delete_books():
    deleted = False
    data = request.get_json()
    with open('books.json') as json_file:
        localData = json.load(json_file)
        for index in range(len(localData['books'])):  
            if localData['books'][index]['title'] == data['title']:
                localData['books'].pop(index)
                with open('books.json','w') as json_file:
                    json.dump(localData,json_file,indent=4)
                return jsonify(localData)
    if not deleted:
        return "ERROR : This book doesn't exist."