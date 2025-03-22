from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests
import matplotlib.pyplot as plt
import io
import base64

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
    azure_service_url = "https://core290-jt42calvin-percent-bhebczfybmhtf4fe.eastus-01.azurewebsites.net/api/calculate"
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

    # Generate charts
    bar_chart = generate_bar_chart(result['percentages'])
    pie_chart = generate_pie_chart(result['percentages'])

    # Return results as JSON
    return jsonify(result=result['result_text'], bar_chart=bar_chart, pie_chart=pie_chart)

def generate_bar_chart(percentages):
    fig, ax = plt.subplots()
    categories = list(percentages.keys())
    values = list(percentages.values())
    ax.bar(categories, values)
    ax.set_xlabel('Categories')
    ax.set_ylabel('Percentages')
    ax.set_title('Bar Chart of Percentages')

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    bar_chart = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    return bar_chart

def generate_pie_chart(percentages):
    fig, ax = plt.subplots()
    categories = list(percentages.keys())
    values = list(percentages.values())
    ax.pie(values, labels=categories, autopct='%1.1f%%')
    ax.set_title('Pie Chart of Percentages')

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    pie_chart = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    return pie_chart

if __name__ == '__main__':
    app.run(debug=True)