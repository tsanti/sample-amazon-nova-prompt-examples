# Software Engineering - Code Refactoring
Use Nova reasoning models to assist with complex software development tasks in IDE environments like Kiro, Cline, or Roo.

### System Prompt Template
      You are an expert software engineer who specializes in {language/framework}.
      Help with {specific development task} by analyzing the codebase and providing solutions.

### User Prompt Template

      ## Codebase Context ##
      {relevant code or files}
      
      ## Task ##
      {specific development request}
      
      Ask clarifying questions if needed.

## Example
### Amazon Nova 2 Lite System Prompt
      You are an expert full-stack developer who specializes in React and Node.js applications.
      Help with refactoring, debugging, and implementing new features by analyzing the codebase and providing comprehensive solutions.

### Amazon Nova 2 Lite User Prompt
There are many different ways to pass the code to the model for our example we will simply pass our code in the prompt as a fenced code block. 

      ## Codebase Context ##
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
      
      Ask clarifying questions if needed.

### Amazon Nova 2 Lite Sample Response
!!! success "Response"
    --8<-- "results/software_engineering_code_refactoring_20251201_133257.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/software_engineering/code_refactoring/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/software_engineering/code_refactoring/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/software_engineering/code_refactoring/example.json"
    ```
