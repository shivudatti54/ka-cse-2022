# Apache Oozie

=====================================

### Overview

Apache Oozie is a workflow scheduler system for managing and coordinating Hadoop jobs. It orchestrates complex multi-step data processing pipelines, handling job dependencies, scheduling, failure management, and monitoring for large-scale IoT analytics workflows.

### Key Points

- **Three Abstractions:** Workflow (DAG of actions), Coordinator (time/data-based scheduling), and Bundle (groups multiple coordinators)
- **Workflow Nodes:** Control nodes (start, end, kill, decision, fork/join) and Action nodes (MapReduce, Pig, Hive, Sqoop, Shell, Spark)
- **Decision Nodes:** Enable conditional branching using switch-case-default expressions for dynamic workflow paths
- **Fork and Join:** Fork splits execution into parallel paths; Join synchronizes all parallel paths before proceeding
- **Coordinator Scheduling:** Supports time-based triggers (cron-like frequency) and data-availability triggers when input data arrives
- **XML-Based Definition:** Workflows defined in XML with action transitions specified through ok (success) and error (failure) paths
- **Fault Tolerance:** Automatic retry on failures, configurable retry policies, and recovery from checkpoints

### Important Concepts

- Workflows are Directed Acyclic Graphs (DAGs) where actions have explicit ok and error transition paths
- Coordinators manage recurring workflow instances using frequency expressions like coord:days(1) or coord:hours(1)
- Bundles group related coordinators (hourly alerts, daily reports, weekly trends) for unified lifecycle management
- Oozie integrates natively with the entire Hadoop ecosystem including MapReduce, Pig, Hive, Sqoop, and Spark

### Notes

- Know the XML structure of a basic workflow: start node, action nodes with ok/error transitions, kill node, and end node
- Understand the difference between Workflow (single execution), Coordinator (recurring schedule), and Bundle (group management)
- IoT pipeline example: Data Ingestion (MapReduce) -> Cleaning (Pig) -> Analysis (Hive) -> Report Generation (Shell) -> Export (Sqoop)
