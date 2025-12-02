# Tool Calling with System Tools 
Use Nova 2 reasoning models with built-in system tools Nova Grounding and Code Interpreter to accomplish research and analysis tasks with source citations.

### System Prompt Template
      You are an expert {domain} analyst who can use web search and code execution to {accomplish goal}.
      Use the available system tools to gather information and perform analysis.
      Always cite your sources with URLs and publication dates when available.

### User Prompt Template
      {task description}
      
      You have access to:
      - Web search for current information
      - Code interpreter for data analysis and calculations
      
      Important: For all information gathered from web search, provide proper citations including:
      - Source URLs
      - Publication dates when available
      - Brief description of the source (e.g., "Tesla Q3 2024 Earnings Report")
      
      Ask clarifying questions if needed.

## Example
### Amazon Nova 2 Lite System Prompt
      You are an expert financial analyst who can use web search and code execution to analyze company performance.
      Use the available system tools to gather current financial information and perform analysis visualizations.
      Always cite your sources with URLs and publication dates when available.

### Amazon Nova 2 Lite User Prompt
      Analyze Amazon's financial performance for 2024. Focus on:
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
      
      Ask clarifying questions if needed.

### Amazon Nova 2 Lite Sample Response
!!! success "Response"
    --8<-- "results/reasoning_tool_calling_grounding_20251126_143847.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/reasoning/tool_calling_grounding/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/reasoning/tool_calling_grounding/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/reasoning/tool_calling_grounding/example.json"
    ```
    ```
