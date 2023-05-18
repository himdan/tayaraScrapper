help:
	@echo ""
	@echo "-- Help Menu"
scrapper_build:
	docker build ./scrapper -t python-cli

scrapper_start:
	docker-compose exec -it scarpper bash -c "celery -A tasks worker -B"
scrapper_force_start:
	docker-compose exec -it scarpper bash -c "python main.py"
webapp_build:
	docker build ./webApp -t python-web