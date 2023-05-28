.PHONY: all lint clean

all: lint

venv: requirements.txt
	python3 -m venv venv
	. venv/bin/activate && pip3 install -r requirements.txt

lint: venv
	. venv/bin/activate && flake8 --config=.flake8 .

isort:
	isort .

clean:
	rm -rf venv
	rm -rf cache || true
	find -iname "*.pyc" -delete
	find -type d -name __pycache__ -delete