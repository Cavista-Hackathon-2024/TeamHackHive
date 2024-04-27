from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/diagnostic")
def diagnostic():
    return render_template("pages/diagnostic.html")

@app.route('/diagnose', methods=['POST'])
def diagnose():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        illness = request.form['illness']
        symptoms = request.form['symptoms']
        
        return f"Patient Name: {patient_name}, Illness: {illness}, Symptoms: {symptoms}"

@app.route("/symptom_result")
def symptomresults():
    return render_template("pages/result.html")

@app.route("/reports")
def reports():
    return render_template("pages/reports.html")

@app.route("/nav")
def nav():
     return render_template("pages/nav.html")

if __name__ == "_main_":
	app.run(host="0.0.0.0")