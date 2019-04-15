# piesAndBars
An application to graphically represent the grade distribution in IIT Bhubaneswar over the past years.</br>
To use, first clone the project then run **pip3 install -r requirements.txt**</br>
Use command **export FLASK_APP=application.py** to set the environment variable and then use **flask run**</br>

**URLs:**</br>
*localhost:5000/cgpa* - Displays the CGPA distribution,batchwise. Required parameter: **year** </br>
Example: localhost/cgpa?year=16</br>
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133124-531c8300-5fa9-11e9-82c0-3d4279363629.png"></img>
</p>

*localhost:5000/cgpa/branch* - Displays the CGPA distribution,batchwise. Required parameter: **year**, **branch** </br>
Example: localhost/cgpa/branch?year=16&branch=CS</br>
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133646-87447380-5faa-11e9-802f-8aaed827a12c.png"></img>
</p>

*localhost:5000/sgpa* - Displays the SGPA distribution,batchwise. Required parameter: **year** </br>
Example: localhost/sgpa?year=16</br>
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133913-1c476c80-5fab-11e9-9669-9450dc75bd7e.png"></img>
</p>

*localhost:5000/sgpa/branch* - Displays the SGPA distribution,batchwise. Required parameter: **year**, **branch** </br>
Example: localhost/sgpa/branch?year=16&branch=CS</br>
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133775-e7d3b080-5faa-11e9-98da-a80104fc1ca7.png"></img>
</p>

*localhost:5000/subject* - Displays the grade distribution, subjectwise. Required parameter: **sub** </br>
Example: localhost/subject?sub=CE1P001</br>
<p align="center">
<img src="https://user-images.githubusercontent.com/25523604/56133997-4862ed80-5fab-11e9-94c5-5e36623fa6d8.png"></img>
</p>

For contributing, please take a look at <a href="https://github.com/dsciitbbs/piesAndBars/blob/master/contributing.md">contributing.md</a>.
