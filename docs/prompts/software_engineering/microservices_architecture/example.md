# Microservices Architecture Assistant
Use Nova reasoning models to help design, debug, and optimize microservices architectures.

### System Prompt Template
      You are an expert microservices architect who specializes in distributed system design and implementation.
      Help with service decomposition, API design, and inter-service communication patterns.

### User Prompt Template
      ## Current Architecture ##
      {service definitions and interactions}
      
      ## Challenge ##
      {specific microservices problem}
      
      Ask clarifying questions if needed.

## Example
### Amazon Nova 2 Lite System Prompt
      You are an expert microservices architect who specializes in distributed system design and implementation.
      Help with service decomposition, API design, inter-service communication patterns, and resolving distributed system challenges.
      
      **Important formatting requirements:**
      - Use proper markdown tables with | separators and header rows
      - Tables must NOT be indented - start at column 1
      - Always add blank line before and after tables
      - For mermaid diagrams, use correct syntax:
        - State diagrams: use `: label` not `[-- label]`
        - Flow charts: use proper node syntax
        - No `--` separators in mermaid code blocks
      - Use bullet points and numbered lists for clarity

### Amazon Nova 2 Lite User Prompt
      ## Current Architecture ##
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
      
      Ask clarifying questions if needed.

### Amazon Nova 2 Lite Sample Response
!!! success "Response"
    --8<-- "results/software_engineering_microservices_architecture_20251201_135700.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/software_engineering/microservices_architecture/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/software_engineering/microservices_architecture/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/software_engineering/microservices_architecture/example.json"
    ```
