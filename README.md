#  University Data Analysis

A Flask-based web application to analyze and visualize university data.  
Built with **Python, Pandas, Matplotlib, and Flask**, this project provides both a web interface and REST APIs to perform data exploration, generate insights, and visualize results.

---

## Features

- **Data Analysis**: Summarizes university data (counts, averages, distributions, etc.)  
- **Visualization**: Generates plots/graphs with Matplotlib for trends and comparisons  
- **REST APIs**: Exposes processed data and visualizations via endpoints  
- **CSV Handling**: Reads and processes CSV datasets  
- **Web UI**: Simple interface to view results (Flask + HTML templates)  

---

## Tech Stack

- **Backend**: Flask (Python)  
- **Data Processing**: Pandas, NumPy  
- **Visualization**: Matplotlib  
- **Frontend**: HTML, CSS, Bootstrap (via Flask templates)  

---

## Project Structure


University-Data-Analysis/<br>
├── app.py  # Main Flask application<br>
├── analysis.py  # Data analysis & visualization<br>
├── data_loader.py  # Data loading/cleaning utilities<br>
├── csv/  # Raw data files<br>
├── static/  # Static files (CSS, charts)<br>
├── templates/  # HTML templates<br>
├── requirements.txt  # Dependencies<br>
└── README.md  # Documentation

---

## Installation & Setup

1. Clone the repository

    ```bash
    git clone https://github.com/deeppatel1809/University-Data-Analysis.git
    cd University-Data-Analysis
    ```

2. Create a virtual environment (recommended)

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment

    Windows:
        
        venv\Scripts\activate

    Linux / macOS:

        source venv/bin/activate
        
4. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask application

    ```bash
    flask run
    ```

6. Open in browser:

    ```bash
    http://127.0.0.1:5000/
    ```

---
   
## Project Screenshots

- **Home Page**

    <p>
        <img src="https://github.com/user-attachments/assets/8ffb5f61-659b-4c67-992d-5a2c1c3f3e39" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;
        <img src="https://github.com/user-attachments/assets/4179e69f-3cf7-4ff7-8e6e-434528ee3fc1" width="30%" />
    </p>

- **Dashboard**

    <img src="https://github.com/user-attachments/assets/7324922d-7f3f-4433-be41-b223a832cebf" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://github.com/user-attachments/assets/7014c997-34f6-441d-80b0-513f7c8afdcc" width="30%" />

- **Visual Insights**
  
    <img src="https://github.com/user-attachments/assets/db3c6017-7f8f-4bde-ae51-5fe85348da49" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://github.com/user-attachments/assets/fff93ac2-d0e6-4496-a739-336db733a797" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://github.com/user-attachments/assets/6797e72f-4638-4b74-a838-751a472d67b2" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;<br><br>
    <img src="https://github.com/user-attachments/assets/281f98b5-4193-495e-ad2f-82c5bc40f6c6" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://github.com/user-attachments/assets/b3bb8735-0706-46a7-a75d-99bf72192c59" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://github.com/user-attachments/assets/cbda19e3-b00a-4105-b63f-96bd140f27d5" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;<br><br>
    <img src="https://github.com/user-attachments/assets/2b4dbcb8-e483-4523-9031-436d4d887789" width="30%" />

- **Textual Analysis**

    <img src="https://github.com/user-attachments/assets/26017e8d-11aa-4a10-8769-29fb810c2b56" width="30%" />&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://github.com/user-attachments/assets/a9c647cd-ed3f-46cc-994c-ed8f88decfab" width="30%" />
    