# from flask import Flask, app
# from flask import render_template, request, jsonify, make_response
# import pandas as pd
# app = Flask(__name__)
#
# @app.route("/upload_static_file", methods=["GET", "POST"])
# def upload_files():
#     if request.method == "POST":
#         file = request.files["file"]
#         filesize = request.cookies.get("filesize")
#         print(f"FileSize: {filesize}")
#         print(file)
#         res = make_response(jsonify({"message": f"{file.filename} uploaded"}), 200)
#         return res
#     return render_template("browse.html")
#
# if __name__ == "__main__":
#  app.run(host='0.0.0.0', debug=True)

from flask import Flask, request, render_template, jsonify
#from flask_cors import CORS
app = Flask(__name__)
#CORS(app)
@app.route('/', methods= ['GET', 'POST'])
def get_message():
 # if request.method == "GET":
 print("Got request in main function")
 return render_template('browse.html')


@app.route('/upload_static_file', methods=['POST'])
def upload_static_file():
 print("Got request in static files")
 print(request.files)
 f = request.files['static_file']
 f.save(f.filename)
 resp = {"success": True, "response": "file saved!"}
 return jsonify(resp), 200
if __name__ == "__main__":
 app.run()
