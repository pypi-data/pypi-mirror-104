"""Let's find some podcasts!"""

__version__ = "0.1.0"

from dataclasses import dataclass
from typing import Optional, List

SEARCH_URL = "https://itunes.apple.com/search"

@dataclass
class Podcast:
    """Podcast metadata."""
    id: str
    name: str
    author: str
    url: str
    feed: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None


def search(name: str, limit: int = 5) -> List[Podcast]:
    """Search podcast by name."""
    params = {"term": name, "limit": limit, "media": "podcast"}
    response = _get(url=SEARCH_URL, params=params)
    return _parse(response)