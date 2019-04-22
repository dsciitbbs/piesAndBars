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
	
def test_transform(client):
	rv=client.post("/subject",data=dict(),follow_redirects=True)
	assert rv.status_code==400
	rv=client.post("/subject",data=dict(names='CS3L003'),follow_redirects=True)
	assert b"<!-- Required meta tags -->" in rv.data
	rv=client.get("/subject")
	assert b"<!-- Required meta tags -->" in rv.data
	rv=client.get("/subject?sub=CS3L003")
	assert b"<!-- Required meta tags -->" in rv.data