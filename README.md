TODO APP

## Readme

There is only server part of TODO application. This project is written in Python3 + Flask-restplus + Peewee ORM.

## Features:

1. Show a list of tasks
2. Show a single task
3. Change a single task
4. Delete a single task
5. Some unit-tests for testing CRUD operations

## Installation and Running

To install you may clone this repo to your local machine in the project directory with command 
`git clone https://github.com/agk606/TODOapp`.

## Dependencies

All dependencies are contained in requirements.txt. The following command will install the packages:
`$ pip install -r requirements.txt`

## Running

To launch the app you need to go to the project directory in the command line and run the server with command
`$ flask run`. Type http://127.0.0.1:5000/ in your browser and you'll see an interactive HTML interface for 
Swagger UI where you can examine operations with endpoints.