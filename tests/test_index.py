import os
import tempfile
import sys
sys.path.insert(0, 'E:\\piesAndBars')
import pytest
import application


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
	
def test_index(client):
	rv=client.post("/",data=dict(),follow_redirects=True)
	assert b"All fields are necessary" in rv.data
	rv=client.post("/",data=dict(year=14,branch='EC',format='SGPA'),follow_redirects=True)
	assert rv.status_code==200
	rv=client.post("/",data=dict(year=14,branch='ALL',format='C'),follow_redirects=True)
	assert rv.status_code==200
	rv=client.post("/",data=dict(year=14,branch='ALL',format='S'),follow_redirects=True)
	assert rv.status_code==200
	rv=client.get("/")
	assert b'Quote' and b'See Results' in rv.data