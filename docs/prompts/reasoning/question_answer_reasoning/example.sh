#!/bin/bash

aws bedrock-runtime converse \
    --model-id amazon.nova-2-lite-v1:0 \
    --region us-west-2 \
    --messages file://messages.json \
    --system '[{"text": "You are an expert software engineer who analyzes application logs to diagnose issues and provide solutions. Use the provided log data to answer questions thoroughly and cite relevant information from the logs."}]' \
    --additional-model-request-fields '{"reasoningConfig": {"type": "enabled", "maxReasoningEffort": "medium"}}'
