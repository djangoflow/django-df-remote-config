# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

django-df-remote-config is a Django app for managing frontend application configuration via a REST API. It serves JSON config "parts" (e.g., legal, app_launch, default) filtered by attributes, with JSON Schema validation in the admin.

Requires Python 3.12+ and Django 6.0+.

## Development Commands

```bash
# Install dev dependencies
pip install -e .[test]

# Run tests
pytest

# Run a single test
pytest tests/test_file.py::test_name

# Linting (CI runs all three)
ruff check .
ruff format --check .
mypy .

# Auto-fix
ruff check --fix .
ruff format .

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

## Architecture

### Request Flow

`GET /api/remote-config/?part=<name>&<attributes>` is handled by:

1. **`RemoteConfigView`** (`drf/views.py`) — validates the `part` param against `api_settings.PARTS`, imports the configured `HANDLER_CLASS`, delegates to it
2. **Handlers** (`handlers.py`) — `DefaultHandler` queries `ConfigPart` objects filtered by name and attributes, returns `part.json`. `AppLaunchHandler` extends this by injecting an `updates` dict with last-modified timestamps per part
3. **`ConfigPart`** model (`models.py`) — stores JSON config with a name, sequence ordering, and M2M `ConfigAttribute` for key-value filtering via `ConfigPartQuerySet.filter_attributes()`

### Settings / Configuration

`DF_REMOTE_CONFIG` dict in Django settings, processed via DRF's `APISettings` in `settings.py`. Structure:

```python
DF_REMOTE_CONFIG = {
    "PARTS": {
        "part_name": {
            "HANDLER_CLASS": "dotted.path.to.Handler",  # optional, defaults to DefaultHandler
            "SCHEMA": "dotted.path.to.schema_dict",      # optional, falls back to schema.py
        },
    },
    "DEFAULT_PART": "default",
}
```

### Key Design Patterns

- **`NoMigrationsChoicesField`** (`fields.py`) — TextField that strips `choices` from `deconstruct()` so adding new part names doesn't generate migrations
- **JSON Schema per part** — `schema.py` defines `PART_SCHEMAS` (hardcoded) and `DEFAULT_SCHEMA`; parts can override via `SCHEMA` setting pointing to an importable dict. Used by admin's `JSONEditor` widget
- **Handler pattern** — each part can specify its own handler class via settings; handlers are instantiated per-request via `import_string`
- **DFMeta on AppConfig** — `api_path = "remote-config/"` is used by `django-df-api-drf` for automatic URL registration

### Dependencies

- `django-df-api-drf` — provides base DRF setup, URL auto-discovery via `DFMeta.api_path`, and `drf-spectacular` integration
- `django-jsoneditor` — admin JSON editing widget with schema validation
- `django-model-utils` — `TimeStampedModel` base for `ConfigPart`

### Linting

Uses ruff for both linting and formatting (replaced black). Config in `pyproject.toml` under `[tool.ruff]` and `[tool.ruff.lint]`.

## Test Configuration

- Django settings: `tests/settings.py` (uses SQLite)
- pytest config in `pyproject.toml`, `DJANGO_SETTINGS_MODULE = "tests.settings"`
- URLs: `tests/urls.py` includes `df_api_drf.urls` which auto-discovers this app's DRF urls
