# piesAndBars
[![Build Status](https://travis-ci.com/dsciitbbs/piesAndBars.svg?branch=master)](https://travis-ci.com/dsciitbbs/piesAndBars) [![codecov](https://codecov.io/gh/dsciitbbs/piesAndBars/branch/master/graph/badge.svg)](https://codecov.io/gh/dsciitbbs/piesAndBars/commits)  

An application to graphically represent the grade distribution in IIT Bhubaneswar over the past years.  

**Usage:**
- Clone the project
- Run *pip3 install -r requirements.txt*
- Use command *export FLASK_APP=application.py* (on Mac/Linux) or *set FLASK_APP=application.py* to set the environment variable
- Use *flask run*  (Windows/Linux) or *python -m flask run* (Mac)

|URL|Action|
|-------|-------|  
localhost:5000 |Form interface for the various result distributions available  
localhost:5000/cgpa|Displays the CGPA distribution,batchwise. Required parameter: **year**  
localhost:5000/sgpa |Displays the SGPA distribution,batchwise. Required parameter: **year**  
localhost:5000/cgpa/branch|Displays the CGPA distribution,batchwise. Required parameters: **year**, **branch**
localhost:5000/sgpa/branch|Displays the SGPA distribution,batchwise. Required parameter: **year**, **branch**
localhost:5000/subject| Displays the grade distribution, subjectwise. Required parameter: **sub**

More features will be added soon.
<h2>Examples</h2>

URL|Interface
|----------|----------|
localhost/cgpa?year=16 |<img src="https://user-images.githubusercontent.com/25523604/56133124-531c8300-5fa9-11e9-82c0-3d4279363629.png"></img>
localhost/cgpa/branch?year=16&branch=CS |<img src="https://user-images.githubusercontent.com/25523604/56133646-87447380-5faa-11e9-802f-8aaed827a12c.png"></img>
localhost/sgpa?year=16 |<img src="https://user-images.githubusercontent.com/25523604/56133913-1c476c80-5fab-11e9-9669-9450dc75bd7e.png"></img>
 localhost/sgpa/branch?year=16&branch=CS  |<img src="https://user-images.githubusercontent.com/25523604/56133775-e7d3b080-5faa-11e9-98da-a80104fc1ca7.png"></img>
localhost/subject?sub=CE1P001 |<img src="https://user-images.githubusercontent.com/25523604/56133997-4862ed80-5fab-11e9-94c5-5e36623fa6d8.png"></img>

For contributing, please take a look at <a href="https://github.com/dsciitbbs/piesAndBars/blob/master/contributing.md">contributing.md</a>.
