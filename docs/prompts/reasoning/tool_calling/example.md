# Tool Calling
Use Nova reasoning models to intelligently select and use tools to accomplish complex tasks.

### System Prompt Template
      You are an expert {domain} assistant who can use available tools to {accomplish goal}.
      Use the appropriate tools to complete the requested task efficiently and provide comprehensive results.

### User Prompt Template
      {task description}
      
      Ask clarifying questions if needed.

## Example
### Amazon Nova 2 Lite System Prompt
      You are an expert data analyst who can use available tools to analyze datasets and generate insights.
      Use the appropriate tools to complete the requested analysis efficiently and provide comprehensive results.

### Amazon Nova 2 Lite User Prompt
      Analyze the sales performance for Q4 2024 and create a summary report with visualizations.
      
      The sales database contains tables: orders, customers, products, and sales_reps.
      Focus on revenue trends, top-performing products, and regional performance.

### Tool Configuration
      Tools available via Bedrock toolConfig:
      - query_database: Execute SQL queries against the sales database
      - create_chart: Generate charts from data (bar, line, pie, scatter)
      - calculate_statistics: Calculate statistical measures (mean, median, growth rates)

### Amazon Nova 2 Lite Sample Response
!!! success "Response"
    --8<-- "results/tool_calling_20251122_144515.md"

### API Request
=== "python"

      ```python
      --8<-- "docs/prompts/reasoning/tool_calling/example.py"
      ```

=== "AWS CLI"

      ```bash
      --8<-- "docs/prompts/reasoning/tool_calling/example.sh"
      ```

=== "json"

      ```json
      --8<-- "docs/prompts/reasoning/tool_calling/example.json"
      ```
      Analyze the sales performance for Q4 2024 and create a summary report with visualizations.
      
      Available tools:
      - query_database(sql_query): Execute SQL queries against the sales database
      - create_chart(data, chart_type): Generate charts from data (bar, line, pie, scatter)
      - calculate_statistics(data, metrics): Calculate statistical measures (mean, median, growth rates)
      - generate_report(sections): Create formatted reports with multiple sections
      
      The sales database contains tables: orders, customers, products, and sales_reps.
      Focus on revenue trends, top-performing products, and regional performance.
      
      Ask clarifying questions if needed.

### Amazon Nova 2 Lite Sample Response
!!! success "Response"
    --8<-- "results/tool_calling_20251122_144515.md"

### API Request
=== "python"

      ```python
      --8<-- "docs/prompts/reasoning/tool_calling/example.py"
      ```

=== "AWS CLI"

      ```bash
      --8<-- "docs/prompts/reasoning/tool_calling/example.sh"
      ```

=== "json"

      ```json
      --8<-- "docs/prompts/reasoning/tool_calling/example.json"
      ```
