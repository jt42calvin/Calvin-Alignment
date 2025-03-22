from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests

app = Flask(__name__)

# Load Census Data from CSV
file_path = "data/Census Day Report FA24 modified for Jacob Tocila.csv"
df = pd.read_csv(file_path)

@app.route('/')
def index():
    genders = df["Gender"].dropna().unique().tolist()
    ethnicities = df["Ethnicity"].dropna().unique().tolist()
    fulltime_parttime = df["FullTimePartTimeIndicator"].dropna().unique().tolist()
    church_affiliation = df["ChurchAffiliation"].dropna().unique().tolist()
    continents = df["Continent"].dropna().unique().tolist()
    child_of_alumni = df["AlumniChild"].dropna().unique().tolist()
    student_academic_level = df["StudentAcademicLevel"].dropna().unique().tolist()
    return render_template('index.html', genders=genders, ethnicities=ethnicities, fulltime_parttime=fulltime_parttime,
                           church_affiliation=church_affiliation, continents=continents, child_of_alumni=child_of_alumni,
                           student_academic_level=student_academic_level)

@app.route('/calculate', methods=['POST'])
def calculate():
    gender = request.form['gender']
    ethnicity = request.form['ethnicity']
    fulltime_parttime = request.form['fulltime_parttime']
    church_affiliation = request.form['church_affiliation']
    continent = request.form['continent']
    child_of_alumni = request.form['child_of_alumni']
    student_academic_level = request.form['student_academic_level']

    # Call Azure web service
    azure_service_url = "core290-jt42calvin-percent-bhebczfybmhtf4fe.eastus-01.azurewebsites.net"
    payload = {
        'gender': gender,
        'ethnicity': ethnicity,
        'fulltime_parttime': fulltime_parttime,
        'church_affiliation': church_affiliation,
        'continent': continent,
        'child_of_alumni': child_of_alumni,
        'student_academic_level': student_academic_level
    }
    response = requests.post(azure_service_url, json=payload)
    result = response.json()

    # Return results as JSON
    return jsonify(result=result['result_text'], percentages=result['percentages'])

if __name__ == '__main__':
    app.run(debug=True)
    
## 