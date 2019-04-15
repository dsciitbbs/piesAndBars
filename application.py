from flask import Flask, flash, redirect, render_template, request, session, url_for, send_file
from flask_session import Session
from tempfile import mkdtemp
from bokeh.embed import components
from bokeh.plotting import figure, output_file, save
from graphIt import get_CGPA
from SGPA import get_SGPA
from subject import get_subject
import numpy as np

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
Session(app)


@app.route("/")
def index():
	"""TODO-Change to a meaningful index page,preferably one with forms so that user can easily go to a graph"""
	return apology("Sorry")

@app.route("/cgpa/branch",methods=["GET"])
def cgpa_branchwise():
	"""TODO: Implement error checking, display suitable messages if:
	a)Some argument is missing in the get request
	b)  Invalid year/branch combo. Only 14,16,17 allowed as year and CS,EC,EE,MM,CE,ME as branch; EC not allowed for 14 and like so"""
	year=request.args.get('year')
	branch=request.args.get('branch')
	val=get_CGPA(year)
	scripts=[]
	divs=[]
	k=0
	highs=[]
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
	flash (' '.join(highs))
	return render_template("cgpa.html", values=values)

@app.route("/cgpa",methods=["GET"])
def cgpa_dist():
	"""TODO: Implement error checking, display suitable messages if:
	a)Some argument is missing in the get request
	b)Invalid year. Only 14,16,17 allowed as year."""
	year=request.args.get('year')
	val = get_CGPA(year)
	scripts = []
	divs = []
	i = 0
	for value in val:
		if i == len(val)-3:
			break
		p = figure(plot_width=400, plot_height=400, sizing_mode='scale_width')
		#p.y_range.end=60
		p.xaxis.axis_label='Semester '+str(int(i+1))
		l=[i for i in range(0,len(value))]
		hist, edges = np.histogram(value, density=True, bins=10, weights=l)
		hist=[int(i*100) for i in hist]
		p.quad(top=hist, bottom=0,
			   left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
		script, div = components(p)
		scripts.append(script)
		divs.append(div)
		i=i+1
	values = list(zip(scripts, divs))
	flash (' '.join(val[len(val)-3]))
	return render_template("cgpa.html", values=values)

@app.route("/sgpa",methods=["GET"])
def sgpa_dist():
	"""TODO: Implement error checking, display suitable messages if:
	a)Some argument is missing in the get request
	b)  Invalid year. Only 14,15,17 allowed as year"""
	year=request.args.get('year')
	val = get_SGPA(year)
	scripts = []
	divs = []
	i = 0
	for value in val:
		if i == len(val)-3:
			break
		p = figure(plot_width=400, plot_height=400, sizing_mode='scale_width')
		#p.y_range.end=60
		p.xaxis.axis_label='Semester '+str(int(i+1))
		l=[i for i in range(0,len(value))]
		hist, edges = np.histogram(value, density=True, bins=10, weights=l)
		hist=[int(i*100) for i in hist]
		p.quad(top=hist, bottom=0,
			   left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
		script, div = components(p)
		scripts.append(script)
		divs.append(div)
		i=i+1
	values = list(zip(scripts, divs))
	flash (' '.join(val[len(val)-3]))
	return render_template("sgpa.html", values=values)

@app.route("/sgpa/branch",methods=["GET"])
def sgpa_branchwise():
	"""TODO: Implement error checking, display suitable messages if:
	a)Some argument is missing in the get request
	b)  Invalid year/branch combo. Only 14,16,17 allowed as year and CS,EC,EE,MM,CE,ME as branch; EC not allowed for 14 and like so"""
	year=request.args.get('year')
	branch=request.args.get('branch')
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
	flash (' '.join(highs))
	return render_template("sgpa.html", values=values)

@app.route("/subject",methods=["GET"])
def subject():
	"""TODO: Implement error checking, display suitable messages if:
	a)Some argument is missing in the get request
	b)Invalid subcode"""
	sub=request.args.get('sub')
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