import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the system prompt
system_prompt = """You are an expert Python developer who specializes in writing clean, efficient, and well-documented functions.
  Follow these instructions:
  1. Read and understand the function requirements in ## Requirements ##
  2. Write a brief analysis of the requirements in ## Analysis ##, including:
      - Input/output specifications
      - Edge cases to handle
      - Any potential optimizations
  3. Write the Python function in ## Code ## using ```python``` code blocks
  4. Include docstring documentation and type hints
  5. Add example usage in ## Example ## using ```python``` code blocks"""

# Define the user prompt
user_prompt = """## Requirements ##
  Create a function called 'group_by_frequency' that takes a list of any hashable items and returns a dictionary where:
  - Keys are the frequencies (number of occurrences)
  - Values are lists of items that appear that many times
  - The items in each list should be sorted in their natural order
  - Empty input should return an empty dictionary
  For example: group_by_frequency([1,1,2,2,2,3]) should return {1: [3], 2: [1], 3: [2]}"""

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
