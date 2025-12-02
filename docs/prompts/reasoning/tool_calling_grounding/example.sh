aws bedrock-runtime converse \
 --model-id amazon.nova-2-lite-v1:0 \
 --system "You are an expert financial analyst who can use web search and code execution to analyze company performance.
Use the available system tools to gather current financial information and perform analysis visualizations." \
 --messages "[{\"role\":\"user\",\"content\":[{\"text\":\"Analyze Tesla's financial performance for 2024. Focus on:\n- Revenue growth and quarterly trends\n- Profitability metrics (gross margin, operating margin)\n- Key financial ratios and comparisons to previous years\n- Stock performance and market sentiment\n\nUse web search to find the latest financial reports, earnings calls, and market data. Then use code interpreter to:\n- Extract and organize key financial metrics\n- Calculate growth rates and ratios\n- Create visualizations showing trends and comparisons\n- Identify notable patterns or concerns\n\nProvide a analysis charts and actionable insights.\n\nAsk clarifying questions if needed.\"}]}]" \
 --tool-config "{\"tools\":[{\"systemTool\":{\"name\":\"nova_grounding\"}},{\"systemTool\":{\"name\":\"nova_code_interpreter\"}}]}" \
 --additional-model-request-fields "{"reasoningConfig":{"type":"enabled","maxReasoningEffort":"low"}}"reasoningConfig\":{\"type\":\"enabled\",\"maxReasoningEffort\":\"medium\"}}" \
 --inference-config "{\"temperature\":0.3,\"topP\":0.9,\"maxTokens\":10000}" \
 --region us-west-2
