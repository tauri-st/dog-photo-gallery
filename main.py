from flask import Flask, render_template, request
import requests

#imports a dictionary of data from dog_breeds.py and "prettifies", or styles, the dog names when they appear in the HTML page
from dog_breeds import prettify_dog_breed

app = Flask("app")

#function adds a dash in the URL between breed names with multiple words like miniature poodle
def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/", methods=["GET","POST"])
def dog_image_gallery():
  errors = []
  if request.method == "POST":
      #gets the breed name from the form,
      #saves data from request method
      #breed string correspond to the dropdown menu
      breed = request.form.get("breed")
  return render_template("dogs.html")


app.debug = True
app.run(host='0.0.0.0', port=8080)