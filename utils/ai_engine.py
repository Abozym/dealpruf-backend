def analyze_lease(text):
    return {
        "summary": {
            "lease_term": "Jan 1, 2024 – Dec 31, 2028",
            "renewal_option": "1 x 5-year",
            "monthly_rent": "$5,000 (+3%/yr)",
            "parties": "XYZ Holdings / ABC Properties"
        },
        "red_flags": [
            { "issue": "No termination clause defined", "risk": "HIGH" },
            { "issue": "CAM clause vague (‘reasonable’)", "risk": "MEDIUM" }
        ],
        "score": 72,
        "zoning_notes": [
            "Use is general office; verify in C3 zoning district"
        ]
    }