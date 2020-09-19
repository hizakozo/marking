.PHONY: setup start

setup:
	pip install selenium
	pip install python-dotenv

run:
	python main.py