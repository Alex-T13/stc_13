import dataclasses
from typing import NamedTuple


class ResponseT(NamedTuple):
    status: str
    headers: dict
    payload: bytes


@dataclasses.dataclass
class RequestT:  # NamedTaple???
    method: str
    path: str
    headers: dict