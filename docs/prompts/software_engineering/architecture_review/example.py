import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the system prompt
system_prompt = """You are an expert software architect who specializes in large-scale distributed systems and microservices architecture.
Evaluate architectural decisions considering performance implications, security vulnerabilities, maintainability challenges, scalability constraints, and long-term technical debt across complex enterprise systems with millions of users.

**Important formatting requirements:**
- Use proper markdown tables with | separators and header rows
- Format all tables as: | Column 1 | Column 2 | with |---|---| separator
- Use bullet points and numbered lists for clarity
- Include mermaid diagrams when helpful for visualization"""

# Define the user prompt
user_prompt = """## System Architecture ##

**Current Monolithic E-commerce Platform (500K LOC)**

```python
# Core monolith structure
ecommerce_platform/
├── user_management/     # 50K LOC - User auth, profiles, preferences
│  ├── authentication.py   # OAuth2, JWT, session management
│  ├── user_profiles.py   # Profile CRUD, preferences, settings
│  └── permissions.py    # RBAC, admin controls
├── product_catalog/     # 80K LOC - Product data, search, recommendations
│  ├── product_models.py   # Complex product hierarchy, variants
│  ├── search_engine.py   # Elasticsearch integration, faceted search
│  ├── recommendations.py  # ML-based product recommendations
│  └── inventory.py     # Real-time inventory tracking
├── order_processing/     # 120K LOC - Cart, checkout, fulfillment
│  ├── shopping_cart.py   # Session-based cart, persistence
│  ├── checkout.py      # Multi-step checkout, validation
│  ├── payment_processing.py # Multiple payment gateways, PCI compliance
│  ├── order_fulfillment.py # Warehouse integration, shipping
│  └── returns.py      # Return processing, refunds
├── customer_service/     # 60K LOC - Support, chat, tickets
│  ├── support_tickets.py  # Ticket management, SLA tracking
│  ├── live_chat.py     # Real-time chat, agent routing
│  └── knowledge_base.py   # FAQ, documentation system
├── analytics/        # 90K LOC - Reporting, BI, ML pipelines
│  ├── event_tracking.py   # User behavior tracking, analytics
│  ├── reporting.py     # Business intelligence, dashboards
│  └── ml_pipelines.py    # Recommendation training, A/B testing
└── shared/          # 100K LOC - Common utilities, integrations
  ├── database.py      # ORM, connection pooling, migrations
  ├── caching.py      # Redis, memcached, cache strategies
  ├── messaging.py     # RabbitMQ, event publishing
  └── external_apis.py   # Payment, shipping, tax integrations
  ```

**Current Performance Metrics**
- Response time: 200ms (p50), 800ms (p95), 2.5s (p99)
- Throughput: 5,000 requests/minute peak
- Database: PostgreSQL, 2TB data, 500 concurrent connections
- Infrastructure: 12 application servers, 3 database replicas
- Deployment: 45-minute deployments, 2-week release cycles
- Incidents: 15 production issues/month, 99.2% uptime

**Scaling Challenges**
- Database bottlenecks during flash sales (10x traffic spikes)
- Memory usage: 8GB per app server, frequent GC pauses
- Code coupling: Changes in one module often break others
- Testing: 6-hour test suite, flaky integration tests
- Team coordination: 25 developers, merge conflicts, blocking dependencies

**Business Requirements**
- Scale to 50,000 requests/minute (10x current)
- Support international expansion (5 new countries)
- Reduce deployment time to <10 minutes
- Improve developer velocity (faster feature delivery)
- Achieve 99.9% uptime SLA
- Support real-time features (live inventory, chat)

**Technology Constraints**
- Must maintain PCI DSS compliance
- Legacy integrations with 15 external systems
- Existing PostgreSQL data (complex migration)
- Team expertise: Strong Python, limited microservices experience
- Budget: $2M for infrastructure changes over 18 months

## Architecture Challenge ##

Evaluate whether TechFlow should migrate from their monolithic architecture to microservices, and if so, design the optimal migration strategy.

Provide architectural analysis covering:

1. **System-Wide Impact Assessment**: Analyze how microservices migration would affect each component. Consider data consistency requirements, transaction boundaries, and inter-service communication patterns. Identify which modules are good candidates for extraction and which should remain coupled.

2. **Performance Implications Analysis**: Model the performance impact of network latency, service-to-service calls, and distributed transactions. Compare current monolith performance with projected microservices performance under various load scenarios. Consider caching strategies, data locality, and query optimization.

3. **Security Architecture Review**: Evaluate security implications of distributed architecture. Analyze authentication/authorization across services, network security, data encryption in transit/at rest, and compliance requirements (PCI DSS). Identify new attack vectors and mitigation strategies.

4. **Dependency and Data Flow Analysis**: Map current tight coupling and shared database dependencies. Design service boundaries that minimize cross-service transactions. Analyze data consistency requirements and propose eventual consistency vs strong consistency trade-offs.

5. **Migration Strategy & Risk Assessment**: Design a phased migration approach that minimizes business disruption. Identify the optimal order for service extraction, considering dependencies and risk levels. Propose strangler fig pattern implementation with specific timelines and rollback strategies.

6. **Operational Complexity Evaluation**: Assess the operational overhead of managing 15-20 microservices vs 1 monolith. Consider monitoring, logging, debugging, deployment pipelines, and team structure changes. Evaluate DevOps tooling requirements and learning curve.

7. **Alternative Architecture Recommendations**: If microservices aren't optimal, propose alternative approaches (modular monolith, service-oriented architecture, domain-driven design within monolith). Compare trade-offs and provide decision framework.

Consider the team's current expertise, budget constraints, and business timeline. Provide specific recommendations for technology choices, infrastructure requirements, and organizational changes needed for success.

Ask clarifying questions if needed."""

# Prepare the request
request_body = {
    "system": [
        {
            "text": system_prompt
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": user_prompt
                }
            ]
        }
    ],
    "toolConfig": {
        "tools": [
            {
                "systemTool": {
                    "name": "nova_grounding"
                }
            },
            {
                "systemTool": {
                    "name": "nova_code_interpreter"
                }
            }
        ]
    },
    "additionalModelRequestFields": {
        "reasoningConfig": {
            "type": "enabled",
            "maxReasoningEffort": "low"
        }
    },
    "inferenceConfig": {
        "temperature": 0.3,
        "topP": 0.9,
        "maxTokens": 10000
    }
}

# Make the API call
response = bedrock_runtime.converse(
    modelId="amazon.nova-2-lite-v1:0",
    **request_body
)

# Print the response
print(json.dumps(response, indent=2, default=str))
