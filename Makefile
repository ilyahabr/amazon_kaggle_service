APP_PORT := 6969
DOCKER_TAG := latest
DOCKER_IMAGE := amazon


.PHONY: run_app
run_app:
	PYTHONPATH=../ python3 -m uvicorn app:app --host='0.0.0.0' --port=$(APP_PORT)

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: lint
lint:
	flake8 src/
