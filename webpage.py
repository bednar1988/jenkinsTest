from flask import Flask
from flask import render_template
from flask import request
import pymongo

app = Flask(__name__)
myclient = pymongo.MongoClient('mongodb01.example.com',replicaset='labReplica',username='root',password='password',authSource='admin',authMechanism='SCRAM-SHA-256')
mydb = myclient["db01"]
mycol = mydb["coll01"]


@app.route("/")
def home_page():
    usersList = mycol.find()
    return render_template("index.html",
        users=usersList)

@app.route("/", methods=["POST"])
def submit_page():
    form_fname = request.form['fName']
    form_lname = request.form['lName']
    form_city = request.form['city']
    form_age = request.form['age']
    form_gender = request.form['gender']
    mydoc = {"name": form_fname, "surname": form_lname, "city": form_city, "age": form_age, "gender": form_gender}
    mycol.insert_one(mydoc)
    return home_page()
