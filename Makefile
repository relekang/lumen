setup: venv
	venv/bin/pip install -r requirements.txt

run_github:
	venv/bin/python github.py 0.0.0.0:8001

venv:
	virtualenv venv

.PHONY: setup run_github
