import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
def plan_task(task: str):

    task = task.lower()

    if "review" in task:
        return [
            "explain",
            "bugs",
            "optimize",
            "complexity",
            "security"
        ]

    elif "fix" in task:
        return ["fix"]

    elif "security" in task:
        return ["security"]

    elif "bug" in task:
        return ["bugs"]

    elif "optimize" in task:
        return ["optimize"]

    elif "complexity" in task:
        return ["complexity"]

    else:
        return ["explain"]
    
def ai_plan(task):

    prompt = f"""
You are an AI Planner Agent.

Your job is to decide which AI agents should execute.

Available agents:

1. explain
2. bugs
3. optimize
4. complexity
5. security
6. fix

User Request:
{task}

Return ONLY a JSON list.

Example:

["explain","bugs","security"]

No explanation.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    try:
        return json.loads(result)
    except Exception:
        return plan_task(task)