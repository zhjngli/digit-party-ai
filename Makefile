.PHONY: clean install test lint format

clean:
	rm -r build/ dist/ **/*.egg-info/ .mypy_cache/ && find . -name __pycache__ -type d -exec rm -r {} \;

install:
	pipenv install

test:
	make lint && echo "You haven't set up tests yet!"

lint:
	make type-check && make format && pipenv run flake8 src

format:
	pipenv run black src && pipenv run isort src --profile black

type-check:
	pipenv run mypy src
