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