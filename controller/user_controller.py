from app import app
# from flask import Flask
from flask import request
from model_controller.user_model import get_all_model
obj= get_all_model() 

@app.route("/get")
def get_all():
    return obj.get_all()

@app.route("/add_one",methods=["POST"])
def add_one():
    return obj.add_one(request.form)

@app.route("/update_one",methods=["PUT"])
def update():
    return obj.update_one(request.form)


@app.route("/delete/<id>",methods=["DELETE"])
def delete(id):
    return obj.delete_user(id)

