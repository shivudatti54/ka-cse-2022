# What is Cloud Computing?

## Definition

Cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet ("the cloud") to offer faster innovation, flexible resources, and economies of scale.

## NIST Definition

According to the National Institute of Standards and Technology (NIST):

> "Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources that can be rapidly provisioned and released with minimal management effort or service provider interaction."

## Core Concept Visualization

```
Traditional Computing vs Cloud Computing:

┌─────────────────────────────────────────────────────────────────┐
│                    TRADITIONAL COMPUTING                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐            │
│  │ Server  │  │ Server  │  │ Server  │  │ Server  │            │
│  │   #1    │  │   #2    │  │   #3    │  │   #4    │            │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘            │
│       │            │            │            │                   │
│  ┌────┴────────────┴────────────┴────────────┴────┐            │
│  │           Your Data Center (Own & Manage)      │            │
│  └────────────────────────────────────────────────┘            │
│  - High upfront costs                                           │
│  - Maintenance responsibility                                   │
│  - Fixed capacity                                               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      CLOUD COMPUTING                             │
├─────────────────────────────────────────────────────────────────┤
│                         ☁️ CLOUD ☁️                              │
│  ┌─────────────────────────────────────────────────────┐        │
│  │   ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐  │        │
│  │   │VM │ │VM │ │VM │ │VM │ │VM │ │VM │ │VM │ │VM │  │        │
│  │   └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘  │        │
│  │         Provider's Data Center (Managed for you)    │        │
│  └─────────────────────────────────────────────────────┘        │
│       ↑           ↑           ↑           ↑                     │
│   ┌───┴───┐   ┌───┴───┐   ┌───┴───┐   ┌───┴───┐                │
│   │User A │   │User B │   │User C │   │User D │                │
│   └───────┘   └───────┘   └───────┘   └───────┘                │
│  - Pay-as-you-go                                                │
│  - Provider manages infrastructure                              │
│  - Elastic capacity                                             │
└─────────────────────────────────────────────────────────────────┘
```

## Service Models

| Model | Full Name                   | What You Manage                     | What Provider Manages                            | Example                       |
| ----- | --------------------------- | ----------------------------------- | ------------------------------------------------ | ----------------------------- |
| IaaS  | Infrastructure as a Service | Apps, Data, Runtime, Middleware, OS | Virtualization, Servers, Storage, Networking     | AWS EC2, Azure VMs            |
| PaaS  | Platform as a Service       | Apps, Data                          | Runtime, Middleware, OS, Virtualization, Servers | Heroku, Google App Engine     |
| SaaS  | Software as a Service       | Nothing (just use it)               | Everything                                       | Gmail, Salesforce, Office 365 |

## The Pizza Analogy

```
┌────────────────────────────────────────────────────────────────┐
│                    THE PIZZA ANALOGY                            │
├──────────────┬──────────────┬──────────────┬──────────────────┤
│  ON-PREMISE  │    IaaS      │    PaaS      │      SaaS        │
│  (Make at    │  (Take &     │  (Pizza      │   (Dine at       │
│   home)      │   Bake)      │  Delivered)  │   Restaurant)    │
├──────────────┼──────────────┼──────────────┼──────────────────┤
│ ■ Dining     │ ■ Dining     │ ■ Dining     │ □ Dining Table   │
│   Table      │   Table      │   Table      │                  │
│ ■ Plates     │ ■ Plates     │ ■ Plates     │ □ Plates         │
│ ■ Oven       │ ■ Oven       │ □ Oven       │ □ Oven           │
│ ■ Dough      │ □ Dough      │ □ Dough      │ □ Dough          │
│ ■ Toppings   │ □ Toppings   │ □ Toppings   │ □ Toppings       │
│ ■ Cheese     │ □ Cheese     │ □ Cheese     │ □ Cheese         │
├──────────────┴──────────────┴──────────────┴──────────────────┤
│ ■ = You provide    □ = Someone else provides                   │
└────────────────────────────────────────────────────────────────┘
```

## Key Components of Cloud Computing

1. **Front End**: Client-side interface (browser, application, mobile app)
2. **Back End**: Cloud infrastructure (servers, storage, databases)
3. **Network**: Internet connection between front and back end
4. **Cloud-Based Delivery**: The mechanism to deliver services

## Simple Example: Email Service

```python
# Traditional Approach
# - Buy mail server hardware
# - Install mail server software
# - Configure DNS, security
# - Maintain 24/7

# Cloud Approach (Using Gmail API)
from googleapiclient.discovery import build

service = build('gmail', 'v1', credentials=creds)
message = create_message('sender@gmail.com', 'recipient@gmail.com',
                         'Subject', 'Body')
send_message(service, 'me', message)
# Google handles all infrastructure!
```

> **Exam Tip**: Remember the NIST definition and the three service models (IaaS, PaaS, SaaS). The pizza analogy helps distinguish them.
