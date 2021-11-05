
citest:
	make test
	coverage xml

clear:
	rm -rf build coverage dist onany.egg-info .coverage

deploy:
	python setup.py sdist bdist_wheel
	twine upload dist/*

doc:
	rm -rf README.rst
	m2r README.md

lint:
	black alcherializer tests
	isort alcherializer tests

test:
	python -m pytest -p no:warnings --cov=alcherializer -v
	coverage html
