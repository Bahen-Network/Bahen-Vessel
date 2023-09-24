import json
import os
import requests
import subprocess
import tempfile

def perform_training_task(task):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Download files and data from greenfield
        print("Downloading data and script...")
        bucket_name = task[4].split('/')[-1]
        print(bucket_name)
        data = download_files_by_request(bucket_name)
        train_script_path = os.path.join(temp_dir, 'train.py')
        with open(train_script_path, 'wb') as f:
            f.write(data)

        # Run the training script
        print("Performing training task...")
        subprocess.call(["python", train_script_path, "--bucket", bucket_name])

def download_files_by_request(bucket_name):
    file_service_url = 'http://bahenfileservice.azurewebsites.net/api/v1/objects'
    params = {'bucketName': bucket_name, 'objectName': 'train.py'}
    response = requests.get(file_service_url, params=params)
    response.raise_for_status()

    data = response.content
    return data
