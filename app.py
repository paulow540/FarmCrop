from flask import Flask, render_template, request,jsonify, url_for
import os
import pickle
import pandas as pd
import numpy as np



picfolder = os.path.join("static","images")

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
app.config["UPLOAD_FOLDER"] = picfolder

@app.route("/")
def home():

    return render_template("myhome.html")





if  __name__ == "__main__":
    app.run(debug=True)     