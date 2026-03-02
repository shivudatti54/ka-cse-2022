# Google Cloud Platform (GCP) - Comprehensive Study Material

## Cloud Computing - BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction to Google Cloud Platform

### 1.1 What is Google Cloud Platform?

Google Cloud Platform (GCP) is a suite of cloud computing services offered by Google that runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search, YouTube, and Gmail. GCP provides a range of cloud services including computing, data storage, data analytics, machine learning, networking, and security.

### 1.2 Real-World Relevance

GCP is widely adopted across industries for various critical applications:

- **E-commerce**: Companies like Spotify, Twitter, and Snapchat rely on GCP for scalable infrastructure
- **Healthcare**: Genomics research and medical imaging analysis using BigQuery and AI tools
- **Financial Services**: Banking institutions use GCP for data analytics and fraud detection
- **Media & Entertainment**: Streaming platforms process and deliver content globally using GCP's global network

### 1.3 Delhi University Syllabus Context

This unit aligns with the Cloud Computing paper under the NEP 2024 UGCF curriculum, focusing on understanding cloud service providers, deployment models, and practical cloud application development. Students should be able to demonstrate proficiency in using major GCP services and understand how to architect cloud solutions.

---

## 2. GCP Architecture and Core Concepts

### 2.1 Global Infrastructure

GCP's infrastructure is organized hierarchically:

| Component | Description |
|-----------|-------------|
| **Zones** | Single failure domain containing discrete data centers |
| **Regions** | Geographical areas containing multiple zones |
| **Multi-regions** | Large geographical areas (US, EU, Asia) |
| **Edge Locations** | Points of presence for CDN and DNS |

### 2.2 Resource Hierarchy

```
Organization
    ↓
Folder
    ↓
Project
    ↓
Resources (Compute Engine, Storage, etc.)
```

- **Organization Node**: Top-level container for all resources
- **Folders**: Group projects and resources for hierarchical management
- **Projects**: Fundamental unit for organizing cloud resources
- **Resources**: Individual services like VMs, buckets, databases

---

## 3. Compute Services

### 3.1 Google Compute Engine (IaaS)

Compute Engine provides virtual machines (VMs) running in Google's data centers. It offers customizable compute capacity with flexible pricing options.

**Key Features:**
- Customizable machine types (CPU, memory)
- Persistent disks (SSD/HDD)
- Preemptible VMs (cost-effective, short-lived)
- Live migration for maintenance
- GPU support for ML workloads

**Example 1: Creating a VM Instance using gcloud CLI**

```bash
# Create a VM instance with custom specifications
gcloud compute instances create my-vm-instance \
    --zone=us-central1-a \
    --machine-type=e2-medium \
    --image-family=debian-11 \
    --image-project=debian-cloud \
    --boot-disk-size=20GB \
    --tags=http-server,https-server

# Allow HTTP and HTTPS traffic
gcloud compute firewall-rules create allow-http \
    --allow=tcp:80 \
    --target-tags=http-server

gcloud compute firewall-rules create allow-https \
    --allow=tcp:443 \
    --target-tags=https-server
```

### 3.2 Google App Engine (PaaS)

App Engine is a fully managed platform for building and hosting web applications. It automatically scales based on traffic.

**Environment Types:**
- **Standard Environment**: Free tier available, language-specific runtimes
- **Flexible Environment**: Docker containers, custom runtimes

```python
# app.yaml for Python Flask application on App Engine
runtime: python39
env: standard

entrypoint: gunicorn -b :$PORT main:app

handlers:
  - url: /
    script: auto
    secure: always

  - url: /api/.*
    script: auto
    secure: always
```

```python
# main.py - Simple Flask application
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Cloud Computing Course',
        'university': 'Delhi University',
        'platform': 'Google App Engine'
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```

### 3.3 Cloud Run (Serverless Containers)

Cloud Run is a fully managed container runtime that automatically scales from zero to handle requests. It abstracts away infrastructure management.

**Advantages:**
- Pay only for used resources
- Automatic scaling (scale to zero when idle)
- Supports any language/framework via containers
- Integration with Cloud Build and Artifact Registry

### 3.4 Google Kubernetes Engine (GKE)

GKE is a managed Kubernetes service for deploying containerized applications.

**Key Concepts:**
- **Pod**: Smallest deployable unit (one or more containers)
- **Node**: Virtual machine running Kubernetes
- **Cluster**: Group of nodes
- **Deployment**: Manages replica pods
- **Service**: Network abstraction for pods

```yaml
# deployment.yaml - Kubernetes deployment for a web application
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-web-app
  labels:
    app: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-container
        image: gcr.io/my-project/web-app:latest
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        env:
        - name: ENVIRONMENT
          value: "production"
---
apiVersion: v1
kind: Service
metadata:
  name: web-app-service
spec:
  selector:
    app: web-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
```

---

## 4. Storage Services

### 4.1 Cloud Storage

Cloud Storage is an object storage service for storing and retrieving any amount of data.

**Storage Classes:**

| Class | Use Case | Min Storage Duration |
|-------|----------|---------------------|
| **Standard** | Hot data, frequent access | None |
| **Nearline** | Monthly access | 30 days |
| **Coldline** | Quarterly access | 90 days |
| **Archive** | Annual access | 365 days |

**Operations with Cloud Storage:**

```bash
# Create a bucket
gsutil mb -l us-central1 gs://my-university-bucket-2024

# Copy file to bucket
gsutil cp lecture-notes.pdf gs://my-university-bucket-2024/

# Make bucket publicly readable
gsutil iam ch allUsers:objectViewer gs://my-university-bucket-2024

# Set lifecycle policy (move to Coldline after 1 year)
cat > lifecycle.json << EOF
{
  "rule": [
    {
      "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
      "condition": {"age": 365}
    }
  ]
}
EOF
gsutil lifecycle set lifecycle.json gs://my-university-bucket-2024

# Download file from bucket
gsutil cp gs://my-university-bucket-2024/lecture-notes.pdf ./
```

### 4.2 Cloud SQL

Cloud SQL is a fully managed relational database service supporting MySQL, PostgreSQL, and SQL Server.

**Features:**
- Automated backups
- High availability (failover replicas)
- Point-in-time recovery
- Automatic encryption
- Vertical and horizontal scaling

```bash
# Create a Cloud SQL instance (MySQL)
gcloud sql instances create my-database \
    --database-version=MYSQL_8_0 \
    --tier=db-f1-micro \
    --region=us-central1 \
    --root-password=securePassword123

# Create a database
gcloud sql databases create student_records \
    --instance=my-database

# Create user
gcloud sql users create dbadmin \
    --instance=my-database \
    --password=adminPass456
```

### 4.3 Firestore (NoSQL)

Firestore is a flexible, scalable NoSQL document database for mobile, web, and server development.

**Characteristics:**
- Document-based (collections → documents → fields)
- Real-time listeners
- Offline support
- Automatic scaling

---

## 5. Big Data and Analytics

### 5.1 BigQuery

BigQuery is a serverless, highly scalable, and cost-effective data warehouse designed for business analytics.

**Key Features:**
- SQL-like queries
- Petabyte-scale storage
- Real-time analytics
- Machine learning integration (BigQuery ML)

```sql
-- Example: Analyzing student performance data
-- Create a table from CSV data
CREATE TABLE IF NOT EXISTS university.student_scores (
    student_id STRING,
    student_name STRING,
    subject STRING,
    score INT64,
    semester STRING,
    timestamp TIMESTAMP
)
OPTIONS (
    description = "Student examination scores",
    labels = [("department", "computer_science")]
);

-- Query: Calculate average scores by subject
SELECT 
    subject,
    COUNT(*) as total_examinations,
    AVG(score) as average_score,
    MIN(score) as min_score,
    MAX(score) as max_score,
    PERCENTILE_CONT(score, 0.5) OVER (PARTITION BY subject) as median_score
FROM university.student_scores
WHERE semester = '2024-1'
GROUP BY subject
ORDER BY average_score DESC;

-- Query: Find students needing intervention (below passing threshold)
SELECT 
    student_id,
    student_name,
    subject,
    score,
    CASE 
        WHEN score < 40 THEN 'Fail - Immediate Action'
        WHEN score < 50 THEN 'Below Average - Monitor'
        WHEN score < 60 THEN 'Average - Encourage'
        ELSE 'Satisfactory'
    END as performance_category
FROM university.student_scores
WHERE score < 50
ORDER BY score ASC;
```

### 5.2 BigQuery ML (BML)

BigQuery ML enables users to create and execute machine learning models using SQL queries.

```sql
-- Example: Predict student performance based on study hours
-- Step 1: Create model
CREATE MODEL university.student_performance_model
OPTIONS (
    model_type = 'linear_reg',
    input_label_cols = ['predicted_score']
) AS
SELECT 
    study_hours,
    attendance_percentage,
    previous_score,
    score as predicted_score
FROM university.training_data;

-- Step 2: Make predictions
SELECT 
    student_id,
    predicted_score,
    confidence_interval(predicted_score, 0.95) as ci_95
FROM ML.PREDICT(
    MODEL university.student_performance_model,
    (SELECT 
        5 as study_hours,
        80 as attendance_percentage,
        65 as previous_score)
);
```

### 5.3 Dataflow

Dataflow is a fully managed service for executing data processing pipelines using Apache Beam.

### 5.4 Dataproc

Dataproc provides a managed Apache Hadoop, Spark, and Kafka environment for big data processing.

---

## 6. AI and Machine Learning Services

### 6.1 Vertex AI

Vertex AI is Google's unified machine learning platform for building, deploying, and scaling ML models.

**Components:**
- **Vertex AI Workbench**: Jupyter notebooks environment
- **AutoML**: Train models without coding
- **Custom Training**: Bring your own model
- **Model Registry**: Version and manage models
- **Vertex AI Prediction**: Deploy models for online/batch prediction

### 6.2 Pre-trained APIs

GCP offers pre-trained ML APIs:

| API | Use Case |
|-----|----------|
| **Vision API** | Image labeling, face detection, OCR |
| **Natural Language API** | Sentiment analysis, entity extraction |
| **Speech-to-Text** | Audio transcription |
| **Text-to-Speech** | Text to audio conversion |
| **Translation API** | Language translation |
| **Dialogflow** | Chatbots and conversational AI |

```python
# Example: Using Vision API for image analysis
from google.cloud import vision
from google.cloud.vision_v1 import types
import io

def analyze_image(image_path):
    """Analyze image using Google Cloud Vision API"""
    
    # Create client
    client = vision.ImageClient()
    
    # Load image
    with io.open(image_path, 'rb') as f:
        content = f.read()
    
    image = vision.Image(content=content)
    
    # Perform label detection
    label_response = client.label_detection(image=image)
    labels = label_response.label_annotations
    
    print("Image Labels:")
    for label in labels:
        print(f"  {label.description} (confidence: {label.score:.2f})")
    
    # Perform text detection (OCR)
    text_response = client.text_detection(image=image)
    texts = text_response.text_annotations
    
    if texts:
        print(f"\nDetected Text: {texts[0].description}")
    
    # Perform face detection
    face_response = client.face_detection(image=image)
    faces = face_response.face_annotations
    
    print(f"\nNumber of faces detected: {len(faces)}")

# Usage
analyze_image('lecture-hall-photo.jpg')
```

---

## 7. Networking Services

### 7.1 Virtual Private Cloud (VPC)

VPC provides networking functionality for GCP resources.

**Key Concepts:**
- **Subnets**: Regional IP address ranges
- **Firewall Rules**: Control traffic to/from instances
- **Routes**: Define paths for traffic
- **Load Balancers**: Distribute traffic across instances

### 7.2 Cloud Load Balancing

GCP offers various load balancers:

- **HTTP(S) Load Balancing**: Global, Layer 7
- **TCP/SSL Load Balancing**: Global, Layer 4
- **UDP Load Balancing**: Global
- **Internal Load Balancing**: Regional, internal traffic

### 7.3 Cloud CDN

Content Delivery Network for caching content at edge locations globally.

---

## 8. Security and Identity

### 8.1 Identity and Access Management (IAM)

IAM controls who can access what resources in GCP.

**Components:**
- **Principal**: Entity requesting access (user, service account, group)
- **Role**: Collection of permissions
- **Policy**: Binds principals to roles

**Role Types:**

| Type | Description |
|------|-------------|
| **Primitive** | Owner, Editor, Viewer (project-level) |
| **Predefined** | Granular, service-specific roles |
| **Custom** | User-defined roles |

```bash
# Create a service account
gcloud iam service-accounts create student-sa \
    --display-name="Student Service Account" \
    --description="Service account for student project"

# Grant specific roles
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:student-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/bigquery.dataViewer"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:student-sa@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.objectViewer"

# Generate key
gcloud iam service-accounts keys create key.json \
    --iam-account="student-sa@$PROJECT_ID.iam.gserviceaccount.com"
```

### 8.2 Cloud Key Management Service (KMS)

KMS manages cryptographic keys for data encryption.

---

## 9. DevOps and CI/CD

### 9.1 Cloud Build

Cloud Build executes builds on GCP infrastructure.

```yaml
# cloudbuild.yaml - CI/CD Pipeline
steps:
  # Build Docker image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/webapp:$COMMIT_SHA', '.']

  # Push to Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/webapp:$COMMIT_SHA']

  # Deploy to GKE
  - name: 'gcr.io/google-samples/hello-app'
    args: ['gcloud', 'container', 'clusters', 'get-credentials', 'my-cluster']
  
  - name: 'gcr.io/google-samples/hello-app'
    args: ['kubectl', 'set', 'image', 'deployment/web', 
           'web=gcr.io/$PROJECT_ID/webapp:$COMMIT_SHA']

images:
  - 'gcr.io/$PROJECT_ID/webapp:$COMMIT_SHA'
```

### 9.2 Cloud Deploy

Cloud Deploy is a managed delivery service for GKE and Cloud Run.

### 9.3 Artifact Registry

Artifact Registry stores, manages, and secures container images and language packages.

---

## 10. Key Takeaways

1. **GCP Infrastructure**: Understanding of global architecture (zones, regions, multi-regions) and resource hierarchy (Organization → Folder → Project → Resources)

2. **Compute Options**: Clear distinction between IaaS (Compute Engine), PaaS (App Engine), Serverless (Cloud Run), and Container Orchestration (GKE)

3. **Storage Solutions**: Cloud Storage for object storage with lifecycle management, Cloud SQL for relational databases, and Firestore for NoSQL

4. **Big Data Analytics**: BigQuery as enterprise data warehouse with SQL support and BigQuery ML for predictive analytics

5. **AI/ML Services**: Vertex AI platform and pre-trained APIs for adding intelligence to applications

6. **Security**: IAM for access control, principle of least privilege, and proper service account management

7. **DevOps**: Cloud Build for CI/CD pipelines and Artifact Registry for artifact management

---

## 11. Assessment Questions

### Multiple Choice Questions

**Level 1: Basic**

1. Which GCP service provides virtual machines in the cloud?
   - [ ] App Engine
   - [ ] Cloud Run
   - [x] Compute Engine
   - [ ] Cloud Functions

2. What is the minimum storage duration for Cloud Storage Coldline class?
   - [ ] 30 days
   - [x] 90 days
   - [ ] 180 days
   - [ ] 365 days

**Level 2: Intermediate**

3. Which BigQuery feature allows creating ML models using SQL?
   - [ ] TensorFlow Integration
   - [x] BigQuery ML
   - [ ] AutoML Tables
   - [ ] Vertex AI

4. In Kubernetes, what is the smallest deployable unit?
   - [ ] Node
   - [x] Pod
   - [ ] Cluster
   - [ ] Deployment

**Level 3: Advanced**

5. Which IAM role type provides the finest-grained permissions?
   - [ ] Primitive Roles
   - [ ] Predefined Roles
   - [x] Custom Roles
   - [ ] Default Roles

6. What GCP service would you use for processing data streams in real-time?
   - [ ] Dataproc
   - [ ] Dataflow
   - [x] Both Dataflow and Pub/Sub
   - [ ] BigQuery

### Short Answer Questions

1. Explain the difference between Cloud Run and Google App Engine.
2. How does BigQuery achieve high query performance at scale?
3. What are the benefits of using GKE over self-managed Kubernetes?
4. Describe the resource hierarchy in GCP.
5. How would you secure a Cloud Storage bucket containing sensitive university records?

### Practical Questions

1. Write a gcloud command to create a Compute Engine instance with 4 vCPUs and 8GB RAM in the asia-south1 region.
2. Create a Cloud Storage lifecycle policy to move objects to Archive storage after 2 years.
3. Write a SQL query in BigQuery to find the top 5 students by average score across all subjects.
4. Create a simple Kubernetes deployment YAML for a Flask application with 3 replicas.

---

## 12. References and Further Reading

- Google Cloud Documentation: https://cloud.google.com/docs
- Qwiklabs GCP Labs: https://www.qwiklabs.com
- Google Cloud Skills Boost: https://www.cloudskillsboost.google
- Delhi University Cloud Computing Syllabus (NEP 2024)

---

*Material prepared for BSc (Hons) Computer Science, Delhi University - NEP 2024 UGCF*