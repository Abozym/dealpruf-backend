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
- revision_suggestions: array of concise improvement ideas, like:
  - "Add indemnification clause."
  - "Clarify CAM expense responsibilities."
  - "Include tenant right to early termination."

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

