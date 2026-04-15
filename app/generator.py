import os
import requests
from dotenv import load_dotenv
from app.prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_email(intent, facts, tone, model="openrouter/auto"):
    if not API_KEY:
        return "❌ Error: OPENROUTER_API_KEY not found. Check your .env file."

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    # Few-shot examples
    for example in FEW_SHOT_EXAMPLES:
        messages.append({
            "role": "user",
            "content": f"Intent: {example['input']['intent']}\nFacts: {example['input']['facts']}\nTone: {example['input']['tone']}"
        })
        messages.append({
            "role": "assistant",
            "content": example["output"]
        })

    # Actual input
    messages.append({
        "role": "user",
        "content": f"""
Intent: {intent}
Facts: {facts}
Tone: {tone}

Generate ONLY ONE professional email. Do not add anything else.
"""
    })

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "HTTP-Referer": "http://localhost:8501",   
                "X-Title": "Email Generator App"           
            },
            json={
                "model": model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 300
            }
        )

        data = response.json()

        # Debug print (important for errors)
        print("API RESPONSE:", data)

        # Handle API errors properly
        if "choices" not in data:
            return f"❌ API Error: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"
    