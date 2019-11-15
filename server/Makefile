.PHONY: virtualenv
virtualenv:
	python3 -m venv venv && . venv/bin/activate && python3 -m pip install -r requirements.txt

dev:
	. venv/bin/activate && uvicorn reportmaster.app:app --reload

