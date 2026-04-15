SYSTEM_PROMPT = """
You are a professional corporate communication expert.

Your task is to generate a SINGLE professional email.

STRICT RULES:
- Only generate ONE email
- Do NOT generate multiple emails
- Do NOT include extra examples or explanations
- Do NOT repeat the input
- Do NOT include 'Intent', 'Facts', or 'Tone' in output
- Ensure ALL key facts are included naturally
- Match the tone exactly

FORMAT:
Subject: <subject line>

<email body>

Best regards,
[Your Name]
"""

FEW_SHOT_EXAMPLES = [
    {
        "input": {
            "intent": "Follow up after meeting",
            "facts": "Discussed project timeline; Need feedback by Friday",
            "tone": "formal"
        },
        "output": """Subject: Follow-up on Project Timeline Discussion

Dear [Recipient],

I hope you are doing well.

I wanted to follow up on our recent discussion regarding the project timeline. As mentioned, we would appreciate your feedback by Friday to ensure we stay on track.

Please let me know if you need any additional information.

Best regards,
[Your Name]"""
    }
]