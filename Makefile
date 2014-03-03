start:
	venv/bin/python run.py

install:
    pip install virtualenv
	virtualenv venv
	venv/bin/pip install flask requests

uninstall:
	rm -fr venv
