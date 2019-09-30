build_core:
	docker-compose build core

start_core:
	docker-compose up core

stop_core:
	docker-compose stop core

run_tests:
	docker-compose up  -d --build ubuntu
	docker-compose up --build tests
	docker-compose stop ubuntu
