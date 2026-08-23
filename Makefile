all: clean

clean:
	sudo chown -R denys:denys ~/Documentos/projectos/LINKEDIN_BOT/__pycache__
	sudo chown -R denys:denys ~/Documentos/projectos/LINKEDIN_BOT/services/__pycache__
	sudo chown -R denys:denys ~/Documentos/projectos/LINKEDIN_BOT/core/pipeline/__pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} +

.PHONY: clean all