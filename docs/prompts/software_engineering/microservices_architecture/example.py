import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the system prompt
system_prompt = """You are an expert microservices architect who specializes in distributed system design and implementation.
  Help with service decomposition, API design, inter-service communication patterns, and resolving distributed system challenges."""

# Define the user prompt
user_prompt = """## Current Architecture ##
  We have an e-commerce platform with these services:
  
  **User Service** (Node.js/Express)
  - Manages user accounts, authentication
  - Database: PostgreSQL
  - Endpoints: /users, /auth/login, /auth/register
  
  **Product Service** (Java/Spring Boot)
  - Product catalog, inventory management
  - Database: MongoDB
  - Endpoints: /products, /inventory
  
  **Order Service** (Python/FastAPI)
  - Order processing, payment integration
  - Database: PostgreSQL
  - Endpoints: /orders, /payments
  
  **Notification Service** (Node.js)
  - Email/SMS notifications
  - Message Queue: RabbitMQ
  
  Current flow: User → Order Service → Product Service (inventory check) → Payment Gateway → Notification Service
  
  ## Challenge ##
  We're experiencing several issues:
  1. Order Service frequently times out when checking inventory during high traffic
  2. Failed payments leave inventory in inconsistent state
  3. Users don't get real-time updates on order status
  4. System becomes unavailable when Product Service goes down
  5. Notification delivery is unreliable during peak hours
  
  We need to redesign this to be more resilient, scalable, and provide better user experience. Consider patterns like circuit breakers, event sourcing, and real-time updates.
  
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
            "maxReasoningEffort": "high"
        }
    }
}

# Make the API call
response = bedrock_runtime.converse(
    modelId="amazon.nova-2-lite-v1:0",
    **request_body
)

# Print the response
print(json.dumps(response, indent=2, default=str))
