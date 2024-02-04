import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

if  __name__ == "__main__":

    # Get the current working directory
    cwd = os.getcwd()
    logging.info(f"Current working directory: {cwd}")

    # Accept the name of the project
    project_name = input("Enter the name of the project: ")
    logging.info(f"Project name: {project_name}")

    # Create the project directory
    project_dir = Path(cwd) / project_name
    project_dir.mkdir(exist_ok=True)
    logging.info(f"Project directory created: {project_dir}")

    # Go into the project directory
    os.chdir(project_dir)
    logging.info(f"Current working directory: {os.getcwd()}")

    # Create the directory structure using these list of files

    list_of_files=[
    "Readme.md",
    "artifacts",
    "notebooks",
    ".gitignore",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_tranier.py",
    f"src/components/model_monitering.py",
    f"src/pipelines/__init__.py",
    f"src/pipelines/training_pipeline.py",
    f"src/pipelines/prediction_pipeline.py",
    f"src/exception.py",
    f"src/logger.py",
    f"src/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    ]
    
    for filepath in list_of_files:
        
        if '.' not in filepath and filepath not in ["Dockerfile"]:
            os.makedirs(filepath, exist_ok=True)
            logging.info(f"Creating directory: {filepath}")
            continue

        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)
        
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory:{filedir} for the file {filename}")

        
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath,'w') as f:
                pass
                logging.info(f"Creating empty file: {filepath}")

    # Add the content to Readme.md
    with open("Readme.md", "w") as f:
        f.write(f"# {project_name}\n\n## This is created by template file for a python project.")
        logging.info(f"Creating Readme.md")

    # Add the content to .gitignore
    with open(".gitignore", "w") as f:
        f.write("""# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
""")
        
        logging.info(f"Creating .gitignore")

    # Add the content to setup.py
    with open("setup.py", "w") as f:
        f.write(f"""from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    with open('requirements.txt') as f:
        return f.read().splitlines()
    

setup(
name='{project_name}',
version='0.0.1',
author='rohan',
author_email='rohansiddeshwara@gmail.com',
packages=find_packages(),
install_requires=get_requirements().remove("-e .")
)""")
        logging.info(f"Creating setup.py")

    # Add the content to requirements.txt
    with open("requirements.txt", "w") as f:
        f.write("-e .")
        logging.info(f"Creating requirements.txt")




    # Add the content to logger.py
    with open(f"src/logger.py", "w") as f:
        f.write("""import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(levelname)s [%(filename)s:%(lineno)d] - %(message)s',
    level=logging.INFO,
)""")
        logging.info(f"Creating logger.py")



    # Add the content to exception.py
    with open(f"src/exception.py", "w") as f:
        f.write(f"""import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)

    def __str__(self):
        return self.error_message""")

        logging.info(f"Creating exception.py")

    # Add the content to utils.py
    with open(f"src/utils.py", "w") as f:
        f.write("""import os
import sys
import pickle
from src.exception import CustomException
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
""")
        logging.info(f"Creating utils.py")


    # Add the content to main.py
        # write a simple print statement
    with open("main.py", "w") as f:
        f.write(f"""from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
import os

if __name__ == "__main__":
    try:
        logging.info("Hello World")
        print(f"Hello World from {project_name}")
        save_object("artifacts/sample.pkl", "Hello World")
        logging.info("successfully saved the object")
    except CustomException as e:
        logging.error(e)
""")
        logging.info(f"Creating main.py")

    # Add the content to app.py
        # create a simple flask app
    with open("app.py", "w") as f:
        f.write(f"""from flask import Flask
from flask-cors import CORS

from src.logger import logging
from src.exception import CustomException


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    try:
        logging.info("Hello World")
        return "Hello, World!"
    except CustomException as e:
        logging.error(e)
        return "Error occured"

if __name__ == "__main__":
    logging.info("Starting the app")
    app.run(host="0.0.0.0", port=5000)
""")


    
    # run the command to create the virtual environment
    os.system("python3 -m venv ./venv")
    logging.info(f"Creating virtual environment")

    # deactivate existing the virtual environment
    try:
        os.system("deactivate")
        os.system("conda deactivate")
        logging.info(f"Deactivating the virtual environment")
    except:
        logging.info(f"No virtual environment to deactivate")


    # run the command to activate the virtual environment
    logging.info(f"Activating virtual environment......")
    os.system("source venv/bin/activate")
    logging.info(f"Virtual environment activated")

    # deactivate conda environment
    try:
        os.system("conda deactivate")
        logging.info(f"Deactivating conda environment")
    except:
        logging.info(f"No conda environment to deactivate")
    

    # run the command to install the dependencies
    logging.info(f"Installing the dependencies")
    os.system("pip3 install -r requirements.txt")
    

    # run the command to execute the main.py
    os.system("python3 main.py")
    logging.info(f"Executing the main.py")

    # run commanda to initialize git
    logging.info(f"Initializing git")
    os.system("git init")


    # run the command to open the project in vscode
    os.system("code .")
    logging.info(f"Opening the project in vscode")

    # delete the pkl file
    os.remove("artifacts/sample.pkl")

    # deactivate the virtual environment
    os.system("deactivate")
    logging.info(f"Sucessfully deactivated the virtual environment")

    
