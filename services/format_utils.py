from __future__ import annotations
from datetime import date, time, datetime
import re


defformat_date(d: date) -> str:
 
    """Return a date formatted as YYYY-MM-DD."""
    return d.strftime("%Y-%m-%d")


defparse_date(value: str) -> date:
 
    """Parse a date string in YYYY-MM-DD format."""
    return datetime.strptime(value, "%Y-%m-%d").date()


defformat_time(t: time) -> str:
 
    """Return a time formatted as HH:MM."""
    return t.strftime("%H:%M")


defparse_time(value: str) -> time:
 
    """Parse a time string in HH:MM format."""
    return datetime.strptime(value, "%H:%M").time()


defclean_cpf(cpf: str) -> str:
 
    """Remove any non-digit characters from a CPF string."""
    return re.sub(r"\D", "", cpf)
