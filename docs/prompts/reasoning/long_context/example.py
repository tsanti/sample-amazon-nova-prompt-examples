import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the system prompt
system_prompt = """You are an expert {domain} assistant. Answer the question being asked using only the document text provided. Follow these instructions:

  1. The full case name in italics (e.g., Skilling v. United States).
  2. A citation with the volume number, reporter abbreviation, first page of the case, and pin-point page if applicable (e.g., 561 U.S. 358).
  3. The court that decided the case and the year of the decision in parentheses (e.g., (U.S. Supreme Court 2010)).
  4. A concise summary of the court's holding or legal conclusion relevant to the question.
  5. Any important legal principles or precedents established by the case.
  6. Optionally, a brief contextual or procedural background if relevant."""

# Define the user prompt
user_prompt = """Document text:
  
  1 Lead Plaintiff states that its motion is based on prior
  pleadings that it filed in support of its motion for preliminary
  approval of the Plan (#5755, 5756), on the briefing in connection
  with Lead Plaintiff’s responses to objections to preliminary
  approval of the Plan (#5773, 5774, 5775, and 5776), and on the
  first Declaration of Professor Roman L. Weil (expert on plan
  allocation 
  and 
  securities 
  violation 
  damages)(#5794), 
  
  [Full document content continues...]"""

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
