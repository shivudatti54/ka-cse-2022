# Application Deployment in PaaS

## Deployment Models

### 1. Git-based Deployment

- Push code to Git repository
- Platform automatically builds and deploys
- Examples: Heroku, Render, Railway

### 2. Container-based Deployment

- Push Docker images
- Platform runs containers
- Examples: Google Cloud Run, Azure Container Apps

### 3. Source Code Upload

- Upload code archive (ZIP)
- Platform builds from source
- Examples: AWS Elastic Beanstalk, Azure App Service

## Deployment Workflow

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Code    │───>│  Build   │───>│  Test    │───>│  Deploy  │
│  Commit  │    │  Stage   │    │  Stage   │    │  Stage   │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     │               │               │               │
     v               v               v               v
  Git Push      Compile/        Run Tests      Deploy to
               Build Image                     Production
```

## Deployment Strategies

| Strategy   | Description                     | Downtime | Risk   |
| ---------- | ------------------------------- | -------- | ------ |
| Rolling    | Gradually replace instances     | None     | Low    |
| Blue-Green | Switch between two environments | None     | Medium |
| Canary     | Route small % to new version    | None     | Lowest |
| Recreate   | Stop old, start new             | Yes      | High   |

### Blue-Green Deployment

```
        Load Balancer
              │
     ┌────────┴────────┐
     │                 │
┌────▼────┐       ┌────▼────┐
│  Blue   │       │  Green  │
│(Current)│       │  (New)  │
└─────────┘       └─────────┘
     │                 │
     └────────┬────────┘
              │
        After testing,
        switch traffic
```

### Canary Deployment

```
        Load Balancer
              │
     ┌────────┴────────┐
     │                 │
     ▼                 ▼
   95%               5%
┌────────┐       ┌────────┐
│ Stable │       │ Canary │
│ v1.0   │       │ v1.1   │
└────────┘       └────────┘
```

## CI/CD Integration

### Continuous Integration

- Automated builds on code push
- Run unit tests
- Static code analysis
- Generate build artifacts

### Continuous Deployment

- Automated deployment to staging/production
- Integration tests
- Automatic rollback on failure
- Release approvals

## Configuration Management

### Environment Variables

```bash
# Set via CLI
heroku config:set API_KEY=secret123

# Or via platform UI
# Most PaaS platforms support environment variables
```

### Secrets Management

- Never commit secrets to code
- Use platform's secrets manager
- Inject at runtime via environment variables

## Buildpacks

Buildpacks automatically detect and build your application:

| Language | Buildpack Detects         |
| -------- | ------------------------- |
| Python   | requirements.txt, Pipfile |
| Node.js  | package.json              |
| Java     | pom.xml, build.gradle     |
| Ruby     | Gemfile                   |
| Go       | go.mod                    |

## Health Checks

```
# Liveness Probe
GET /health → 200 OK

# Readiness Probe
GET /ready → 200 OK (when ready to receive traffic)
```

## Scaling

### Horizontal Scaling

- Add more instances
- Load balancer distributes traffic
- Automatic based on metrics (CPU, memory, requests)

### Vertical Scaling

- Increase instance size
- More CPU/memory per instance
- May require restart

## Best Practices

1. **Use Environment Variables**: Never hardcode configuration
2. **Implement Health Checks**: Enable proper load balancing
3. **Use Rolling Deployments**: Minimize downtime
4. **Enable Auto-scaling**: Handle traffic spikes
5. **Implement CI/CD**: Automate testing and deployment
6. **Monitor Everything**: Logs, metrics, traces

> **Exam Tip**: Understand different deployment strategies and when to use each. Blue-green for instant rollback, canary for risk mitigation.
