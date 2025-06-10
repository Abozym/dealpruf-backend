
from pydantic import BaseModel
from typing import List, Optional

class RedFlag(BaseModel):
    issue: str
    risk: str

class Summary(BaseModel):
    lease_term: str
    renewal_option: str
    monthly_rent: str
    parties: str

class LeaseAnalysisResult(BaseModel):
    summary: Summary
    red_flags: List[RedFlag]
    score: int
    zoning_notes: Optional[List[str]]
