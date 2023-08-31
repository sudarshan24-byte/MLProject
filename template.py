import os
from pathlib import Path
import logging 
'''
The logging library in Python is a built-in module that provides a flexible and customizable 
way to record messages, warnings, errors, and other information during the execution of a program.
'''

logging.basicConfig(level=logging.INFO)

project_name="mlproject"

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    '''
    It checks if the filedir (directory) is not an empty string. 
    If the directory is not empty, it tries to create the directory using os.makedirs(). 
    The exist_ok=True parameter ensures that if the directory already exists, it won't raise an error.
    '''
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")



    '''
    This Block checks whether the filepath is present or not and also whether the file is empty or not.
    If either of these conditions is met, it means the file is missing or empty. 
    In that case, it opens the file in write mode ('w') using a context manager (with open(...) as f:)
    '''
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")