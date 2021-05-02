# RADIUS
Two-Factor Authentication Using RADIUS test client


# Cloning the repository

1. Create a projects folder (if you don't have one): `mkdir path_to_project_folder`
2. Go to the projects folder: `$ cd path_to_project_folder`
3. To clone a repository with git clone <url>. `$ git clone https://github.com/xandrade/radius.git`


# Creating enviroment on Windows

1. Go to the project folder, for example: `cd path_to_project_folder`
2. Create virtual enviroment: `python -m venv .venv`
2.1 if error 'Error: [WinError 2] The system cannot find the file specified' is shown, try `py -3.7 -m venv .venv`
3. Activate environment `.venv\Scripts\activate.bat`
4. After the virtual environment is active, we are going to want to ensure that a couple of essential Python packages within the virtual environment are up to date: `(.venv)> pip install -U setuptools pip`
5. Install the requirements: `(.venv)> pip install -r requirements.txt`
6. Open VSCode `(.venv)> code .`

# Excecutable (exe) creation

1. Go to the project folder `$ cd path_to_project`
2. Activate environment `$ .venv\Scripts\activate.bat`
3. Run `$ pyinstaller --clean -F ./main.py --name middleware.radius --version-file file_version_info.txt`
