.PHONY: help install test lint format clean docker-build docker-run docker-compose-up docker-compose-down

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install black isort flake8 mypy

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=app --cov-report=html

lint: ## Run linting
	flake8 app tests
	mypy app

format: ## Format code
	black app tests
	isort app tests

format-check: ## Check code formatting
	black --check app tests
	isort --check-only app tests

clean: ## Clean up cache and temporary files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf htmlcov/
	rm -rf .coverage

run: ## Run the application
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

run-prod: ## Run the application in production mode
	uvicorn main:app --host 0.0.0.0 --port 8000

docker-build: ## Build Docker image
	docker build -t fastapi-template .

docker-run: ## Run Docker container
	docker run -p 8000:8000 --env-file .env fastapi-template

docker-compose-up: ## Start services with Docker Compose
	docker-compose up -d

docker-compose-down: ## Stop services with Docker Compose
	docker-compose down

docker-compose-logs: ## View Docker Compose logs
	docker-compose logs -f

setup: ## Initial setup
	cp env.example .env
	@echo "Please edit .env file with your configuration"
	@echo "Then run: make install"

dev: ## Development setup
	make install-dev
	make format
	make test

ci: ## Continuous integration checks
	make format-check
	make lint
	make test-cov 