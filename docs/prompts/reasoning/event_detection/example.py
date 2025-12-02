import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the system prompt
system_prompt = """You are an expert cybersecurity analyst who specializes in detecting and analyzing security incidents from system logs.
  Identify relevant security events from the provided log data and provide detailed threat analysis with recommended actions."""

# Define the user prompt
user_prompt = """## Data ##
  ```
  2024-03-19 14:23:15 [INFO] User john.doe@company.com logged in from IP 192.168.1.100
  2024-03-19 14:23:45 [INFO] File access: /home/john.doe/documents/project_alpha.pdf
  2024-03-19 14:24:12 [WARN] Failed login attempt for admin@company.com from IP 203.0.113.45
  2024-03-19 14:24:18 [WARN] Failed login attempt for admin@company.com from IP 203.0.113.45
  2024-03-19 14:24:25 [WARN] Failed login attempt for admin@company.com from IP 203.0.113.45
  2024-03-19 14:24:31 [ERROR] Account locked: admin@company.com
  2024-03-19 14:25:02 [INFO] User sarah.smith@company.com logged in from IP 10.0.0.50
  2024-03-19 14:25:15 [INFO] Database query executed: SELECT * FROM customer_data WHERE ssn IS NOT NULL
  2024-03-19 14:25:22 [WARN] Large data export initiated by sarah.smith@company.com (50,000 records)
  2024-03-19 14:26:45 [INFO] VPN connection established from IP 198.51.100.75 for user mike.wilson@company.com
  2024-03-19 14:27:12 [WARN] Unusual file access pattern detected for user mike.wilson@company.com
  2024-03-19 14:27:30 [ERROR] Antivirus alert: Suspicious file detected in /tmp/update.exe
  2024-03-19 14:28:01 [WARN] Multiple failed SSH attempts from IP 198.51.100.75
  2024-03-19 14:28:15 [INFO] System backup initiated by scheduled task
  2024-03-19 14:29:33 [ERROR] Network anomaly detected: Unusual outbound traffic to IP 185.220.101.42
  ```
  
  ## Detection Criteria ##
  Identify and analyze:
  - Brute force attacks
  - Insider threat indicators
  - Malware/suspicious file activity
  - Data exfiltration attempts
  - Network anomalies
  - Account compromise indicators
  
  For each detected event, provide:
  - Event classification and severity
  - Timeline and affected systems/users
  - Potential impact assessment
  - Recommended immediate actions
  - Investigation priorities
  
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
