from dataclasses import dataclass
from event import Event


@dataclass
class TrackingPlan:
    events: list[Event]