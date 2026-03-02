# Apache Oozie


## Table of Contents

- [Apache Oozie](#apache-oozie)
- [Overview](#overview)
- [What is Apache Oozie?](#what-is-apache-oozie)
  - [Key Characteristics](#key-characteristics)
- [Oozie Components](#oozie-components)
  - [1. Oozie Workflow](#1-oozie-workflow)
  - [2. Oozie Coordinator](#2-oozie-coordinator)
  - [3. Oozie Bundle](#3-oozie-bundle)
- [Oozie Workflow Definition](#oozie-workflow-definition)
  - [Basic Workflow Structure](#basic-workflow-structure)
  - [Decision Nodes](#decision-nodes)
  - [Fork and Join Nodes](#fork-and-join-nodes)
- [Oozie Coordinator Jobs](#oozie-coordinator-jobs)
  - [Time-Based Coordination](#time-based-coordination)
  - [Data-Availability Coordination](#data-availability-coordination)
- [Integration with Hadoop Ecosystem](#integration-with-hadoop-ecosystem)
  - [MapReduce Integration](#mapreduce-integration)
  - [Pig Integration](#pig-integration)
  - [Hive Integration](#hive-integration)
  - [Sqoop Integration](#sqoop-integration)
- [IoT Workflow Examples](#iot-workflow-examples)
  - [Example 1: Daily Sensor Data Pipeline](#example-1-daily-sensor-data-pipeline)
  - [Example 2: Real-time Alert Generation](#example-2-real-time-alert-generation)
- [Oozie Workflow Execution](#oozie-workflow-execution)
  - [Submitting a Workflow](#submitting-a-workflow)
- [Submit workflow](#submit-workflow)
- [Job properties file (job.properties)](#job-properties-file-jobproperties)
  - [Monitoring Workflows](#monitoring-workflows)
- [Check job status](#check-job-status)
- [View job log](#view-job-log)
- [List running jobs](#list-running-jobs)
  - [Managing Workflows](#managing-workflows)
- [Suspend a running job](#suspend-a-running-job)
- [Resume a suspended job](#resume-a-suspended-job)
- [Kill a running job](#kill-a-running-job)
- [Rerun a failed job](#rerun-a-failed-job)
- [Advantages of Oozie](#advantages-of-oozie)
- [Limitations of Oozie](#limitations-of-oozie)
- [Summary](#summary)
- [Key Takeaways for Exams](#key-takeaways-for-exams)

## Overview

Apache Oozie is a workflow scheduler system designed to manage and coordinate Hadoop jobs. In IoT environments where data processing involves multiple interconnected steps—data ingestion, cleaning, transformation, analysis, and reporting—Oozie orchestrates these complex workflows automatically. It ensures that jobs execute in the correct order, handles dependencies, manages failures, and provides monitoring capabilities for large-scale data processing pipelines.

## What is Apache Oozie?

Apache Oozie is a server-based workflow scheduling system that manages Apache Hadoop jobs. Oozie workflows are collections of actions arranged in a control dependency directed acyclic graph (DAG), where actions are Hadoop jobs such as MapReduce, Pig, Hive, Sqoop, or even Java programs.

### Key Characteristics

**1. Workflow Management:**

- Define multi-step data processing pipelines
- Specify job dependencies and execution order
- Control flow with decision nodes and forks

**2. Scheduling:**

- Time-based triggers (cron-like)
- Data availability triggers
- Event-driven execution

**3. Integration:**

- Native support for Hadoop ecosystem
- MapReduce, Pig, Hive, Sqoop, Spark
- Custom actions via shell scripts or Java

**4. Scalability:**

- Handles thousands of workflows
- Distributed execution across cluster
- Efficient resource utilization

**5. Fault Tolerance:**

- Automatic retry on failures
- Configurable retry policies
- Recovery from checkpoint

## Oozie Components

### 1. Oozie Workflow

A workflow is a collection of actions arranged in a DAG that defines the sequence of operations.

**Structure:**

```xml
<workflow-app name="sample-workflow" xmlns="uri:oozie:workflow:0.5">
    <start to="action1"/>

    <action name="action1">
        <!-- Action definition -->
        <ok to="action2"/>
        <error to="fail"/>
    </action>

    <action name="action2">
        <!-- Action definition -->
        <ok to="end"/>
        <error to="fail"/>
    </action>

    <kill name="fail">
        <message>Workflow failed</message>
    </kill>

    <end name="end"/>
</workflow-app>
```

**Workflow Nodes:**

**Control Nodes:**

- **start:** Entry point of workflow
- **end:** Successful completion
- **kill:** Failure termination
- **decision:** Conditional branching
- **fork/join:** Parallel execution
- **action:** Actual work execution

**Action Nodes:**

- MapReduce action
- Pig action
- Hive action
- Sqoop action
- Shell action
- Java action
- Spark action

### 2. Oozie Coordinator

A coordinator job schedules and triggers workflow jobs based on time or data availability.

**Features:**

- Time-based scheduling (like cron)
- Data-triggered execution
- Manages multiple workflow instances
- Handles late data scenarios

**Example:**

```xml
<coordinator-app name="daily-sensor-analysis"
                 frequency="${coord:days(1)}"
                 start="2024-01-01T00:00Z"
                 end="2024-12-31T23:59Z"
                 timezone="UTC">

    <datasets>
        <dataset name="sensor-data"
                 frequency="${coord:days(1)}"
                 initial-instance="2024-01-01T00:00Z"
                 timezone="UTC">
            <uri-template>
                /data/sensors/${YEAR}/${MONTH}/${DAY}
            </uri-template>
        </dataset>
    </datasets>

    <input-events>
        <data-in name="input" dataset="sensor-data">
            <instance>${coord:current(0)}</instance>
        </data-in>
    </input-events>

    <action>
        <workflow>
            <app-path>${workflowPath}</app-path>
        </workflow>
    </action>
</coordinator-app>
```

### 3. Oozie Bundle

A bundle is a higher-level abstraction that manages multiple coordinator jobs as a single unit.

**Purpose:**

- Group related coordinators
- Start/stop multiple jobs together
- Manage lifecycle of coordinated processes

**Example:**

```xml
<bundle-app name="iot-analytics-bundle">
    <coordinator name="hourly-alerts">
        <app-path>/path/to/hourly-coordinator</app-path>
    </coordinator>

    <coordinator name="daily-reports">
        <app-path>/path/to/daily-coordinator</app-path>
    </coordinator>

    <coordinator name="weekly-trends">
        <app-path>/path/to/weekly-coordinator</app-path>
    </coordinator>
</bundle-app>
```

## Oozie Workflow Definition

### Basic Workflow Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<workflow-app name="sensor-data-processing" xmlns="uri:oozie:workflow:0.5">

    <!-- Start Node -->
    <start to="data-ingestion"/>

    <!-- MapReduce Action -->
    <action name="data-ingestion">
        <map-reduce>
            <job-tracker>${jobTracker}</job-tracker>
            <name-node>${nameNode}</name-node>
            <configuration>
                <property>
                    <name>mapred.mapper.class</name>
                    <value>com.example.SensorMapper</value>
                </property>
                <property>
                    <name>mapred.reducer.class</name>
                    <value>com.example.SensorReducer</value>
                </property>
                <property>
                    <name>mapred.input.dir</name>
                    <value>${inputDir}</value>
                </property>
                <property>
                    <name>mapred.output.dir</name>
                    <value>${outputDir}/raw</value>
                </property>
            </configuration>
        </map-reduce>
        <ok to="data-cleaning"/>
        <error to="fail"/>
    </action>

    <!-- Pig Action -->
    <action name="data-cleaning">
        <pig>
            <job-tracker>${jobTracker}</job-tracker>
            <name-node>${nameNode}</name-node>
            <script>clean-sensor-data.pig</script>
            <param>INPUT=${outputDir}/raw</param>
            <param>OUTPUT=${outputDir}/clean</param>
        </pig>
        <ok to="data-analysis"/>
        <error to="fail"/>
    </action>

    <!-- Hive Action -->
    <action name="data-analysis">
        <hive>
            <job-tracker>${jobTracker}</job-tracker>
            <name-node>${nameNode}</name-node>
            <script>analyze-sensors.hql</script>
            <param>input_table=${outputDir}/clean</param>
            <param>output_table=sensor_analysis</param>
        </hive>
        <ok to="generate-report"/>
        <error to="fail"/>
    </action>

    <!-- Shell Action -->
    <action name="generate-report">
        <shell>
            <job-tracker>${jobTracker}</job-tracker>
            <name-node>${nameNode}</name-node>
            <exec>generate-report.sh</exec>
            <argument>${outputDir}</argument>
            <file>generate-report.sh#generate-report.sh</file>
        </shell>
        <ok to="end"/>
        <error to="fail"/>
    </action>

    <!-- Kill Node -->
    <kill name="fail">
        <message>Sensor data processing failed: ${wf:errorMessage(wf:lastErrorNode())}</message>
    </kill>

    <!-- End Node -->
    <end name="end"/>
</workflow-app>
```

### Decision Nodes

Decision nodes enable conditional execution based on expressions.

```xml
<decision name="check-data-quality">
    <switch>
        <case to="high-quality-processing">
            ${fs:fileSize(dataQualityScore) gt 0.9}
        </case>
        <case to="low-quality-processing">
            ${fs:fileSize(dataQualityScore) lt 0.5}
        </case>
        <default to="normal-processing"/>
    </switch>
</decision>

<action name="high-quality-processing">
    <!-- Advanced analytics -->
    <ok to="end"/>
    <error to="fail"/>
</action>

<action name="low-quality-processing">
    <!-- Basic analytics with filtering -->
    <ok to="end"/>
    <error to="fail"/>
</action>

<action name="normal-processing">
    <!-- Standard analytics -->
    <ok to="end"/>
    <error to="fail"/>
</action>
```

### Fork and Join Nodes

Fork and join enable parallel execution of independent tasks.

```xml
<fork name="parallel-processing">
    <path start="temperature-analysis"/>
    <path start="pressure-analysis"/>
    <path start="humidity-analysis"/>
</fork>

<action name="temperature-analysis">
    <map-reduce>
        <!-- Temperature processing -->
    </map-reduce>
    <ok to="join-results"/>
    <error to="fail"/>
</action>

<action name="pressure-analysis">
    <map-reduce>
        <!-- Pressure processing -->
    </map-reduce>
    <ok to="join-results"/>
    <error to="fail"/>
</action>

<action name="humidity-analysis">
    <map-reduce>
        <!-- Humidity processing -->
    </map-reduce>
    <ok to="join-results"/>
    <error to="fail"/>
</action>

<join name="join-results" to="consolidate-reports"/>

<action name="consolidate-reports">
    <!-- Merge all analysis results -->
    <ok to="end"/>
    <error to="fail"/>
</action>
```

## Oozie Coordinator Jobs

### Time-Based Coordination

Schedule workflows to run at specific times or intervals.

```xml
<coordinator-app name="hourly-sensor-processing"
                 frequency="${coord:hours(1)}"
                 start="2024-01-01T00:00Z"
                 end="2024-12-31T23:59Z"
                 timezone="UTC">

    <action>
        <workflow>
            <app-path>${workflowAppPath}</app-path>
            <configuration>
                <property>
                    <name>inputDir</name>
                    <value>/data/sensors/${coord:formatTime(coord:nominalTime(), 'yyyyMMdd/HH')}</value>
                </property>
                <property>
                    <name>outputDir</name>
                    <value>/output/sensors/${coord:formatTime(coord:nominalTime(), 'yyyyMMdd/HH')}</value>
                </property>
            </configuration>
        </workflow>
    </action>
</coordinator-app>
```

### Data-Availability Coordination

Trigger workflows when input data becomes available.

```xml
<coordinator-app name="data-driven-processing"
                 frequency="${coord:hours(1)}"
                 start="2024-01-01T00:00Z"
                 end="2024-12-31T23:59Z"
                 timezone="UTC">

    <datasets>
        <dataset name="sensor-input"
                 frequency="${coord:hours(1)}"
                 initial-instance="2024-01-01T00:00Z"
                 timezone="UTC">
            <uri-template>
                /data/sensors/${YEAR}${MONTH}${DAY}/${HOUR}
            </uri-template>
        </dataset>

        <dataset name="processed-output"
                 frequency="${coord:hours(1)}"
                 initial-instance="2024-01-01T00:00Z"
                 timezone="UTC">
            <uri-template>
                /output/sensors/${YEAR}${MONTH}${DAY}/${HOUR}
            </uri-template>
        </dataset>
    </datasets>

    <input-events>
        <data-in name="sensor-data" dataset="sensor-input">
            <instance>${coord:current(0)}</instance>
        </data-in>
    </input-events>

    <output-events>
        <data-out name="processed-data" dataset="processed-output">
            <instance>${coord:current(0)}</instance>
        </data-out>
    </output-events>

    <action>
        <workflow>
            <app-path>${workflowAppPath}</app-path>
            <configuration>
                <property>
                    <name>inputDir</name>
                    <value>${coord:dataIn('sensor-data')}</value>
                </property>
                <property>
                    <name>outputDir</name>
                    <value>${coord:dataOut('processed-data')}</value>
                </property>
            </configuration>
        </workflow>
    </action>
</coordinator-app>
```

## Integration with Hadoop Ecosystem

### MapReduce Integration

```xml
<action name="mapreduce-job">
    <map-reduce>
        <job-tracker>${jobTracker}</job-tracker>
        <name-node>${nameNode}</name-node>
        <prepare>
            <delete path="${outputDir}"/>
        </prepare>
        <configuration>
            <property>
                <name>mapred.job.queue.name</name>
                <value>${queueName}</value>
            </property>
            <property>
                <name>mapred.mapper.class</name>
                <value>com.example.IoTMapper</value>
            </property>
            <property>
                <name>mapred.reducer.class</name>
                <value>com.example.IoTReducer</value>
            </property>
            <property>
                <name>mapred.input.dir</name>
                <value>${inputDir}</value>
            </property>
            <property>
                <name>mapred.output.dir</name>
                <value>${outputDir}</value>
            </property>
        </configuration>
    </map-reduce>
    <ok to="next-action"/>
    <error to="fail"/>
</action>
```

### Pig Integration

```xml
<action name="pig-aggregation">
    <pig>
        <job-tracker>${jobTracker}</job-tracker>
        <name-node>${nameNode}</name-node>
        <prepare>
            <delete path="${outputPath}"/>
        </prepare>
        <script>sensor-aggregation.pig</script>
        <param>INPUT=${inputPath}</param>
        <param>OUTPUT=${outputPath}</param>
        <param>DATE=${date}</param>
    </pig>
    <ok to="next-action"/>
    <error to="fail"/>
</action>
```

### Hive Integration

```xml
<action name="hive-analysis">
    <hive>
        <job-tracker>${jobTracker}</job-tracker>
        <name-node>${nameNode}</name-node>
        <script>sensor-analysis.hql</script>
        <param>INPUT_TABLE=${inputTable}</param>
        <param>OUTPUT_TABLE=${outputTable}</param>
        <param>PARTITION_DATE=${partitionDate}</param>
    </hive>
    <ok to="next-action"/>
    <error to="fail"/>
</action>
```

### Sqoop Integration

```xml
<action name="sqoop-export">
    <sqoop>
        <job-tracker>${jobTracker}</job-tracker>
        <name-node>${nameNode}</name-node>
        <command>export --connect ${dbConnectionString} --table sensor_results --export-dir ${hdfsExportDir} --username ${dbUser} --password ${dbPassword}</command>
    </sqoop>
    <ok to="end"/>
    <error to="fail"/>
</action>
```

## IoT Workflow Examples

### Example 1: Daily Sensor Data Pipeline

**Scenario:** Process daily sensor data through cleaning, aggregation, and reporting.

```xml
<workflow-app name="daily-sensor-pipeline" xmlns="uri:oozie:workflow:0.5">
    <start to="validate-input"/>

    <!-- Check if input data exists -->
    <decision name="validate-input">
        <switch>
            <case to="ingest-data">
                ${fs:exists(inputPath)}
            </case>
            <default to="no-data"/>
        </switch>
    </decision>

    <!-- Data ingestion -->
    <action name="ingest-data">
        <map-reduce>
            <!-- Ingest raw sensor data -->
        </map-reduce>
        <ok to="parallel-processing"/>
        <error to="fail"/>
    </action>

    <!-- Parallel processing of different sensor types -->
    <fork name="parallel-processing">
        <path start="process-temperature"/>
        <path start="process-pressure"/>
        <path start="process-humidity"/>
    </fork>

    <action name="process-temperature">
        <pig>
            <script>process-temperature.pig</script>
        </pig>
        <ok to="join-processing"/>
        <error to="fail"/>
    </action>

    <action name="process-pressure">
        <pig>
            <script>process-pressure.pig</script>
        </pig>
        <ok to="join-processing"/>
        <error to="fail"/>
    </action>

    <action name="process-humidity">
        <pig>
            <script>process-humidity.pig</script>
        </pig>
        <ok to="join-processing"/>
        <error to="fail"/>
    </action>

    <join name="join-processing" to="generate-insights"/>

    <!-- Generate insights using Hive -->
    <action name="generate-insights">
        <hive>
            <script>generate-insights.hql</script>
        </hive>
        <ok to="export-results"/>
        <error to="fail"/>
    </action>

    <!-- Export to database -->
    <action name="export-results">
        <sqoop>
            <command>export --table daily_sensor_analysis</command>
        </sqoop>
        <ok to="end"/>
        <error to="fail"/>
    </action>

    <kill name="no-data">
        <message>No input data available for processing</message>
    </kill>

    <kill name="fail">
        <message>Workflow failed: ${wf:errorMessage(wf:lastErrorNode())}</message>
    </kill>

    <end name="end"/>
</workflow-app>
```

### Example 2: Real-time Alert Generation

**Coordinator for hourly anomaly detection:**

```xml
<coordinator-app name="hourly-anomaly-detection"
                 frequency="${coord:hours(1)}"
                 start="2024-01-01T00:00Z"
                 end="2099-12-31T23:59Z"
                 timezone="UTC">

    <datasets>
        <dataset name="sensor-logs"
                 frequency="${coord:hours(1)}"
                 initial-instance="2024-01-01T00:00Z"
                 timezone="UTC">
            <uri-template>
                /logs/sensors/${YEAR}/${MONTH}/${DAY}/${HOUR}
            </uri-template>
        </dataset>
    </datasets>

    <input-events>
        <data-in name="hourly-logs" dataset="sensor-logs">
            <instance>${coord:current(0)}</instance>
        </data-in>
    </input-events>

    <action>
        <workflow>
            <app-path>/workflows/anomaly-detection</app-path>
            <configuration>
                <property>
                    <name>inputLogs</name>
                    <value>${coord:dataIn('hourly-logs')}</value>
                </property>
                <property>
                    <name>timestamp</name>
                    <value>${coord:formatTime(coord:nominalTime(), 'yyyy-MM-dd-HH')}</value>
                </property>
            </configuration>
        </workflow>
    </action>
</coordinator-app>
```

## Oozie Workflow Execution

### Submitting a Workflow

```bash
# Submit workflow
oozie job -oozie http://localhost:11000/oozie -config job.properties -run

# Job properties file (job.properties)
nameNode=hdfs://localhost:9000
jobTracker=localhost:8032
queueName=default
workflowPath=/user/oozie/workflows/sensor-processing
inputDir=/data/sensors/2024/01/15
outputDir=/output/sensors/2024/01/15
```

### Monitoring Workflows

```bash
# Check job status
oozie job -oozie http://localhost:11000/oozie -info <job-id>

# View job log
oozie job -oozie http://localhost:11000/oozie -log <job-id>

# List running jobs
oozie jobs -oozie http://localhost:11000/oozie -jobtype workflow -filter status=RUNNING
```

### Managing Workflows

```bash
# Suspend a running job
oozie job -oozie http://localhost:11000/oozie -suspend <job-id>

# Resume a suspended job
oozie job -oozie http://localhost:11000/oozie -resume <job-id>

# Kill a running job
oozie job -oozie http://localhost:11000/oozie -kill <job-id>

# Rerun a failed job
oozie job -oozie http://localhost:11000/oozie -rerun <job-id>
```

## Advantages of Oozie

1. **Workflow Orchestration:** Manages complex multi-step data pipelines
2. **Scheduling:** Time and data-based triggers for automation
3. **Integration:** Native support for Hadoop ecosystem tools
4. **Scalability:** Handles thousands of concurrent workflows
5. **Fault Tolerance:** Automatic retry and recovery mechanisms
6. **Monitoring:** Web UI and CLI for job tracking
7. **Flexibility:** Supports custom actions and extensions

## Limitations of Oozie

1. **XML Configuration:** Verbose and complex workflow definitions
2. **Limited UI:** Basic web interface compared to modern tools
3. **Learning Curve:** Requires understanding of XML and Oozie concepts
4. **Debugging:** Difficult to troubleshoot complex workflows
5. **Version Control:** XML files can be challenging to manage

## Summary

Apache Oozie is a workflow scheduler for Hadoop that orchestrates complex data processing pipelines in IoT environments. It provides three main abstractions: workflows (DAG of actions), coordinators (time/data-based scheduling), and bundles (grouping coordinators).

Workflows are defined in XML and consist of control nodes (start, end, decision, fork/join) and action nodes (MapReduce, Pig, Hive, Sqoop). Oozie integrates seamlessly with the Hadoop ecosystem, enabling automated execution of multi-step data pipelines.

For IoT applications, Oozie manages daily sensor data processing, hourly anomaly detection, and multi-stage analytics pipelines. It provides fault tolerance through automatic retries, monitoring through web UI and CLI, and scalability to handle thousands of concurrent workflows.

## Key Takeaways for Exams

1. **Oozie Definition:** Workflow scheduler for Hadoop managing and coordinating jobs

2. **Three Components:** Workflow (DAG of actions), Coordinator (scheduling), Bundle (group coordinators)

3. **Workflow Nodes:** Control nodes (start, end, kill, decision, fork/join) and action nodes (MapReduce, Pig, Hive, Sqoop, Shell)

4. **XML Structure:** Workflows defined in XML with start, actions (ok/error transitions), kill, and end nodes

5. **Coordinator Features:** Time-based scheduling (frequency), data-triggered execution, dataset definitions

6. **Integration:** Native support for MapReduce, Pig, Hive, Sqoop, Spark

7. **Parallel Execution:** Fork node splits flow, join node merges, enables parallel processing

8. **Decision Nodes:** Conditional branching based on expressions (switch-case-default)

9. **IoT Use Cases:** Daily sensor pipelines, hourly anomaly detection, multi-stage analytics

10. **Advantages:** Orchestration, scheduling, integration, scalability, fault tolerance, monitoring
