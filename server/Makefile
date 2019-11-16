.PHONY: virtualenv
virtualenv:
	python3 -m venv venv && . venv/bin/activate && python3 -m pip install -r requirements.txt

dev:
	. venv/bin/activate && uvicorn reportmaster.app:app --reload

dbinit:
	mkdir -p db/mysql/data && mkdir db/mysql/init && cp schema.sql db/mysql/init/ && docker-compose up -d

dbdestroy:
	docker-compose down && rm -r db/
