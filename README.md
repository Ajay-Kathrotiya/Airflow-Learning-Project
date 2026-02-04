# 🚀 Apache Airflow Full Course (Hands-On)

Welcome to the **Apache Airflow Full Course** 🎯  
This repository provides a **hands-on, practical introduction** to Apache Airflow, covering everything from **basic DAGs** to **advanced orchestration and asset dependencies**.

The course is designed for:
- ✅ Beginners starting with Airflow
- ✅ Intermediate users who want real-world patterns
- ✅ Data Engineers, Data Analysts, and DevOps engineers

---

## 📺 YouTube Tutorial

🎥 Watch the complete tutorial here:  
**Airflow Full Course** (link your YouTube video)

---

## 📚 Table of Contents

- [Course Structure](#-course-structure)
- [Getting Started](#-getting-started)
- [Running with Docker Compose](#-running-with-docker-compose)
- [DAGs Overview](#-dags-overview)
- [Key Concepts Covered](#-key-concepts-covered)
- [Custom Plugins](#-custom-plugins)
- [Logs](#-logs)
- [Contributing](#-contributing)
- [License](#-license)
- [References](#-references)

---

## 📂 Course Structure

```text
├── docker-compose.yaml      # Docker Compose setup for Airflow
├── main.py                  # Entry point or utility script
├── pyproject.toml           # Python project configuration
├── README.md                # Project documentation
├── config/                  # Configuration files
├── dags/                    # Airflow DAG examples
│   ├── 1_first_dag.py
│   ├── 2_dag_versioning.py
│   ├── 3_operators.py
│   ├── 4_XCOMs_auto.py
│   ├── 5_XCOMs_kwargs.py
│   ├── 6_parallel_tasks.py
│   ├── 7_branches.py
│   ├── 8_schedule_preset.py
│   ├── 9_schedule_cron.py
│   ├── 10_schedule_delta.py
│   ├── 11_incremental_load.py
│   ├── 12_special_dates.py
│   ├── asset_13.py
│   ├── 14_asset_dependent.py
│   ├── dag_orchestrate_1.py
│   ├── dag_orchestrate_2.py
│   └── dag_orchestrate_parent.py
├── logs/                    # Airflow logs
├── plugins/                 # Custom Airflow plugins
