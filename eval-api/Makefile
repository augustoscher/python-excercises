.PHONY: all
all: setup lint coverage-report

.PHONY: setup
setup:
	@poetry env use 3.11.1
	@poetry install

.PHONY: run-api
run-api:
	@poetry run uvicorn api.main:app --reload

.PHONY: isort
isort: ## Check import sort order.
	@poetry run isort --profile black ./ --check-only

.PHONY: isort-apply
isort-apply: ## Sort import order.
	@poetry run isort --profile black ./

.PHONY: format
format: isort-apply
	@echo $(PROJECT_PATH)
	@poetry run black src/$(PROJECT_PATH) src/$(BLACK_OPTIONS)

.PHONY: lint
lint: BLACK_OPTIONS := --check
lint: isort
	@poetry run ruff check src/$(PROJECT_PATH) src/$(RUFF_OPTIONS)

.PHONY: test
test:
	@poetry run pytest --cov

.PHONY: coverage-report
coverage-report:
	@poetry run pytest --cov --cov-report=html
