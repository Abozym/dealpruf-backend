from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_lease(text):
    prompt = f"""
You are a commercial real estate assistant. Extract key terms from this lease and identify red flags.

Lease:
{text}

Return JSON with:
- summary: lease_term, renewal_option, monthly_rent, parties
- red_flags: array of {{"issue": "...", "risk": "HIGH|MEDIUM|LOW"}}
- score (0–100)
- zoning_notes: bullet points
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You extract structured lease terms and risks."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return eval(response.choices[0].message.content)
