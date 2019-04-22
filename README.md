# piesAndBars
[![Build Status](https://travis-ci.com/dsciitbbs/piesAndBars.svg?branch=master)](https://travis-ci.com/dsciitbbs/piesAndBars) [![codecov](https://codecov.io/gh/dsciitbbs/piesAndBars/branch/master/graph/badge.svg)](https://codecov.io/gh/dsciitbbs/piesAndBars/commits)  

An application to graphically represent the grade distribution in IIT Bhubaneswar over the past years.  
To use, first clone the project then run **pip3 install -r requirements.txt**  
Use command **export FLASK_APP=application.py** to set the environment variable and then use **flask run**  

**URLs:**  

*localhost:5000/*: - Form interface for the various result distributions available  

*localhost:5000/cgpa* - Displays the CGPA distribution,batchwise. Required parameter: **year**  
Example: localhost/cgpa?year=16  
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133124-531c8300-5fa9-11e9-82c0-3d4279363629.png"></img>
</p>

*localhost:5000/cgpa/branch* - Displays the CGPA distribution,batchwise. Required parameter: **year**, **branch**  
Example: localhost/cgpa/branch?year=16&branch=CS  
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133646-87447380-5faa-11e9-802f-8aaed827a12c.png"></img>
</p>

*localhost:5000/sgpa* - Displays the SGPA distribution,batchwise. Required parameter: **year**  
Example: localhost/sgpa?year=16  
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133913-1c476c80-5fab-11e9-9669-9450dc75bd7e.png"></img>
</p>

*localhost:5000/sgpa/branch* - Displays the SGPA distribution,batchwise. Required parameter: **year**, **branch**  
Example: localhost/sgpa/branch?year=16&branch=CS  
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133775-e7d3b080-5faa-11e9-98da-a80104fc1ca7.png"></img>
</p>

*localhost:5000/subject* - Displays the grade distribution, subjectwise. Required parameter: **sub**  
Example: localhost/subject?sub=CE1P001  
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133997-4862ed80-5fab-11e9-94c5-5e36623fa6d8.png"></img>
</p>

For contributing, please take a look at <a href="https://github.com/dsciitbbs/piesAndBars/blob/master/contributing.md">contributing.md</a>.
