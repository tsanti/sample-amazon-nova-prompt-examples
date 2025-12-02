# Long Context Analysis
Use Nova reasoning models to analyze and synthesize information from extensive documents or datasets.

### System Prompt Template
      You are an expert {domain} assistant. Answer the question being asked using only the document text provided. Follow these instructions:

      1. {instructions}
      2. {instructions}

### User Prompt Template
      Question: {question}

## Example

Here we ask Nova to explain the logic behind a conclusion made in the [Enron Case](https://www.txs.uscourts.gov/page/newby-et-al-v-enron-corporation-et-al-401-cv-3624)

We've also included a `download.py` script to download the document text. Feel free to use for other documents as well.

### Amazon Nova 2 Lite System Prompt
      You are an expert {domain} assistant. Answer the question being asked using only the document text provided. Follow these instructions:

      1. The full case name in italics (e.g., Skilling v. United States).
      2. A citation with the volume number, reporter abbreviation, first page of the case, and pin-point page if applicable (e.g., 561 U.S. 358).
      3. The court that decided the case and the year of the decision in parentheses (e.g., (U.S. Supreme Court 2010)).
      4. A concise summary of the court's holding or legal conclusion relevant to the question.
      5. Any important legal principles or precedents established by the case.
      6. Optionally, a brief contextual or procedural background if relevant.

### Amazon Nova 2 Lite User Prompt
      Document text:
      
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
      
      [Full document content continues...]


### Amazon Nova 2 Lite Sample Response
!!! success "Response"
    --8<-- "results/long_context_20251122_143744.md"

### API Request
=== "python"

      ```python
      --8<-- "docs/prompts/reasoning/long_context/example.py"
      ```

=== "AWS CLI"

      ```bash
      --8<-- "docs/prompts/reasoning/long_context/example.sh"
      ```

=== "json"

      ```json
      --8<-- "docs/prompts/reasoning/long_context/example.json"
      ```
