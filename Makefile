
citest:
	make test
	coverage xml

doc:
	rm -rf README.rst
	m2r README.md

test:
	coverage run tests/suite.py
	coverage html
	coverage report
