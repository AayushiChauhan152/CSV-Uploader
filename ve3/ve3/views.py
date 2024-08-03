from django.shortcuts import render
from app.models import File
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import seaborn as sns
import os
from django.conf import settings

def handle_fun(file_path):
    df = pd.read_csv(file_path)

    # Identify missing values
    missing_values = df.isnull().sum().reset_index()
    missing_values.columns = ['Column', 'Missing Values']

    # Handle missing values (example: fill with mean for numerical columns)
    df_filled = df.fillna(df.mean(numeric_only=True))

    # Collect the header and data rows after handling missing values
    header = list(df_filled.columns)
    data_rows = df_filled.values.tolist()[:11]
    combined_data = [header] + data_rows

    # Calculate summary statistics
    summary_stats = df_filled.describe().transpose().reset_index()
    summary_stats = summary_stats[['index', 'mean', '50%', 'std']]  # Selecting mean, median (50%), and std columns
    summary_stats.columns = ['Column', 'Mean', 'Median', 'Standard Deviation']
    summary_stats = summary_stats.values.tolist()

    # Generate histograms for numerical columns
    plots = []
    for column in df_filled.select_dtypes(include=['number']).columns:
        pyplot.figure()
        sns.histplot(df_filled[column], kde=True)
        plot_path = os.path.join(settings.MEDIA_ROOT, f'{column}_histogram.png')
        pyplot.savefig(plot_path)
        pyplot.close()
        plots.append(os.path.join(settings.MEDIA_URL, f'{column}_histogram.png'))

    return combined_data, summary_stats, missing_values.values.tolist(), plots

# Upload function
def upload_file(request):
    data = []
    summary_stats = []
    missing_values = []
    plots = []
    message = None
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        data, summary_stats, missing_values, plots = handle_fun(obj.file.path)
        message = "File uploaded successfully!"
        return render(request, 'upload.html', {"data": data, "messages": message, "summary_stats": summary_stats, "missing_values": missing_values, "plots": plots})
    return render(request,'upload.html')
