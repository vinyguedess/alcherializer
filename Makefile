
citest:
	make test
	coverage xml

clear:
	rm -rf build coverage dist onany.egg-info .coverage

deploy:
	python setup.py sdist bdist_wheel
	twine upload dist/*

lint:
	black alcherializer tests
	isort alcherializer tests

test:
	python -m pytest -p no:warnings --cov=alcherializer -vv
	coverage html
