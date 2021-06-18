
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

test:
	coverage run tests/suite.py
	coverage html
	coverage report
