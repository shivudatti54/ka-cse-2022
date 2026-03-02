# Programming with Google App Engine


## Table of Contents

- [Programming with Google App Engine](#programming-with-google-app-engine)
- [Introduction to Google App Engine](#introduction-to-google-app-engine)
- [Core Architecture and Components](#core-architecture-and-components)
  - [Service Model](#service-model)
  - [Runtime Environments](#runtime-environments)
  - [Core Services](#core-services)
- [Application Development Lifecycle](#application-development-lifecycle)
  - [Development Process](#development-process)
  - [Project Structure](#project-structure)
- [Programming Models and Patterns](#programming-models-and-patterns)
  - [Web Application Programming](#web-application-programming)
  - [Microservices Architecture](#microservices-architecture)
- [app.yaml for main service](#appyaml-for-main-service)
- [app.yaml for API service](#appyaml-for-api-service)
- [Data Management with Datastore](#data-management-with-datastore)
  - [Data Modeling](#data-modeling)
- [Create entity](#create-entity)
  - [Querying Data](#querying-data)
- [Basic query](#basic-query)
- [Ancestor query](#ancestor-query)
  - [Transactions](#transactions)
- [Read operations](#read-operations)
- [Write operations](#write-operations)
- [Scaling and Performance Optimization](#scaling-and-performance-optimization)
  - [Scaling Types](#scaling-types)
  - [Instance Classes](#instance-classes)
  - [Caching Strategies](#caching-strategies)
- [Set cache](#set-cache)
- [Get cache](#get-cache)
- [Security and Authentication](#security-and-authentication)
  - [Identity and Access Management](#identity-and-access-management)
- [Check if user is logged in](#check-if-user-is-logged-in)
- [Check if user is admin](#check-if-user-is-admin)
  - [Application Security](#application-security)
- [app.yaml security configuration](#appyaml-security-configuration)
- [Deployment and Operations](#deployment-and-operations)
  - [Deployment Process](#deployment-process)
- [Install Google Cloud SDK](#install-google-cloud-sdk)
- [Authenticate](#authenticate)
- [Set project](#set-project)
- [Deploy application](#deploy-application)
- [View deployment](#view-deployment)
  - [Version Management](#version-management)
- [Deploy new version](#deploy-new-version)
- [Set traffic splitting](#set-traffic-splitting)
  - [Monitoring and Logging](#monitoring-and-logging)
- [Structured logging](#structured-logging)
- [Comparison with Other Cloud Platforms](#comparison-with-other-cloud-platforms)
- [Exam Tips](#exam-tips)

## Introduction to Google App Engine

Google App Engine (GAE) is a Platform-as-a-Service (PaaS) offering from Google Cloud Platform that enables developers to build and deploy scalable web applications and mobile backends without managing the underlying infrastructure. As part of Module 5: Cloud Programming and Software Environments, GAE represents a key implementation of cloud platform architecture that demonstrates the practical application of distributed systems principles.

GAE abstracts away server management and infrastructure concerns, allowing developers to focus solely on writing code. It automatically handles scaling, load balancing, health checking, and other operational tasks, making it an ideal platform for rapid application development and deployment.

## Core Architecture and Components

### Service Model

GAE operates as a PaaS (Platform-as-Service) within the cloud computing service model hierarchy:

- **IaaS**: Infrastructure (e.g., Google Compute Engine)
- **PaaS**: Platform (e.g., Google App Engine)
- **SaaS**: Software (e.g., Google Workspace)

```markdown
+-----------------------+
| Application |
+-----------------------+
| App Engine Runtime |
+-----------------------+
| Managed Infrastructure|
| (Compute, Storage, Network)|
+-----------------------+
```

### Runtime Environments

GAE supports multiple runtime environments:

| Runtime              | Languages Supported                   | Key Characteristics                            |
| -------------------- | ------------------------------------- | ---------------------------------------------- |
| Standard Environment | Python, Java, Node.js, Go, PHP, Ruby  | Sandboxed, automatic scaling, free tier        |
| Flexible Environment | Python, Java, Node.js, Go, Ruby, .NET | Docker containers, custom runtimes, SSH access |

### Core Services

GAE provides several built-in services that form the application ecosystem:

1. **Datastore**: NoSQL document database
2. **Cloud Storage**: File and object storage
3. **Memcache**: In-memory caching service
4. **Task Queues**: Asynchronous task processing
5. **Cron Service**: Scheduled task execution
6. **Search**: Full-text search capabilities
7. **Users API**: Authentication and authorization

## Application Development Lifecycle

### Development Process

The typical GAE development workflow follows these steps:

1. **Application Design**: Plan application structure and data model
2. **Local Development**: Develop using local development server
3. **Testing**: Test application functionality and performance
4. **Deployment**: Deploy to GAE using gcloud CLI
5. **Monitoring**: Use Cloud Monitoring and Logging
6. **Scaling**: Monitor and adjust scaling parameters

```markdown
+----------------+ +----------------+ +----------------+
| Design | --> | Develop | --> | Test |
+----------------+ +----------------+ +----------------+
^ | |
| v |
+----------------+ +----------------+ +----------------+
| Monitor | <-- | Deploy | <-- | Debug |
+----------------+ +----------------+ +----------------+
```

### Project Structure

A typical GAE application has the following structure:

```markdown
my-app/
app.yaml # Application configuration
appengine_config.py # Custom runtime configuration
main.py # Main application module
requirements.txt # Python dependencies
static/ # Static files (CSS, JS, images)
styles.css
script.js
templates/ # HTML templates
index.html
```

## Programming Models and Patterns

### Web Application Programming

GAE supports traditional web application development using various frameworks:

**Example: Flask Application in Python**

```python
from flask import Flask, render_template
import google.cloud.datastore as datastore

app = Flask(__name__)
client = datastore.Client()

@app.route('/')
def index():
    query = client.query(kind='Task')
    tasks = list(query.fetch())
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = datastore.Entity(key=client.key('Task'))
    task.update({'description': request.form['description']})
    client.put(task)
    return redirect('/')
```

### Microservices Architecture

GAE supports building applications as collections of microservices:

```yml
# app.yaml for main service
service: default
runtime: python39
entrypoint: gunicorn -b :$PORT main:app

# app.yaml for API service
service: api
runtime: python39
entrypoint: gunicorn -b :$PORT api:app
```

Each service can be deployed independently and communicate via HTTP requests or task queues.

## Data Management with Datastore

### Data Modeling

Google Cloud Datastore is a NoSQL document database that uses entities, kinds, and properties:

**Entity Structure:**

```python
from google.cloud import datastore

# Create entity
client = datastore.Client()
key = client.key('User', 'user123')
entity = datastore.Entity(key=key)
entity.update({
    'name': 'John Doe',
    'email': 'john@example.com',
    'created': datetime.datetime.utcnow()
})
client.put(entity)
```

### Querying Data

```python
# Basic query
query = client.query(kind='User')
query.add_filter('name', '=', 'John Doe')
results = list(query.fetch())

# Ancestor query
ancestor_key = client.key('UserGroup', 'group1')
query = client.query(kind='User', ancestor=ancestor_key)
```

### Transactions

```python
with client.transaction():
    # Read operations
    key1 = client.key('Account', 'account1')
    account1 = client.get(key1)

    # Write operations
    account1['balance'] -= 100
    client.put(account1)
```

## Scaling and Performance Optimization

### Scaling Types

GAE offers different scaling options:

| Scaling Type      | Description                                | Use Cases              |
| ----------------- | ------------------------------------------ | ---------------------- |
| Automatic Scaling | Scales based on request rate               | Web applications, APIs |
| Manual Scaling    | Fixed number of instances                  | Background processing  |
| Basic Scaling     | Scales between zero and configured maximum | Intermittent workloads |

### Instance Classes

Different instance classes provide varying levels of performance:

| Instance Class | Memory  | CPU     | Cost       |
| -------------- | ------- | ------- | ---------- |
| F1 (Free)      | 256MB   | 600MHz  | Free       |
| F2             | 512MB   | 1.2GHz  | Low        |
| F4             | 1GB     | 2.4GHz  | Medium     |
| B1, B2, B4     | Various | Various | Background |

### Caching Strategies

```python
from google.appengine.api import memcache

# Set cache
memcache.set('user:123', user_data, time=3600)

# Get cache
user_data = memcache.get('user:123')
if user_data is None:
    user_data = get_user_from_db(123)
    memcache.set('user:123', user_data, time=3600)
```

## Security and Authentication

### Identity and Access Management

GAE integrates with Google Cloud IAM for access control:

```python
from google.appengine.api import users

# Check if user is logged in
current_user = users.get_current_user()
if current_user:
    user_email = current_user.email()

# Check if user is admin
is_admin = users.is_current_user_admin()
```

### Application Security

```yml
# app.yaml security configuration
handlers:
  - url: /admin/.*
    script: admin.app
    login: admin # Requires admin access
  - url: /profile/.*
    script: profile.app
    login: required # Requires any logged-in user
  - url: /public/.*
    script: public.app
    login: optional # Public access allowed
```

## Deployment and Operations

### Deployment Process

```bash
# Install Google Cloud SDK
# Authenticate
gcloud auth login
# Set project
gcloud config set project my-project-id
# Deploy application
gcloud app deploy
# View deployment
gcloud app browse
```

### Version Management

GAE supports multiple versions:

```bash
# Deploy new version
gcloud app deploy --version v2
# Set traffic splitting
gcloud app services set-traffic default \
    --splits v1=.5,v2=.5
```

### Monitoring and Logging

```python
import logging
from google.cloud import logging as cloud_logging

# Structured logging
client = cloud_logging.Client()
logger = client.logger('app-logger')
logger.log_text('User action completed', severity='INFO')
```

## Comparison with Other Cloud Platforms

| Feature           | Google App Engine | AWS Elastic Beanstalk | Azure App Service |
| ----------------- | ----------------- | --------------------- | ----------------- |
| Service Model     | PaaS              | PaaS                  | PaaS              |
| Automatic Scaling | Yes               | Yes                   | Yes               |
| Free Tier         | Generous          | Limited               | Limited           |
| Native Services   | Google Cloud      | AWS                   | Azure             |
| Deployment        | gcloud CLI        | EB CLI                | Azure CLI         |
| Custom Domains    | Yes               | Yes                   | Yes               |
| SSL Certificates  | Automatic         | Manual                | Automatic         |

## Exam Tips

1. **Understand the PaaS Model**: Remember that GAE abstracts infrastructure management, unlike IaaS solutions.
2. **Know the Scaling Options**: Be able to differentiate between automatic, manual, and basic scaling.
3. **Datastore vs SQL**: Understand when to use Datastore (NoSQL) vs Cloud SQL (relational).
4. **Security Configuration**: Remember how to configure access controls in app.yaml.
5. **Service Communication**: Know how microservices communicate within GAE.
6. **Cost Management**: Understand how instance classes and scaling affect costs.
7. **Development Workflow**: Be familiar with the local development server and deployment process.
