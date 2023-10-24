# importing redirect 
from flask import Flask, redirect, url_for, render_template, request, jsonify
  
# Initialize the flask application 
app = Flask(__name__) 
  
# It will load the form template which  
# is in login.html 
@app.route('/') 
def index(): 
    return render_template("index.html") 
  
  
@app.route('/success') 
def success(): 
    return "logged in successfully"
  
# loggnig to the form with method POST or GET 
@app.route("/login", methods=["POST", "GET"]) 
def login(): 
    
    # if the method is POST and Username is admin then 
    # it will redirects to success url. 
    if request.method == "POST" and request.form["username"] == "admin": 
        return redirect(url_for("success")) 
  
    # if the method is GET or username is not admin, 
    # then it redirects to index method. 
    return redirect(url_for('index')) 

@app.route("/postman_test",methods = ["POST", "GET"])
def postLogin():

    if request.method == "POST" and request.json["username"] == "admin": 
        return jsonify("Successful!")
    
    return jsonify("Not Successful!")


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
