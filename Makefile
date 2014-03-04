start:
	venv/bin/python run.py

install:
	virtualenv venv
	venv/bin/pip install flask requests

uninstall:
	rm -fr venv
	rm -fr *.pyc app/*.pyc
