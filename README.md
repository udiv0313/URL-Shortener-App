# URL-Shortener-App
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
It is URL Shortener web app which have GET, POST, DElETE functionality for the generated url. It takes any long url as a parameter and make it short with the generated key, So you can paste it and easily share it with anyone.
	
## Technologies
Project is created with:
* Python3
* SQLAlchemy
* FastAPI
	
## Setup
To run this project :

* Make a directory name as whatever you want.
```
$ mkdir URl_shortener
$ cd /URL_shortener
```
* Make another directory inside the URL_shortener where all your main files stored.
```
URL_shortener$ mkdir shortener_app
URL_shortener/shortener_app$
```

* Make Virtual Environment in root folder so you download and can acess all your dependencies 
```
URL_shortener$ python -m venv myenv
```
* Activate Virtual Environment for powershell, for other you can change by tab key
```
URL_shortener$  .\myenv\Scripts\Activate.ps1
```
# Installation
* for dependencies installation check the requirement.txt file.

# Run
* To start the server run
```
URL_shortener/shortener_app$ uvicorn main:app --reload
```




