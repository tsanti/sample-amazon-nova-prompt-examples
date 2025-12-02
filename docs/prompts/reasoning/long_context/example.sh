aws bedrock-runtime converse \
  --model-id "amazon.nova-2-lite-v1:0" \
  --system '[{"text": "Answer the question being asked using only the document text provided. Follow these instructions:\n\n1. The full case name in italics (e.g., Skilling v. United States).\n2. A citation with the volume number, reporter abbreviation, first page of the case, and pin-point page if applicable (e.g., 561 U.S. 358).\n3. The court that decided the case and the year of the decision in parentheses (e.g., (U.S. Supreme Court 2010)).\n4. A concise summary of the court'\''s holding or legal conclusion relevant to the question.\n5. Any important legal principles or precedents established by the case.\n6. Optionally, a brief contextual or procedural background if relevant."}]' \
  --messages file://messages.json \
  --additional-model-request-fields '{"reasoningConfig": {"type": "enabled", "maxReasoningEffort": "high"}}' \
  --region us-west-2
