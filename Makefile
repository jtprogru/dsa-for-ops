.DEFAULT_GOAL := help

# Список доступных лабораторных (имена модулей без расширения), отсортированный
LABS := $(sort $(patsubst labs/%.py,%,$(wildcard labs/lab*.py)))
# Имя лабораторной, переданное после `run` (например, `make run lab01`)
RUN_ARGS := $(filter-out run,$(MAKECMDGOALS))
# Go-модули (каталоги с go.mod внутри src/golang)
GO_MODULES := $(sort $(dir $(wildcard src/golang/*/go.mod)))

.PHONY: help sync test run clean docs docs-build go-build go-vet go-test

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

sync: ## Установить зависимости
	uv sync

test: ## Запустить тесты
	uv run pytest -v

run: ## Запустить лабораторную (make run lab01) или показать список (make run)
ifeq ($(RUN_ARGS),)
	@echo "Доступные лабораторные работы:"
	@for lab in $(LABS); do echo "  $$lab"; done
	@echo ""
	@echo "Запуск: make run lab01"
else ifeq ($(filter $(RUN_ARGS),$(LABS)),)
	@echo "Лабораторная '$(RUN_ARGS)' не найдена. Доступные:"
	@for lab in $(LABS); do echo "  $$lab"; done
	@exit 1
else
	uv run python -m labs.$(RUN_ARGS)
endif

# Перехватываем имена лабораторных, переданные как цели, чтобы make не ругался.
lab%:
	@:

docs: ## Запустить локальный сервер документации (http://127.0.0.1:8000)
	uv run --group docs mkdocs serve

docs-build: ## Собрать статический сайт документации в site/
	uv run --group docs mkdocs build --strict

go-build: ## Собрать все Go-модули (src/golang/*)
	@for m in $(GO_MODULES); do echo "==> $$m"; (cd $$m && go build ./...) || exit 1; done

go-vet: ## Прогнать go vet по всем Go-модулям
	@for m in $(GO_MODULES); do echo "==> $$m"; (cd $$m && go vet ./...) || exit 1; done

go-test: ## Прогнать go test по всем Go-модулям
	@for m in $(GO_MODULES); do echo "==> $$m"; (cd $$m && go test ./...) || exit 1; done

clean: ## Удалить кэш и временные файлы
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	rm -rf site
