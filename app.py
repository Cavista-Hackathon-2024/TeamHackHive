from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/diagnostic")
def diagnostic():
    return render_template("pages/diagnostic.html")

@app.route("/symptom_result")
def symptomresults():
    return render_template("pages/result.html")

if __name__ == "_main_":
	app.run(host="0.0.0.0")