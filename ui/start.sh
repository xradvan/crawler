#! /bin/bash
export FLASK_APP=index.py
export FLASK_DEBUG=1
xdg-open http://127.0.0.1:5000/
flask run
