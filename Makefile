.PHONY: setup start

setup:
	pip install selenium
	pip install python-dotenv

start:
	python main.py