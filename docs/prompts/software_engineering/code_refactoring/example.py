import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

# Define the system prompt
system_prompt = """You are an expert full-stack developer who specializes in React and Node.js applications.
  Help with refactoring, debugging, and implementing new features by analyzing the codebase and providing comprehensive solutions."""

# Define the user prompt
user_prompt = """## Codebase Context ##
  ```javascript
  // components/UserProfile.jsx
  import React, { useState, useEffect } from 'react';
  import { fetchUserData, updateUserProfile } from '../api/userService';
  
  const UserProfile = ({ userId }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [editing, setEditing] = useState(false);
    
    useEffect(() => {
      fetchUserData(userId).then(userData => {
        setUser(userData);
        setLoading(false);
      });
    }, [userId]);
    
    const handleSave = async (updatedData) => {
      await updateUserProfile(userId, updatedData);
      setUser(updatedData);
      setEditing(false);
    };
    
    if (loading) return <div>Loading...</div>;
    
    return (
      <div className="user-profile">
        {editing ? (
          <EditForm user={user} onSave={handleSave} />
        ) : (
          <ProfileView user={user} onEdit={() => setEditing(true)} />
        )}
      </div>
    );
  };
  ```
  
  ```javascript
  // api/userService.js
  const API_BASE = 'https://api.example.com';
  
  export const fetchUserData = async (userId) => {
    const response = await fetch(`${API_BASE}/users/${userId}`);
    return response.json();
  };
  
  export const updateUserProfile = async (userId, data) => {
    const response = await fetch(`${API_BASE}/users/${userId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    return response.json();
  };
  ```
  
  ## Task ##
  Add error handling, loading states for save operations, and implement optimistic updates for better UX. Also add proper TypeScript types and make the component more robust.
  
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
