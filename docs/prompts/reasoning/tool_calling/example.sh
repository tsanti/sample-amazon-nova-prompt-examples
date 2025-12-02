#!/bin/bash

aws bedrock-runtime converse \
    --model-id amazon.nova-2-lite-v1:0 \
    --region us-west-2 \
    --messages '[
        {
            "role": "user",
            "content": [
                {
                    "text": "Analyze the sales performance for Q4 2024 and create a summary report with visualizations.\n\nThe sales database contains tables: orders, customers, products, and sales_reps.\nFocus on revenue trends, top-performing products, and regional performance."
                }
            ]
        }
    ]' \
    --system '[
        {
            "text": "You are an expert data analyst who can use available tools to analyze datasets and generate insights.\nUse the appropriate tools to complete the requested analysis efficiently and provide comprehensive results."
        }
    ]' \
    --tool-config '{
        "tools": [
            {
                "toolSpec": {
                    "name": "query_database",
                    "description": "Execute SQL queries against the sales database",
                    "inputSchema": {
                        "json": {
                            "type": "object",
                            "properties": {
                                "sql_query": {
                                    "type": "string",
                                    "description": "The SQL query to execute"
                                }
                            },
                            "required": ["sql_query"]
                        }
                    }
                }
            },
            {
                "toolSpec": {
                    "name": "create_chart",
                    "description": "Generate charts from data",
                    "inputSchema": {
                        "json": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "description": "The data to visualize"
                                },
                                "chart_type": {
                                    "type": "string",
                                    "enum": ["bar", "line", "pie", "scatter"],
                                    "description": "Type of chart to create"
                                }
                            },
                            "required": ["data", "chart_type"]
                        }
                    }
                }
            },
            {
                "toolSpec": {
                    "name": "calculate_statistics",
                    "description": "Calculate statistical measures",
                    "inputSchema": {
                        "json": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "description": "The data to analyze"
                                },
                                "metrics": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "enum": ["mean", "median", "growth_rate", "std_dev"]
                                    },
                                    "description": "Statistical metrics to calculate"
                                }
                            },
                            "required": ["data", "metrics"]
                        }
                    }
                }
            }
        ]
    }' \
    --additional-model-request-fields '{
        "reasoningConfig": {
            "type": "enabled",
            "maxReasoningEffort": "low"
        }
    }'
