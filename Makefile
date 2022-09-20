down:
	docker compose down --volumes --remove-orphans

logs:
	docker compose logs -f
	
migrate:
	docker exec -it app bash -c "python src/manage.py migrate --settings=setup.settings.prod"

run:
	docker compose down
	docker compose up -d
