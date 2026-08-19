# v1 - package 1 (pandas)
# v2 - package 2 (numpy)
# v3 - package 3 (moviepy)
# ".\env2\Scripts\Activate.ps1" (To activate env2)

import moviepy
"""
pip install moviepy
python -m venv my_env # creates a local environment

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned ( execute this command if there is an error "cannot be loaded because 
running scripts is disabled on this system." )

.\my_env\Scripts\activate # activate the local env
pip install requests # Installs the "requests" library
pip install numpy==1.20.0 # Installs a specific version
pip list
pip install --upgrade requests
pip uninstall requests
pip freeze 
pip freeze > requirements.txt # Creates the requirements file
pip install -r requirements.txt # Installs packages from the fil
deactivate # return to the global environment from the local environment
"""