from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField ,SubmitField
from wtforms.validators import DataRequired

class FirstForm(FlaskForm):
    year = SelectField('Year', choices = [('14', '14'),('17', '17'),('16', '16')], validators=[DataRequired()])
    branch = SelectField('Branch', choices = [('ALL', 'All branches'),('EC', 'Electronics and Communication Enineering'), ('CS', 'Computer Science and Engineering'), ('EE','Electrical Engineering'), ('ME','Mechanical Engineering'), ('CE','Civil Engineering'), ('MM','Material and Minerals Engineering')], validators=[DataRequired()])
    format = RadioField('Format', choices = [('S','SGPA'),('C','CGPA')], validators=[DataRequired()])
    submit = SubmitField('See Results')