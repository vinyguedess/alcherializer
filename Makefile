
citest:
	make test
	coverage xml

clear:
	rm -rf build coverage dist onany.egg-info .coverage

deploy:
	python setup.py sdist bdist_wheel
	twine upload dist/*

down:
	docker-compose stop
	docker-compose down

lint:
	black alcherializer tests
	isort alcherializer tests

test:
	python -m pytest -p no:warnings --cov=alcherializer -vv
	coverage html

up:
	docker-compose up -d
	docker-compose exec app bash
