setup:
	virtualenv venv && venv/bin/pip install -r requirements.txt

run_github:
	venv/bin/python github.py 0.0.0.0:8001
