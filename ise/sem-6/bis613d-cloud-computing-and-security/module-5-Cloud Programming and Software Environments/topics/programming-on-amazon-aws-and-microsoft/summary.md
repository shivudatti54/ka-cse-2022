# Programming on Amazon AWS and Microsoft Azure

Cloud programming on AWS and Azure represents a fundamental shift from traditional development by leveraging managed services instead of managing physical infrastructure. This service-oriented and event-driven paradigm allows developers to focus on business logic while the platform handles provisioning, scaling, and maintenance through well-defined APIs and SDKs for languages like Python, JavaScript, Java, and .NET.

Core concepts include the shared responsibility model where providers secure infrastructure while customers secure data and applications; Infrastructure as Code (IaC) using CloudFormation (AWS) or ARM Templates/Bicep (Azure) for version-controlled, repeatable environments; and event-driven architecture where events like file uploads or scheduled times trigger code execution. Key AWS services include Lambda for serverless computing, S3 for object storage, DynamoDB for NoSQL, and API Gateway for RESTful APIs. Azure equivalents are Functions, Blob Storage, Cosmos DB, and API Management. Both platforms provide SDKs (Boto3 for AWS, Azure SDK) for programmatic service interaction.

## Key Takeaways

- Cloud programming is service-oriented and event-driven, focusing on business logic over infrastructure management
- Shared responsibility model: providers secure infrastructure, customers secure data and applications
- Infrastructure as Code enables version-controlled, repeatable environments via CloudFormation or ARM Templates
- AWS and Azure offer equivalent services with slight differences in integration and ecosystem strengths
