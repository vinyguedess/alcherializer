
citest:
	make test
	coverage xml

test:
	coverage run tests/suite.py
	coverage html
	coverage report
