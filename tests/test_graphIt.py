import os
import tempfile
import sys
sys.path.insert(0, 'E:\\piesAndBars')
import pytest
import application
import subject

@pytest.fixture
def app():
	#db_fd, db_path = tempfile.mkstemp()
	app=application.app
	application.app.config['TESTING'] = True
	#client = application.app.test_client()
	yield app
	#os.close(db_fd)
	#os.unlink(flaskr.app.config['DATABASE'])

@pytest.fixture
def client(app):
	return app.test_client()


@pytest.fixture
def runner(app):
	return app.test_cli_runner()
	
def test_cgpa(client):
	rv=client.get("/cgpa")
	assert b"<!-- Required meta tags -->" in rv.data
	rv=client.get("/cgpa?year=14")
	assert b"<!-- Required meta tags -->" in rv.data
	rv=client.get("/cgpa?year=17")
	assert b"<!-- Required meta tags -->" in rv.data
	rv=client.get("/cgpa?year=16")
	assert b"<!-- Required meta tags -->" in rv.data
	rv=client.get("/cgpa/?year=15")
	assert len(rv.data)<5000
	
def test_cgpa_branchwise(client):
	rv=client.get("/cgpa/branch")
	assert b"<!-- Required meta tags -->" in rv.data
	rv=client.get("/cgpa/branch?year=16&branch=EC")
	assert b"<!-- Required meta tags -->" in rv.data
	rv=client.get("/cgpa/branch?year=16&branch=l")
	assert len(rv.data)<5000
	rv=client.get("/cgpa/branch?year=15&branch=CS")
	assert len(rv.data)<5000