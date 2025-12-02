import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the system prompt
system_prompt = """You are an expert software engineer who analyzes application logs to diagnose issues and provide solutions.
  Use the provided log data to answer questions thoroughly and cite relevant information from the logs."""

# Define the user prompt
user_prompt = """## Context ##
  **Application Debug Logs - E-commerce Checkout Flow**
  
  ```
  2024-11-22 10:15:23 [INFO] User session started: user_id=12345, session_id=abc-def-789
  2024-11-22 10:15:24 [INFO] User navigated to product page: product_id=SKU-001, category=electronics
  2024-11-22 10:15:45 [INFO] Product added to cart: product_id=SKU-001, quantity=2, price=299.99
  2024-11-22 10:16:12 [INFO] User navigated to cart page
  2024-11-22 10:16:15 [INFO] Cart validation successful: total_items=2, subtotal=599.98
  2024-11-22 10:16:18 [INFO] User clicked checkout button
  2024-11-22 10:16:19 [INFO] Checkout process initiated: user_id=12345
  2024-11-22 10:16:20 [INFO] Loading shipping addresses for user_id=12345
  2024-11-22 10:16:21 [INFO] Found 2 saved addresses for user
  2024-11-22 10:16:25 [INFO] User selected shipping address: address_id=addr_456
  2024-11-22 10:16:30 [INFO] Calculating shipping costs for zip_code=90210
  2024-11-22 10:16:31 [INFO] Shipping cost calculated: standard=$9.99, express=$19.99
  2024-11-22 10:16:35 [INFO] User selected standard shipping
  2024-11-22 10:16:40 [INFO] Proceeding to payment step
  2024-11-22 10:16:41 [INFO] Loading saved payment methods for user_id=12345
  2024-11-22 10:16:42 [WARN] No saved payment methods found for user
  2024-11-22 10:16:45 [INFO] User entered new credit card details
  2024-11-22 10:16:46 [INFO] Validating credit card number: ****1234
  2024-11-22 10:16:47 [ERROR] Credit card validation failed: invalid_luhn_checksum
  2024-11-22 10:16:47 [INFO] Displaying error message to user: "Please check your card number"
  2024-11-22 10:17:02 [INFO] User re-entered credit card details
  2024-11-22 10:17:03 [INFO] Validating credit card number: ****5678
  2024-11-22 10:17:04 [INFO] Credit card validation successful
  2024-11-22 10:17:05 [INFO] Validating expiration date: 12/2027
  2024-11-22 10:17:06 [INFO] Expiration date validation successful
  2024-11-22 10:17:07 [INFO] Validating CVV code
  2024-11-22 10:17:08 [INFO] CVV validation successful
  2024-11-22 10:17:10 [INFO] Processing payment authorization
  2024-11-22 10:17:12 [INFO] Contacting payment gateway: gateway=stripe
  2024-11-22 10:17:15 [INFO] Payment gateway response: status=success, auth_code=AUTH123456
  2024-11-22 10:17:16 [INFO] Payment authorized successfully: amount=$609.97
  2024-11-22 10:17:17 [INFO] Creating order record in database
  2024-11-22 10:17:18 [INFO] Order created: order_id=ORD-789123, status=confirmed
  2024-11-22 10:17:19 [INFO] Sending confirmation email to: user@example.com
  2024-11-22 10:17:20 [INFO] Email sent successfully
  2024-11-22 10:17:21 [INFO] Clearing user cart
  2024-11-22 10:17:22 [INFO] Cart cleared successfully
  2024-11-22 10:17:23 [INFO] Redirecting user to order confirmation page
  2024-11-22 10:17:24 [INFO] Order confirmation page loaded: order_id=ORD-789123
  ```
  
  ## Question ##
  The user reported that their checkout process failed and they couldn't complete their purchase. Based on these logs, what actually happened during their checkout experience? Was there really a failure, and if so, what caused it and how was it resolved?
  
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
