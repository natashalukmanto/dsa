from __future__ import annotations

from dataclasses import dataclass


# dataclass is just shorthand in Python so you wouldn't need to creat __init__ and __repr__ or __eq__
# frozen = True means that this class is immutable
@dataclass(frozen=True) 
class User:
    """Represents a registered user in the social network.

    Immutable value object keyed on user_id.
    """

    user_id: str
    name: str
