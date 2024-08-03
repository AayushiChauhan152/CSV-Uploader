# CSV Uploader with Data Analysis

This Django application allows users to upload CSV files, analyze data, and visualize summary statistics and histograms.

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system
- pip package manager
- Django framework

### Installation

1. Clone the repository
   
### Install dependencies:
pip install -r requirements.txt

### Apply migrations to set up the database:
python manage.py migrate

### Run the Django development server:
python manage.py runserver

Access the application in your web browser at http://localhost:8000

## Project Overview
This project includes the following components:

### File Upload: 
Users can upload CSV files using a form.
### Data Handling: 
The backend processes uploaded files to handle missing values (filled with means) and computes summary statistics (mean, median, standard deviation).
### Data Visualization: 
Histograms are generated for numerical columns using matplotlib and seaborn.
### Navigation: 
The frontend includes a navigation bar that allows users to jump to different sections of the page (Upload, Data, Summary Statistics, Missing Values, Histograms).
### Responsive Design: 
Bootstrap is used for styling to ensure the application is mobile-friendly.

### Technologies Used
Backend: Python, Django, pandas, matplotlib, seaborn <br>
Frontend: HTML, CSS (Bootstrap)<br>
Database: SQLite (default for Django)<br>
