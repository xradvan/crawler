from flask import Flask, render_template
from indexView import IndexView
from firestoreModel import FirestoreModel
from os import environ

# create Flask instance
app = Flask(__name__)

# model
baseDir = environ['CRAWLER_HOME']
model = FirestoreModel(baseDir)

# routing
@app.route('/')
def index():
	view = IndexView(model)
	return view.render()
