.DEFAULT_GOAL := help

# Список доступных лабораторных (имена модулей без расширения), отсортированный
LABS := $(sort $(patsubst labs/%.py,%,$(wildcard labs/lab*.py)))
# Имя лабораторной, переданное после `run` (например, `make run lab01`)
RUN_ARGS := $(filter-out run,$(MAKECMDGOALS))

.PHONY: help sync test run clean

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

clean: ## Удалить кэш и временные файлы
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
