import os
import logging
from pathlib import Path 

# Configure logging format and level
logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s]")

# Define the project name (used for folder structure)
project_name="Medical_Insurance_Charges_Estimator"

# List of files & directories to create for the project
list_of_files=[
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", 
    "schema.yaml", 
    "main.py", 
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"]


# Loop through all file paths and create them if not already present
for filepath in list_of_files:
    filepath=Path(filepath)
    file_dir,file_name=os.path.split(filepath)

    # Create directory if it doesn't exist
    if file_dir != "": 
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"{file_dir} created for {file_name}")

    # Create an empty file if it doesn’t exist OR is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass # just create an empty file
        logging.info(f"create empty {file_name}")

    else:
        logging.info(f"{file_name} is already exits....")
