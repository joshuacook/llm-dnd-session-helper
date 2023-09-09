debug:
	pytest -s

lint:
	black .
	mypy .
	ruff check .
test:
	pytest --cov=lldm --cov-report term-missing