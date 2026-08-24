DOCKER := docker compose up

all: run

telegram:
	$(DOCKER) job-bot

web:
	$(DOCKER) web

run:
	$(DOCKER)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} +

.PHONY: clean all web telegram