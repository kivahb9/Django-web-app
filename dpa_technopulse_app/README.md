# Technopulse
---
This is an hackathon platform built to attract data science enthusiast by encouraging them to participate and take up challenges.
---
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Anaconda
* Visual Studio Code


**Note**: 
*Follow below instructions to set up bitbucket account and clone the project structure created on bit bucket to your local machine* 
*If you are cloning the complete repository (all programms) or partially created project, then skip below steps and refer **How to directly run partilly created or complete Python-django of other machine or cloned from Bitbucket.***

1. Create a bitbucket repository with suitable project name. *Contact IT Team for the same.*

2. Clone the newly created repo to your workspace. Please create a 'workspace' named directory on the 'D drive' for windows machine and for linux clone in under 'work' directory. *Install git bash for cloning.*

3. How to clone: Open git bash and write the following command.    
		
		$ git clone pathtoyourrepo		
		# Enter your bitbucket password if prompted
				
4. Once cloned, please open the project folder on your VS Code IDE.

5. Open a new terminal on your VS Code IDE. You can click on Terminal widget on navigation bar and new terminal
(shorthand Ctrl+Shift+~).

6. Open explorer and select for a python interpreter (shorthand Ctrl+Shift+P) click on Select Interpreter.

7. Select and activate base conda environment (shorthand Ctrl+Shift+~).

8. Create a new environment for your project using the following command

		$ conda create -n yourprojectenv Django
		# Type 'y' if conda prompts for installing extra packages.
		# We are installing Django since it is a Django based project.
	
9. Activate your newly created environment using following command 
	
		$ conda activate yourprojectenv
		# Here yourprojectenv is your environment name.
	
10. It is recommended to install **pylint** and **formater black** for your IDE. This helps you write your code efficiently.

11. Checkout from **master branch to develop branch.**

12. Add a new **.gitignore** file to ignore unnecessary files which should not be pushed from your local git to server. 

13. Install django in newly created virtual environment

	Install using `pip` or `conda ` (Prefer conda)...

	    $ conda install django

14. Create your Django project and required apps using following command  

		$ djangp-admin startproject project_name
		$ django-admin startapp app_name

15. After completion of project you can directly stage the chanages and push to bitbucket from local machine using VS code.
	** First select the components or modules you wish to push using + sing. 
	** Then click on ✓ sign to commit.

16. It is recommended to create and work fetaure branch (master>develop>fetaure).After completing work in fetaure branch, ask seniors to review and approve. Once approved Push it to develop branch. From develop branch after rigorous testing or fixing all bugs it will finally move to master branch which will be our production ready code.

**P.S**:*Always create .yaml file at the end of the day. This file helps to clone any other system python-django environment which includes all required modules to your workspace*
**Use following command to create .yaml file.**	

		$ conda env export > environment.yaml


## How to directly run partilly created or complete Python-django of other machine or cloned from Bitbucket. 	

1. Clone the project to your workspace.Please check for the **.yaml and .gitignore files.
2. Activate base environement and run following command to clone the environment to your machine.

		$ conda env create -f environment.yaml

3. In .gitignore file add necessary apps,files like migrtaions, __init__.py and append ignore('*') or not  ignore(!*/) as per your need.
4. Change the **settings:Database** and do the miggrations using following commands to create tabales.

		$ python manage.py makemigrations
		$ python manage.py migrate

5. Finally run server to run the project using following commands

		$ python manage.py migrate`


## Deployment

Add additional notes about how to deploy this on a live system


## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 
Please note we have a code of conduct, please follow it in all your interactions with the project.


## Authors

* **Manager**: ShravanKumar Suvarna 
* **Developers**: Bhavik Prajapati
* **Analyst**: Sarita Maurya


## License

[DPA](https://www.decimalpointanalytics.com) © Copyright (c) 2019 Decimal Point Analytics, Pvt Ltd.
All rights reserved.