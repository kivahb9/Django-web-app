# Technopulse - Online hackathon

This is an hackathon platform built to attract data science enthusiast by encouraging them to participate and take up challenges.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Programming Language
* Python
* HTML
* Javascript  

## Version Used

* [Python](https://repo.anaconda.com/archive/Anaconda3-2019.07-MacOSX-x86_64.pkg) --3.7.3
* [HTML] --HTML5
* [Visual Studio Code](https://code.visualstudio.com/download) --1.37.1
* [MySQL](https://dev.mysql.com/downloads/file/?id=488054) --8.0.17.0

## Library Used
* Please refer requirements.txt or environment.yml file

## Prerequisites/Requirements

Running the Technopulse Portal requires Python 3.7 and an IDE (Integrated Development Environment) for development.

Running the Django web application requires the following tools:

* [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2019.07-MacOSX-x86_64.pkg) -- Download the 2019.07 Python 3.7.3 version   
* [Visual Studio Code](https://code.visualstudio.com/download) --Download the latest version. Project was buil using 1.37.1 version
* [MySql](https://dev.mysql.com/downloads/file/?id=488054) --Download the 8.0.17.0 version
* [Conda Environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) --Follow to create, export, import etc
* [Git](https://git-scm.com/) --Obviously 


## Project Description

* Problem Statement: An online coding competition portal which comprises various machine learning challenges.
* Process Followed: 
	1. Created multiple django applications using the command `python manage.py startapp appname`.
		1. user --this application manages user creation, authentication, profile etc.
		4. challenges --this application has all the business logic related to different challenges which will be only accessible to the users. 
	3. Created all the required models in **models.py** for all the applications.
	4. Create all the required business logic in **views.py** for all the applications.
	5. Registered all the models for django admin site with import-export functionalities in **admin.py** for all the applications.
	6. Create templates for the required logic in the **templates** folder of user and challenges applications.  

## Data Source
* MySql Database. We have created all the master tables internally

## Setup Development Environment

*Follow below instructions to set up GitHub account and clone the project structure created on your local machine* 

1. Get the Source Code
    
    *Clone the repo on your workspace. It is recommended to create `D:\work` named directory on the 'D' Drive for windows machine. `cd /work` for linux clone it under 'work' directory. Install git bash for cloning.*

2. How to clone: Open git bash and write the following command. 

	`git clone https://bitbucket.org/decimal-point-analytics/dpa_technopulse_app.git`
	`#Enter your bitbucket password if prompt`

3. Once cloned, open the project folder on your VS Code IDE.
4. Open a new terminal on your VS Code IDE. You can click on Terminal widget on navigation bar and then click on new terminal (shorthand Ctrl+Shift+~).
5. Open explorer and select for a python interpreter (shorthand Ctrl+Shift+P) click on Select Interpreter.
6. Select and activate base conda environment (shorthand Ctrl+Shift+~).  
7. How to set-up development or testing conda environment. Please follow the below instructions. 

	1. Clone the existing environment using the environement.yml file. Open the directory where you have cloned this repo and use the below mentioned command.

		* Replicate the Virtual Environment
		`conda env create -f environment.yml` -- This will download the python and required library with appropriate versions. When conda asks you to proceed, type y: `Proceed ([y]/n)?`

	2. If you are unable to create an anaconda environment or environment using environment.yml or requirement.txt file, then create a new environment for your project using the following command.

		1. Anaconda Steps 		
			* Create new environment 
				`conda create -n technopulseenv django` --We are installing Django because this is a python Django based project. 
			* Install required packages 
				`conda install packagename=version=pythonversion` --eg.`conda install wheel=0.33.4=py37_0`	

		2. If you are not using anaconda python for specific reason, then use the below commands. 

			* Install virtual environemnt 
				`pip install virtualenv`
			* Create virtual environment
				`virtualenv timepulseenv`--timepulseenv is your environment name
			* Activate your environment
				`timepulseenv\Scripts\activate` --Windows
				`source timepulseenv/bin/activate` --MacOS/Linux
			* Install the required library
				`pip install -r requirements.txt`	

8. If you are unable to create an anaconda environment or pip environment using environment.yml or requirement.txt file, then create a new environment for your project using the above mentioned commands and download the libarary manually using `conda` or `pip` package manager.

9. Activate your newly created environment using following command 

	`conda activate technopulseenv` OR
	`technopulseenv\Scripts\activate` --Windows (Refer above for Linux)

10. Check the **settings.py** and make the necessary changes to suit your development machine. Below are a few key changes. Database connection configurations.  

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'technopulse',
        'USER': config['USER'],
        'PASSWORD': config['PASSWORD'],
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

11. Create a new **technopulse_config.json** file in the working directory and add the following sensitive information. Check with your IT manager for more information

	`{
        "SECRET_KEY": *Secret Key Here*, --Django secrete key
        "EMAIL_HOST_USER": *Email Address*,
        "EMAIL_HOST_PASSWORD": *Email Password*,
        "DATABASE_USER": *Database Username*,
        "DATABASE_PASSWORD": *Database Password*
	}`

11. Run Django development server and check if everything is working fine on VS Code Terminal.
	`python manage runserver`

10. It is recommended to install **pylint** and **formater black** for your IDE. This helps you write your code efficiently. If you are cloning the environment.yml or requirement.txt file, then it will come preloaded with the same.
11. Checkout from **master branch to develop branch.**. If you are working on a specific feature branch, then please checkout to that particular branch.

## Deployment

1. SSH

		$ ssh root@IP
		$ enter password:

2. Clone the project to work directory

		$ git clone "bit bucket project link"

3. Create new and activate virtual environment

		$ python3 -m venv name_venv
		Inside the folder where you created activate the same
 		$ source venv/bin/activate

4. Install all the dependencies using requirements.txt file

		$ pip install -r requirements.txt

5. Collect Static Files

		$ python manage.py collectstatic

6. Run Django Server and Test

		$ python manage.py runserver

7. Install Apached and Mod WSGI (Web Server Gateway Interface)

		$ sudo apt-get install apache2
		$ sudo apt-get install libapache2-mod-wsgi-py3

8. Set-up apache2
	* Create new file
			$ cd /etc/apache2/sites-available/
	* Add below
			Alias /static "static folder path"
			<Directory "static folder path">
				Require all granted
			</Directory>

			Alias "media folder path"
			<Directory "media folder path">
				Require all granted
			</Directory>

			<Directory "Project folder path">
				<Files wsgi.py>
				Require all granted
				</Files>
			</Directory>

			WSGIScriptAlias / "wsgi.py file path"
			WSGIDaemonProcess timesheet_app python-path="path"
			python-home="path"
			WSGIProcessGroup "project_name"

9. **Create config file and copy Sensitive Data in a config file**

10. Import sensitive information in Project Setting file

		import json
		with open('config file path') as config_file:
			config = json.load(config_file)

		SECRET_KEY = config['SECRET_KEY']

11. Finally restart apache2 using following command

		$ sudo service apache2 restart

12. If restarting server didn't host your site then check the logs using following command

		$ sudo tail /var/log/apache2/error.log

## Built With

* [Django](https://www.djangoproject.com/) --The web framework used to build webapps quickly.

## Authors

* **Developer: Bhavik Prajapati**
* **Analyst: Sarita Maurya**
* **Team Leader: Shravankumar Suvarna**
* **Reporting Manager: Rikesh Patel**
	
## License

[Decimal Point Analytics](https://www.decimalpointanalytics.com) © Copyright (c) 2019 Decimal Point Analytics, Inc.
All rights reserved.