from flask import Flask, render_template
from data_loader import load_data
from analysis import perform_all_analyses

app = Flask(__name__)

departments, employees, counseling = load_data()
imgUrls,top_courses_df,textual_analysis = perform_all_analyses(departments, employees, counseling)
data = {"department_names":departments["Department_Name"].values,"imgUrls":imgUrls,"top_courses":top_courses_df.to_dict(orient='records'),"textual_analysis":textual_analysis}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)