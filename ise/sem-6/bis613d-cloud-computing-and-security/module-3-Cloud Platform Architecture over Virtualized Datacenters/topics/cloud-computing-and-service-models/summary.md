# Cloud Computing and Service Models

## Overview

Cloud computing is a paradigm shift delivering computing resources (servers, storage, applications) as on-demand services from cloud providers like AWS, Azure, and GCP. According to NIST, it enables ubiquitous, on-demand network access to a shared pool of configurable resources that can be rapidly provisioned with minimal management effort.

## Key Points

- **On-Demand Self-Service**: Consumers can unilaterally provision computing capabilities automatically without human interaction with service providers
- **Broad Network Access**: Capabilities available over the network through standard mechanisms (mobile phones, tablets, laptops, workstations)
- **Resource Pooling**: Provider's computing resources pooled to serve multiple consumers using multi-tenant model with dynamic resource assignment
- **Rapid Elasticity**: Capabilities can be elastically provisioned and released automatically to scale rapidly based on demand
- **Measured Service**: Cloud systems automatically control and optimize resource use through metering capabilities at appropriate abstraction levels
- **IaaS (Infrastructure as a Service)**: Provides virtualized computing resources (VMs, storage, networks); user manages OS, runtime, applications; examples: Amazon EC2, Azure VMs, Google Compute Engine
- **PaaS (Platform as a Service)**: Provides development and deployment environments; user manages only applications and data; examples: Google App Engine, Heroku, AWS Elastic Beanstalk
- **SaaS (Software as a Service)**: Delivers complete applications over internet; provider manages everything; examples: Gmail, Microsoft Office 365, Salesforce, Slack

## Important Concepts

- Deployment models: Public Cloud (third-party providers), Private Cloud (single organization), Hybrid Cloud (combination), Community Cloud (shared by specific community)
- Evolving service models: FaaS/Serverless (AWS Lambda, Azure Functions), DBaaS (Amazon RDS), CaaS (Google Kubernetes Engine)
- IaaS provides maximum control with highest management responsibility; SaaS provides minimum control with lowest management responsibility
- Service model selection depends on business and technical requirements: IaaS for full control, PaaS for developer productivity, SaaS for ready-made applications

## Notes

- Memorize NIST's five essential characteristics - commonly tested in short-answer questions
- Focus on understanding what user manages vs. what provider manages in each service model
- Be prepared to match cloud services (EC2, GAE, Salesforce) to their correct service model with explanations
- Draw the service model stack diagram from memory showing the responsibility boundaries
- Understand newer models like FaaS/Serverless and how they differ from traditional PaaS
