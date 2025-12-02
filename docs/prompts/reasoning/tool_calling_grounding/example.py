import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the system prompt
system_prompt = """You are an expert financial analyst who can use web search and code execution to analyze company performance.
  Use the available system tools to gather current financial information and perform analysis visualizations.
  Always cite your sources with URLs and publication dates when available."""

# Define the user prompt
user_prompt = """Analyze Amazon's financial performance for 2024. Focus on:
  - Revenue growth and quarterly trends
  - Profitability metrics (gross margin, operating margin)
  - Key financial ratios and comparisons to previous years
  - Stock performance and market sentiment
  
  Use web search to find the latest financial reports, earnings calls, and market data. Then use code interpreter to:
  - Extract and organize key financial metrics
  - Calculate growth rates and ratios
  - Create visualizations using matplotlib (charts, graphs, trend analysis)
  - Generate mermaid diagrams for process flows or organizational structures
  - Identify notable patterns or concerns
  
  Important: For all information gathered from web search, provide proper citations including:
  - Source URLs
  - Publication dates when available
  - Brief description of the source (e.g., "Amazon Q3 2024 Earnings Report")
  
  Provide analysis charts and actionable insights with all sources properly cited.
  
  Ask clarifying questions if needed.
  
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
