from flask import Flask, flash, redirect, render_template, request, session, url_for, send_file
from flask_session import Session
from tempfile import mkdtemp
from bokeh.embed import components
from bokeh.plotting import figure, output_file, save
from graphIt import get_CGPA
from SGPA import get_SGPA
from subject import get_subject
import numpy as np
from forms import FirstForm

app = Flask(__name__)


def apology(message, code=400):
	"""Render message as an apology to user."""
	def escape(s):
		"""
		Escape special characters.

		https://github.com/jacebrowning/memegen#special-characters
		"""
		for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
						 ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
			s = s.replace(old, new)
		return s
	return render_template("apology.html", top=code, bottom=escape(message)), code

def getSGPA_allBranch(year = 2016):
	val = get_SGPA(year)
	scripts = []
	divs = []
	k = 0
	for value in val:
		if k == len(val)-3:
			break
		p = figure(plot_width=400, plot_height=400, sizing_mode='scale_width')
		#p.y_range.end=60
		p.xaxis.axis_label='Semester '+str(int(k+1))
		temp_SGPA=[]
		temp_roll=[]
		temp_name=[]
		for idx,i in enumerate(val[len(val)-2]):
			temp_SGPA.append(value[idx])
			temp_roll.append(val[len(val)-2][idx])
			temp_name.append(val[len(val)-1][idx])
		if not temp_SGPA:
			values = []
			return values, val
		m=max(temp_SGPA)
		t=[i for i, j in enumerate(temp_SGPA) if j == m]
		l=[i for i in range(0,len(temp_SGPA))]
		hist, edges = np.histogram(temp_SGPA, density=True, bins=10, weights=l)
		hist=[int(i*100) for i in hist]
		p.quad(top=hist, bottom=0,
			   left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
		script, div = components(p)
		scripts.append(script)
		divs.append(div)
		k=k+1
	values = list(zip(scripts, divs))
	return values, val

def getCGPA_allBranch(year=2016):
	val = get_CGPA(year)
	scripts = []
	divs = []
	k = 0
	for value in val:
		if k == len(val)-3:
			break
		p = figure(plot_width=400, plot_height=400, sizing_mode='scale_width')
		#p.y_range.end=60
		p.xaxis.axis_label='Semester '+str(int(k+1))
		temp_CGPA=[]
		temp_roll=[]
		temp_name=[]
		for idx,i in enumerate(val[len(val)-2]):
			temp_CGPA.append(value[idx])
			temp_roll.append(val[len(val)-2][idx])
			temp_name.append(val[len(val)-1][idx])
		if not temp_CGPA:
			values = []
			return values, val
		m=max(temp_CGPA)
		t=[i for i, j in enumerate(temp_CGPA) if j == m]
		l=[i for i in range(0,len(temp_CGPA))]
		hist, edges = np.histogram(temp_CGPA, density=True, bins=10, weights=l)
		hist=[int(i*100) for i in hist]
		p.quad(top=hist, bottom=0,
			   left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
		script, div = components(p)
		scripts.append(script)
		divs.append(div)
		k=k+1
	values = list(zip(scripts, divs))
	return values, val
	
def getCGPA_branchwiseValues(year=2016, branch = "EC"):
	val=get_CGPA(year)
	scripts=[]
	divs=[]
	k=0
	highs=[]
	print(len(val))
	for value in val:
		if k==len(val)-3:
			break
		p=figure(plot_width=400,plot_height=400,sizing_mode='scale_width')
		p.xaxis.axis_label='Semester '+str(k+1)
		temp_CGPA=[]
		temp_roll=[]
		temp_name=[]
		for idx,i in enumerate(val[len(val)-2]):
			if i[2:4]==branch:
				temp_CGPA.append(value[idx])
				temp_roll.append(val[len(val)-2][idx])
				temp_name.append(val[len(val)-1][idx])
		if not temp_CGPA:
			values = []
			highs=[]
			return values, highs
		m=max(temp_CGPA)
		t=[i for i, j in enumerate(temp_CGPA) if j == m]
		for v in t:
			highs.append("Semester "+str(k+1)+": "+temp_name[v]+","+temp_roll[v]+","+str(temp_CGPA[v]))
		l=[i for i in range(0,len(temp_CGPA))]
		hist, edges = np.histogram(temp_CGPA, density=True, bins=10, weights=l)
		hist=[int(i*100) for i in hist]
		p.quad(top=hist, bottom=0,
			   left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
		script, div = components(p)
		scripts.append(script)
		divs.append(div)
		k=k+1
	values = list(zip(scripts, divs))
	return values, highs

def getSGPA_branchwiseValues(year=2016, branch="EC"):
	val=get_SGPA(year)
	scripts=[]
	divs=[]
	k=0
	highs=[]
	for value in val:
		if k==len(val)-3:
			break
		p=figure(plot_width=400,plot_height=400,sizing_mode='scale_width')
		p.xaxis.axis_label='Semester '+str(k+1)
		temp_SGPA=[]
		temp_roll=[]
		temp_name=[]
		for idx,i in enumerate(val[len(val)-2]):
			if i[2:4]==branch:
				temp_SGPA.append(value[idx])
				temp_roll.append(val[len(val)-2][idx])
				temp_name.append(val[len(val)-1][idx])
		m=max(temp_SGPA)
		t=[i for i, j in enumerate(temp_SGPA) if j == m]
		for v in t:
			highs.append("Semester "+str(k+1)+": "+temp_name[v]+","+temp_roll[v]+","+str(temp_SGPA[v]))
		l=[i for i in range(0,len(temp_SGPA))]
		hist, edges = np.histogram(temp_SGPA, density=True, bins=10, weights=l)
		hist=[int(i*100) for i in hist]
		p.quad(top=hist, bottom=0,
			   left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
		script, div = components(p)
		scripts.append(script)
		divs.append(div)
		k=k+1
	values = list(zip(scripts, divs))
	return values, highs


# Ensure responses aren't cached
@app.after_request
def after_request(response):
	response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	response.headers["Expires"] = 0
	response.headers["Pragma"] = "no-cache"
	return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'you-will-never-guess'
Session(app)


@app.route("/", methods=['GET', 'POST'])
def index():
	form = FirstForm()

	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are necessary')
			return render_template('firstform.html', form=form)
		else:
			yearentry = form.year.data
			branchentry = form.branch.data
			formatentry = form.branch.data
			if yearentry == "14" and branchentry =="EC":
				print("ECE 14");
				flash('ECE branch does not exist in year 14')
				return render_template('firstform.html',form = form)
			elif branchentry == "ALL":
				if formatentry == "C":
					values,val = getCGPA_allBranch(yearentry)
					flash (' '.join(val[len(val)-3]))
					return render_template("cgpa.html", values=values)
				else:
					values,val = getSGPA_allBranch(yearentry)
					flash (' '.join(val[len(val)-3]))
					return render_template("sgpa.html",values=values)
			else:
				if formatentry == "S":
					values, highs = getSGPA_branchwiseValues(yearentry,branchentry)
					if not values or not highs:
						flash('Could not find any entry that met your specification')
						return render_template("sgpa.html", values=values)
					flash (' '.join(highs))
					return render_template("sgpa.html", values=values)
				else:
					values, highs = getCGPA_branchwiseValues(yearentry, branchentry)
					if not values or not highs:
						flash('Could not find any entry that met your specification')
						return render_template("cgpa.html", values=values)
					flash (' '.join(highs))
					return render_template("cgpa.html", values=values)
	elif request.method == 'GET':
		return render_template('firstform.html', form = form)

@app.route("/cgpa/branch",methods=["GET"])
def cgpa_branchwise(year=16, branch="EC"):
	values, highs = getCGPA_branchwiseValues(year, branch)
	flash (' '.join(highs))
	return render_template("cgpa.html", values=values)

@app.route("/cgpa",methods=["GET"])
def cgpa_dist():
	values = getCGPA_allBranch(year =16)
	flash (' '.join(val[len(val)-3]))
	return render_template("cgpa.html", values=values)

@app.route("/sgpa",methods=["GET"])
def sgpa_dist():
	values,val = getSGPA_allBranch(year = 2016)
	flash (' '.join(val[len(val)-3]))
	return render_template("sgpa.html", values=values)

@app.route("/sgpa/branch",methods=["GET"])
def sgpa_branchwise(year = 16, branch="EC"):
	values,highs = getSGPA_branchwiseValues(year,branch)
	flash (' '.join(highs))
	return render_template("sgpa.html", values=values)

@app.route("/subject",methods=["GET"])
def subject():
	"""TODO: Implement error checking, display suitable messages if:
	a)Some argument is missing in the get request
	b)Invalid subcode"""
	sub="ID1T001"
	scripts=[]
	divs=[]
	x=get_subject(sub)
	for key,value in x.items():
		p=figure(plot_width=400,plot_height=400,sizing_mode='scale_width')
		p.xaxis.axis_label='Batch '+str(key)
		l=[i for i in range(0,len(value))]
		#p.line(l,value,line_width=2)
		hist, edges = np.histogram(value, density=True, bins=10, weights=l)
		p.quad(top=hist, bottom=0,
			   left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
		script, div = components(p)
		scripts.append(script)
		divs.append(div)
	values = list(zip(scripts, divs))
	return render_template('subject.html',values=values)