from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import logging

# Set the Matplotlib backend to 'Agg'
plt.switch_backend('Agg')

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load Census Data from CSV
file_path = "data/Census Day Report FA24 modified for Jacob Tocila.csv"
try:
    df = pd.read_csv(file_path)
    logging.info("CSV file loaded successfully.")
except Exception as e:
    logging.error(f"Error loading CSV file: {e}")

@app.route('/')
def index():
    try:
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
    except Exception as e:
        logging.error(f"Error in index route: {e}")
        return "Error loading data", 500

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        gender = request.form['gender']
        ethnicity = request.form['ethnicity']
        fulltime_parttime = request.form['fulltime_parttime']
        church_affiliation = request.form['church_affiliation']
        continent = request.form['continent']
        child_of_alumni = request.form['child_of_alumni']
        student_academic_level = request.form['student_academic_level']

        # Log received data
        logging.info(f"Received data: gender={gender}, ethnicity={ethnicity}, fulltime_parttime={fulltime_parttime}, "
                     f"church_affiliation={church_affiliation}, continent={continent}, child_of_alumni={child_of_alumni}, "
                     f"student_academic_level={student_academic_level}")

        # Calculate alignment percentages
        percentages = calculate_percentages(gender, ethnicity, fulltime_parttime, church_affiliation, continent, child_of_alumni, student_academic_level)

        # Log calculated percentages
        logging.info(f"Calculated percentages: {percentages}")

        # Generate charts
        bar_chart = generate_bar_chart(percentages)
        pie_chart = generate_pie_chart(percentages)

        # Calculate weighted overall match
        weights = [0.30, 0.30, 0.05, 0.05, 0.20, 0.05, 0.05]  # Adjusted weights to prioritize gender, ethnicity, and continent
        weighted_percentages = [percent * weight for percent, weight in zip(percentages.values(), weights)]
        overall_match = sum(weighted_percentages)

        # Return results as JSON
        return jsonify(result="Your alignment with Calvin's population", bar_chart=bar_chart, pie_chart=pie_chart, percentages=percentages, overall_match=round(overall_match, 2))
    except Exception as e:
        logging.error(f"Error in calculate route: {e}")
        return jsonify(error=str(e)), 500

@app.route('/random_student', methods=['GET'])
def random_student():
    try:
        random_student = df.sample(n=1).iloc[0]
        student_data = {
            "gender": random_student["Gender"],
            "ethnicity": random_student["Ethnicity"],
            "fulltime_parttime": random_student["FullTimePartTimeIndicator"],
            "church_affiliation": random_student["ChurchAffiliation"],
            "continent": random_student["Continent"],
            "child_of_alumni": random_student["AlumniChild"],
            "student_academic_level": random_student["StudentAcademicLevel"]
        }
        # Call calculate function with the random student's data
        percentages = calculate_percentages(student_data["gender"], student_data["ethnicity"], student_data["fulltime_parttime"],
                                            student_data["church_affiliation"], student_data["continent"], student_data["child_of_alumni"],
                                            student_data["student_academic_level"])
        bar_chart = generate_bar_chart(percentages)
        pie_chart = generate_pie_chart(percentages)
        weights = [0.30, 0.30, 0.05, 0.05, 0.20, 0.05, 0.05]
        weighted_percentages = [percent * weight for percent, weight in zip(percentages.values(), weights)]
        overall_match = sum(weighted_percentages)
        return jsonify(student_data=student_data, result="Your alignment with Calvin's population", bar_chart=bar_chart, pie_chart=pie_chart, percentages=percentages, overall_match=round(overall_match, 2))
    except Exception as e:
        logging.error(f"Error in random_student route: {e}")
        return jsonify(error=str(e)), 500

def calculate_percentages(gender, ethnicity, fulltime_parttime, church_affiliation, continent, child_of_alumni, student_academic_level):
    total_students = len(df)
    percentages = {}

    if gender:
        gender_count = len(df[df["Gender"] == gender])
        percentages["Gender"] = (gender_count / total_students) * 100

    if ethnicity:
        ethnicity_count = len(df[df["Ethnicity"] == ethnicity])
        percentages["Ethnicity"] = (ethnicity_count / total_students) * 100

    if fulltime_parttime:
        fulltime_parttime_count = len(df[df["FullTimePartTimeIndicator"] == fulltime_parttime])
        percentages["Full-Time/Part-Time"] = (fulltime_parttime_count / total_students) * 100

    if church_affiliation:
        church_affiliation_count = len(df[df["ChurchAffiliation"] == church_affiliation])
        percentages["Church Affiliation"] = (church_affiliation_count / total_students) * 100

    if continent:
        continent_count = len(df[df["Continent"] == continent])
        percentages["Continent"] = (continent_count / total_students) * 100

    if child_of_alumni:
        child_of_alumni_count = len(df[df["AlumniChild"] == child_of_alumni])
        percentages["Child of Alumni"] = (child_of_alumni_count / total_students) * 100

    if student_academic_level:
        student_academic_level_count = len(df[df["StudentAcademicLevel"] == student_academic_level])
        percentages["Student Academic Level"] = (student_academic_level_count / total_students) * 100

    return percentages

def generate_bar_chart(percentages):
    fig, ax = plt.subplots()
    categories = list(percentages.keys())
    values = list(percentages.values())
    ax.bar(categories, values, color='gold')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Percentages')
    ax.set_xticklabels(categories, rotation=45, ha='right')
    # ax.set_title('Bar Chart of Percentages')

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
    ax.pie(values, labels=categories, autopct='%1.1f%%', colors=['#800000', '#FFD700', '#FF6347', '#4682B4', '#32CD32', '#FF4500', '#DA70D6'])
    # ax.set_title('Pie Chart of Percentages')

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    pie_chart = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    return pie_chart

if __name__ == '__main__':
    app.run(debug=True)