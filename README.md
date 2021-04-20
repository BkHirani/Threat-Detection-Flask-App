# Threat Detection Application

Welcome to Threat Detection App! Here we're uploading scanned images from a scanner which we usually find at the airport, companies, colleges, etc. We'll need basic 

## Steps to start app

Below are the steps to start the Flask server. I'll start at [localhost:6500](http://localhost:6500/)

```bash
cd solution/backend
python main.py
```

## Tools/Libraries used

1. Python 3.7
2. SqlAlchemy (SQL db in this scenario)
3. OpenCV (For plotting rectangle on image)

## Solution Approach
   
Here I've used the SqlAlchemy database to make the solution easily deployable without any external requirements. I'm using the XML library to parse the tree and then I'm using OpenCV to draw a rectangle over given coordinates. After that, I'm storing information in the database. In the show logs method, I'm taking user input to display logs in the grid. Apart from CSV, I'm providing different options to download the data like Excel, PDF and Clipboard.

## Solution Snaps

- Welcome page

![Welcome Page](https://github.com/BkHirani/Threat-Detection-Flask-App/blob/master/solution%20snaps/Welcome%20Page.png?raw=true)

- Upload Files

![Upload Files](https://github.com/BkHirani/Threat-Detection-Flask-App/blob/master/solution%20snaps/Upload%20files.png?raw=true)

- Upload Confirmation Page

![Upload Confirmation page](https://github.com/BkHirani/Threat-Detection-Flask-App/blob/master/solution%20snaps/Upload%20file%20success.png?raw=true)


- Show Logs

![Show Logs](https://raw.githubusercontent.com/BkHirani/Threat-Detection-Flask-App/master/solution%20snaps/Show%20Logs.png)


## Scope of improvements

In the plan of productionalize the solution, We can use NoSQL database as It would be easy to change the schema if required. Due to lack of time I wasn't able to create separate services. One can create REST API server for backend and frontend apps. 
