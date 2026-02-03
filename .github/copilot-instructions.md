# Copilot Instructions for AI Agents

## Project Overview
This repository is an Apache Airflow tutorial project, designed for local development and experimentation with Airflow DAGs, operators, and integrations. The project is containerized using Docker Compose and uses a CeleryExecutor setup with Redis and PostgreSQL.

## Key Components
- **dags/**: Contains all Airflow DAG definitions. Each file is a separate DAG example, demonstrating different Airflow features and patterns.
- **config/airflow.cfg**: Main Airflow configuration. Many behaviors (executor, authentication, logging, integrations) are controlled here.
- **docker-compose.yaml**: Orchestrates the Airflow environment, including webserver, scheduler, workers, Redis, and PostgreSQL. Environment variables and volumes are set here.
- **logs/**: Stores Airflow logs, mapped as a volume in Docker.
- **plugins/**: For custom Airflow plugins (empty by default).

## Developer Workflows
- **Start/Stop Airflow**: Use `docker-compose up` and `docker-compose down` to start/stop the full Airflow stack.
- **Access UI**: Airflow webserver is available at http://localhost:8080 (default credentials: airflow/airflow).
- **Add/Modify DAGs**: Place Python files in `dags/`. Changes are picked up automatically by the scheduler.
- **Install Python dependencies**: Add to `pyproject.toml` and rebuild the Docker image if needed.
- **Environment Variables**: Set in `.env` or directly in `docker-compose.yaml`.

## Project-Specific Conventions
- **DAG Naming**: Each DAG file is named with a numeric prefix for ordering and clarity (e.g., `1_first_dag.py`, `10_incremental_load.py`).
- **Configuration**: All Airflow settings are managed in `config/airflow.cfg` and/or via environment variables in Docker Compose.
- **No custom plugins**: The `plugins/` directory is present but not used by default.
- **CeleryExecutor**: The default executor is Celery; ensure Redis and PostgreSQL are running.
- **User/Permissions**: The default admin user is set via Docker Compose environment variables.

## Integration & External Dependencies
- **Airflow**: Version pinned in `pyproject.toml` and Docker image.
- **PostgreSQL**: Used as the Airflow metadata database.
- **Redis**: Used as the Celery broker.
- **OpenLineage, Sentry, Azure, AWS, Elasticsearch**: Configuration stubs are present in `airflow.cfg` for advanced integrations, but not enabled by default.

## Examples & Patterns
- See `dags/1_first_dag.py` for a minimal DAG example.
- See `dags/10_incremental_load.py` for incremental data load patterns.
- All DAGs are self-contained and demonstrate a single concept or feature.

## Tips for AI Agents
- Always check `docker-compose.yaml` and `config/airflow.cfg` for environment and configuration changes.
- When adding new dependencies, prefer updating `pyproject.toml` and rebuilding the Docker image.
- Use the numeric prefix convention for new DAG files.
- Avoid editing files in `logs/` or `__pycache__/`.

---
For more details, see the official [Airflow documentation](https://airflow.apache.org/docs/).
