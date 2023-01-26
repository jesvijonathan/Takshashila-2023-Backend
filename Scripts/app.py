 
from lib2to3.pgen2.tokenize import generate_tokens
from flask import Flask, jsonify, request, render_template
from flask import Flask, redirect, url_for, request, render_template, make_response
from flask_restful import Resource, Api
from flask_mail import *
import random

import hashlib
import uuid

import json

from mysql import connector

import random

import modules.database as database
from config import * 

app = Flask(__name__) 
api = Api(app)

mail = Mail(app)  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = email
app.config['MAIL_PASSWORD'] = email_password  
app.config['MAIL_USE_SSL'] = True  
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)
mail = Mail(app)

# connect to database
db = connector.connect(
host=database_host,
user=database_user,
password=database_password)

cursor = db.cursor(buffered=True)
sql = "CREATE DATABASE IF NOT EXISTS {s0}".format(s0=database_name)
cursor.execute(sql)

db = connector.connect(
host=database_host,
user=database_user,
password=database_password,
database=database_name )
cursor = db.cursor(buffered=True)

database_create = database.database_create(cursor, db)
database_create.create_base()

print("database loaded")

def generate_hash():
    encrpass = str(uuid.uuid4())
    encrpass = hashlib.sha512(encrpass.encode())
    Hash = encrpass.hexdigest()
    return Hash

@app.route('/artist_update',methods = ["POST"])
def artist_update():
    response = make_response(render_template("login/ok.html"))
    response.set_cookie('Key1', "Value1")
    response.set_cookie('Key2', "Value2")
    return response
 
@app.route('/render')
def render():
	return render_template("index.html")

@app.route('/data_dict',methods = ["POST"])
def data_dict():
    data = request.form
    return data

@app.route('/data_url/<var1>/<var2>')
def data_url(var1="", var2=""):
    return var1, var2

@app.errorhandler(404)
def page_not_found(e):
    return "Error Page", 404
 
@app.route("/")
def index(): 
    return "Landing Page" 

 
if __name__ == '__main__': 
    context = ('local.crt', 'local.key')#certificate and key files
    app.run(debug=True, ssl_context=context)


