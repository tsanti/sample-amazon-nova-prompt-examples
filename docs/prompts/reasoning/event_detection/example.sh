aws bedrock-runtime converse \
  --model-id "amazon.nova-2-lite-v1:0" \
  --system '[
    {
      "text": "You are an expert cybersecurity analyst who specializes in detecting and analyzing security incidents from system logs. Identify relevant security events from the provided log data and provide detailed threat analysis with recommended actions."
    }
  ]' \
  --messages '[
    {
      "role": "user",
      "content": [
        {
          "text": "## Data ##\n```\n2024-03-19 14:23:15 [INFO] User john.doe@company.com logged in from IP 192.168.1.100\n2024-03-19 14:23:45 [INFO] File access: /home/john.doe/documents/project_alpha.pdf\n2024-03-19 14:24:12 [WARN] Failed login attempt for admin@company.com from IP 203.0.113.45\n2024-03-19 14:24:18 [WARN] Failed login attempt for admin@company.com from IP 203.0.113.45\n2024-03-19 14:24:25 [WARN] Failed login attempt for admin@company.com from IP 203.0.113.45\n2024-03-19 14:24:31 [ERROR] Account locked: admin@company.com\n2024-03-19 14:25:02 [INFO] User sarah.smith@company.com logged in from IP 10.0.0.50\n2024-03-19 14:25:15 [INFO] Database query executed: SELECT * FROM customer_data WHERE ssn IS NOT NULL\n2024-03-19 14:25:22 [WARN] Large data export initiated by sarah.smith@company.com (50,000 records)\n2024-03-19 14:26:45 [INFO] VPN connection established from IP 198.51.100.75 for user mike.wilson@company.com\n2024-03-19 14:27:12 [WARN] Unusual file access pattern detected for user mike.wilson@company.com\n2024-03-19 14:27:30 [ERROR] Antivirus alert: Suspicious file detected in /tmp/update.exe\n2024-03-19 14:28:01 [WARN] Multiple failed SSH attempts from IP 198.51.100.75\n2024-03-19 14:28:15 [INFO] System backup initiated by scheduled task\n2024-03-19 14:29:33 [ERROR] Network anomaly detected: Unusual outbound traffic to IP 185.220.101.42\n```\n\n## Detection Criteria ##\nIdentify and analyze:\n- Brute force attacks\n- Insider threat indicators\n- Malware/suspicious file activity\n- Data exfiltration attempts\n- Network anomalies\n- Account compromise indicators\n\nFor each detected event, provide:\n- Event classification and severity\n- Timeline and affected systems/users\n- Potential impact assessment\n- Recommended immediate actions\n- Investigation priorities\n\nAsk clarifying questions if needed."
        }
      ]
    }
  ]' \
  --additional-model-request-fields '{
    "reasoningConfig": {
      "type": "enabled",
      "maxReasoningEffort": "low"
    }
  }' \
  --region us-west-2
