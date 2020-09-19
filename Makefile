.PHONY: setup run

setup:
	pip install selenium
	pip install python-dotenv

run:
	python main.py