from flask import Flask, render_template
from indexView import IndexView
from firestoreModel import FirestoreModel

# create Flask instance
app = Flask(__name__)

# model
baseDir = '/home/peter/programming/crawler'
model = FirestoreModel(baseDir)

# routing
@app.route('/')
def index():
	view = IndexView(model)
	return view.render()
