.PHONY: install
install: # Install the dependencies from the lock file
	poetry install -v

.PHONY: test
test: ## Launch the tests
	poetry run pytest -vv tests
