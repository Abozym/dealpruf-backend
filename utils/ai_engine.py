import openai
import os
import json

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_lease(text):
    prompt = f"""
You are a commercial real estate assistant. Extract key terms from this lease and identify red flags.

Lease:
{text}

Return JSON with:
- summary:
  - lease_term
  - renewal_option
  - monthly_rent
  - parties: {{ landlord, tenant }}
- red_flags: array of {{ "issue": "...", "risk": "HIGH|MEDIUM|LOW" }}
- score (0–100)
- zoning_notes: bullet points
- After the red flags section, provide a field called "revision_suggestions".

These should NOT just repeat the red flags. Instead, offer practical, clause-level language suggestions or legal best practices that would reduce the risks.

Each suggestion should begin with an action verb and explain how to improve or reword the lease.

Examples:
- "Add a renewal clause specifying a 1-year auto-renewal unless terminated by either party in writing."
- "Include a specific CAM cap or fixed percentage to prevent unpredictable charges."
- "Define insurance requirements with policy limits and required coverages like general liability and property loss."


When identifying red flags, check for:
- missing or vague lease renewal clauses
- missing or unclear termination conditions
- no mention of insurance requirements
- CAM or maintenance ambiguity
- subletting/assignment restrictions
- improvement reimbursement terms
- lack of tax responsibility definition
- lack of dispute resolution clauses
- harvest rights / post-lease access
- zoning or land use conflict potential
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You extract structured lease terms and risks."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("❌ JSON decode failed. Raw content:\n", content)
        return {"error": "GPT response was not valid JSON"}

