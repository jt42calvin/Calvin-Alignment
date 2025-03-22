import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define color palette
maroon = "#800000"
gold = "#FFD700"
bg_color = "#323232" # Light gray background color


# Load Census Data from CSV
file_path = "Census Day Report FA24 modified for Jacob Tocila.csv"
df = pd.read_csv(file_path)

# Extract unique values for dropdowns
genders = df["Gender"].dropna().unique().tolist()
ethnicities = df["Ethnicity"].dropna().unique().tolist()
fulltime_parttime = df["FullTimePartTimeIndicator"].dropna().unique().tolist()
church_affiliation = df["ChurchAffiliation"].dropna().unique().tolist()
continents = df["Continent"].dropna().unique().tolist()
child_of_alumni = df["AlumniChild"].dropna().unique().tolist()
student_academic_level = df["StudentAcademicLevel"].dropna().unique().tolist()

# Create UI
root = tk.Tk()
root.title("Calvin Percentage Alignment Calculator")
root.geometry("900x850")
root.configure(bg=bg_color)

# Create style
style = ttk.Style()
style.configure("TLabel", background=bg_color, foreground="white", font=("Helvetica", 12))
style.configure("TButton", background=bg_color, foreground=gold, font=("Helvetica", 12), padding=5)
style.configure("TCombobox", background=bg_color, foreground="white", font=("Helvetica", 12))

# Create custom button style
style.configure("Custom.TButton", background=bg_color, foreground=gold, font=("Helvetica", 12), padding=5)
style.map("Custom.TButton",
          background=[('active', bg_color)],
          foreground=[('active', gold)])

# Create custom red button style for close
style.configure("Custom.Red.TButton", background="red", foreground="red", font=("Helvetica", 12), padding=5)
style.map("Custom.Red.TButton",
          background=[('active', bg_color)],
          foreground=[('active', 'red')])

# Create frames
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

graph_frame = tk.Frame(root, bg=bg_color)
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

# Dropdown labels
ttk.Label(input_frame, text="Select Gender:").pack(pady=5)
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(input_frame, textvariable=gender_var, values=genders, state="readonly", style="TCombobox")
gender_dropdown.pack()

ttk.Label(input_frame, text="Select Ethnicity:").pack(pady=5)
ethnicity_var = tk.StringVar()
ethnicity_dropdown = ttk.Combobox(input_frame, textvariable=ethnicity_var, values=ethnicities, state="readonly", style="TCombobox")
ethnicity_dropdown.pack()

ttk.Label(input_frame, text="Select FullTime/PartTime:").pack(pady=5)
fulltime_parttime_var = tk.StringVar()
fulltime_parttime_dropdown = ttk.Combobox(input_frame, textvariable=fulltime_parttime_var, values=fulltime_parttime, state="readonly", style="TCombobox")
fulltime_parttime_dropdown.pack()

ttk.Label(input_frame, text="Select Church Affiliation:").pack(pady=5)
church_affiliation_var = tk.StringVar()
church_affiliation_dropdown = ttk.Combobox(input_frame, textvariable=church_affiliation_var, values=church_affiliation, state="readonly", style="TCombobox")
church_affiliation_dropdown.pack()

ttk.Label(input_frame, text="Select Continent:").pack(pady=5)
continent_var = tk.StringVar()
continent_dropdown = ttk.Combobox(input_frame, textvariable=continent_var, values=continents, state="readonly", style="TCombobox")
continent_dropdown.pack()

ttk.Label(input_frame, text="Select Child of Alumni:").pack(pady=5)
child_of_alumni_var = tk.StringVar()
child_of_alumni_dropdown = ttk.Combobox(input_frame, textvariable=child_of_alumni_var, values=child_of_alumni, state="readonly", style="TCombobox")
child_of_alumni_dropdown.pack()

ttk.Label(input_frame, text="Select Student Academic Level:").pack(pady=5)
student_academic_level_var = tk.StringVar()
student_academic_level_dropdown = ttk.Combobox(input_frame, textvariable=student_academic_level_var, values=student_academic_level, state="readonly", style="TCombobox")
student_academic_level_dropdown.pack()

# Function to compare user input with dataset
def calculate_match():
    if not gender_var.get() or not ethnicity_var.get() or not fulltime_parttime_var.get() or not church_affiliation_var.get() or not continent_var.get() or not child_of_alumni_var.get() or not student_academic_level_var.get():
        messagebox.showwarning("Input Error", "Please enter all fields.")
        return

    # Calculate matches
    total_students = len(df) # 3,681 students in dataset
    gender_match = df[df["Gender"] == gender_var.get()].shape[0]
    ethnicity_match = df[df["Ethnicity"] == ethnicity_var.get()].shape[0]
    fulltime_parttime_match = df[df["FullTimePartTimeIndicator"] == fulltime_parttime_var.get()].shape[0]
    church_affiliation_match = df[df["ChurchAffiliation"] == church_affiliation_var.get()].shape[0]
    continent_match = df[df["Continent"] == continent_var.get()].shape[0]
    child_of_alumni_match = df[df["AlumniChild"] == child_of_alumni_var.get()].shape[0]
    student_academic_level_match = df[df["StudentAcademicLevel"] == student_academic_level_var.get()].shape[0]

    # Calculate percentages from matches
    gender_percent = round((gender_match / total_students) * 100, 2)
    ethnicity_percent = round((ethnicity_match / total_students) * 100, 2)
    fulltime_parttime_percent = round((fulltime_parttime_match / total_students) * 100, 2)
    church_affiliation_percent = round((church_affiliation_match / total_students) * 100, 2)
    continent_percent = round((continent_match / total_students) * 100, 2)
    child_of_alumni_percent = round((child_of_alumni_match / total_students) * 100, 2)
    student_academic_level_percent = round((student_academic_level_match / total_students) * 100, 2)

    result_text.set(
        f"Gender Match: {gender_percent}%\n"
        f"Ethnicity Match: {ethnicity_percent}%\n"
        f"FullTime/PartTime Match: {fulltime_parttime_percent}%\n"
        f"Church Affiliation Match: {church_affiliation_percent}%\n"
        f"Continent Match: {continent_percent}%\n"
        f"Child of Alumni Match: {child_of_alumni_percent}%\n"
        f"Student Academic Level Match: {student_academic_level_percent}%"
    )
    
    # Calculate overall match by averaging the individual percentages
    percentages = [gender_percent, ethnicity_percent, fulltime_parttime_percent, church_affiliation_percent, continent_percent, child_of_alumni_percent, student_academic_level_percent]

    weights = [0.30, 0.30, 0.05, 0.05, 0.20, 0.05, 0.05]  # Adjusted weights to prioritize gender, ethnicity, and continent
    weighted_percentages = [percent * weight for percent, weight in zip(percentages, weights)]

    # Calculate overall match as the weighted average of all percentages
    overall_match = sum(weighted_percentages)
    result_text.set(result_text.get() + f"\n\nOverall Match: {round(overall_match, 2)}%")

    # Calculate the number of students that match all criteria
    exact_match = df[
        (df["Gender"] == gender_var.get()) &
        (df["Ethnicity"] == ethnicity_var.get()) &
        (df["FullTimePartTimeIndicator"] == fulltime_parttime_var.get()) &
        (df["ChurchAffiliation"] == church_affiliation_var.get()) &
        (df["Continent"] == continent_var.get()) &
        (df["AlumniChild"] == child_of_alumni_var.get()) &
        (df["StudentAcademicLevel"] == student_academic_level_var.get())
    ].shape[0]

    # Add the exact match count to the result text
    result_text.set(result_text.get() + f"\n\nNumber of students exactly like you: {exact_match}")
    result_text.set(result_text.get() + f"\n\nTotal Students: {total_students}")
    
    # Show pie chart
    show_charts(percentages)

def show_charts(percentages):
    labels = ["Gender", "Ethnicity", "FullTime/PartTime", "Church Affiliation", "Continent", "Child of Alumni", "Academic Level"]
    
    # Clear previous chart if exists
    for widget in graph_frame.winfo_children():
        widget.destroy()
    
    # Create bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, percentages, color="#F0BD00") # Gold color for bars
    ax.set_ylabel('Percentage')
    ax.set_title('Match Percentages by Category')
    
    # Angle the labels under each bar
    plt.xticks(rotation=45, ha='right')
    
    # Adjust the layout to fit everything automatically
    fig.tight_layout()
    
    # Display bar chart in the graph frame
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Create pie chart
    fig2, ax2 = plt.subplots()
    colors = ["#800000", "#901B00", "#A03600", "#C06C00", "#E0A200", "#F0BD00", "#FFD700"]
    text_colors = ['white', 'white', 'white', 'white', 'black', 'black', 'black']
    
    wedges, texts, autotexts = ax2.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.70)
    
    # Set the color of the text
    for i, autotext in enumerate(autotexts):
        autotext.set_color(text_colors[i])
    
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title('Match Percentages by Category')
    
    # Display pie chart in the graph frame
    canvas2 = FigureCanvasTkAgg(fig2, master=graph_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def pick_random_student():
    random_student = df.sample(n=1).iloc[0]
    gender_var.set(random_student["Gender"])
    ethnicity_var.set(random_student["Ethnicity"])
    fulltime_parttime_var.set(random_student["FullTimePartTimeIndicator"])
    church_affiliation_var.set(random_student["ChurchAffiliation"])
    continent_var.set(random_student["Continent"])
    child_of_alumni_var.set(random_student["AlumniChild"])
    student_academic_level_var.set(random_student["StudentAcademicLevel"])
    calculate_match()

# Button to calculate match
compare_button = ttk.Button(input_frame, text="Compare", command=calculate_match, style="Custom.TButton")
compare_button.pack(pady=0)

# Button to pick a random student
random_button = ttk.Button(input_frame, text="Pick Random Student", command=pick_random_student, style="Custom.TButton")
random_button.pack(pady=0)

# Button to close app
close_button = ttk.Button(input_frame, text="Close", command=root.destroy, style="Custom.Red.TButton")
close_button.pack(pady=0)

# Label to display results
result_text = tk.StringVar()
result_label = ttk.Label(input_frame, textvariable=result_text, font=("Helvetica", 12), background=bg_color, foreground=gold)
result_label.pack(pady=0)

# Run app
root.mainloop()