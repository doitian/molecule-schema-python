test:
	python -m unittest discover

requirements.txt: setup.py
	pip-compile --strip-extras

dev-requirements.txt: dev-requirements.in requirements.txt
	pip-compile --strip-extras dev-requirements.in

publish: setup requirements.txt
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine --version || pip install twine
	twine upload -u "$${PYPI_USERNAME}" -p "$${PYPI_PASSWORD}" dist/*

clean:
	rm -rf dist molecule_schema.egg-info

setup:
	pip install pip-tools wheel twine
	pip install -r requirements.txt

.PHONY: test publish clean setup
