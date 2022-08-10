APP_PORT := 6969
DOCKER_TAG := latest
DOCKER_IMAGE := amazon


.PHONY: run_app
run_app:
	python3 -m uvicorn app:app --host='0.0.0.0' --port=$(APP_PORT)

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: download_weights
download_weights:
	dvc pull -R weights
	ls weights

.PHONY: lint
lint:
	flake8 src/

.PHONY: run_unit_tests
run_unit_tests:
	PYTHONPATH=. pytest tests/unit/

.PHONY: run_integration_tests
run_integration_tests:
	PYTHONPATH=. pytest -s tests/integration/

.PHONY: run_all_tests
run_all_tests:
	make run_unit_tests
	make run_integration_tests

.PHONY: generate_coverage_report
generate_coverage_report:
	PYTHONPATH=. pytest --cov=src --cov-report html  tests/


.PHONY: build
build:
	docker build -f Dockerfile . -t $(DOCKER_IMAGE):$(DOCKER_TAG)


.PHONY: install_c_libs
install_c_libs:
	apt-get update && apt-get install -y --no-install-recommends gcc ffmpeg libsm6 libxext6
