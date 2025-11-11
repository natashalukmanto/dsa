from dataclasses import dataclass
from typing import Dict, Tuple, Optional


@dataclass(frozen=True)
class Flight:
    """
    Represents a single direct flight between two destinations.
    """

    source: str
    destination: str
    airline: str
    cost: int


class FlightGraph:
    """
    Stores flights in a directed graph and allows efficient lookups
    of direct-flight costs between (source, destination) pairs.
    """

    def __init__(self, routes_str: str) -> None:
        """
        Initialize the graph from a string like:
        "UK:US:FedEx:4,UK:FR:Jet1:2,US:UK:RyanAir:8,CA:UK:CanadaAir:8"
        """
        self._routes: Dict[Tuple[str, str], Flight] = {}
        self._parse_routes(routes_str)

    def _parse_routes(self, routes_str: str) -> None:
        """
        Internal helper to parse the input string and populate the route map.

        Each route must be of the form: "Source:Destination:Airline:Cost".
        Raises ValueError if any entry is malformed.
        """
        if not routes_str:
            return

        for token in routes_str.split(","):
            token = token.strip()
            if not token:
                # Ignore empty sections like trailing commas
                continue

            parts = token.split(":")
            if len(parts) != 4:
                raise ValueError(f"Malformed route entry: {token!r}")

            source, destination, airline, cost_str = parts

            if not source or not destination:
                raise ValueError(
                    f"Source and destination must be non-empty in {token!r}"
                )

            try:
                cost = int(cost_str)
            except ValueError as exc:
                raise ValueError(f"Invalid cost {cost_str!r} in {token!r}") from exc

            if cost < 0:
                raise ValueError(f"Cost must be non-negative in {token!r}")

            # Store by (source, destination); overwrite if duplicate appears.
            self._routes[(source, destination)] = Flight(
                source=source,
                destination=destination,
                airline=airline,
                cost=cost,
            )

    def get_cost(self, source: str, destination: str) -> Optional[int]:
        """
        Return the cost of a direct flight from `source` to `destination`.

        If no such direct flight exists, returns None.
        """
        flight = self._routes.get((source, destination))
        if flight is None:
            return None
        return flight.cost

    def has_direct_flight(self, source: str, destination: str) -> bool:
        """Convenience method to check if a direct flight exists."""
        return (source, destination) in self._routes


def build_flight_graph(routes_str: str) -> FlightGraph:
    """
    Convenience factory function, so caller code is nice and simple.
    """
    return FlightGraph(routes_str)


if __name__ == "__main__":
    # Example usage and lightweight tests

    routes = "UK:US:FedEx:4,UK:FR:Jet1:2,US:UK:RyanAir:8,CA:UK:CanadaAir:8"
    graph = build_flight_graph(routes)

    # Expected costs:
    assert graph.get_cost("UK", "US") == 4
    assert graph.get_cost("UK", "FR") == 2
    assert graph.get_cost("US", "UK") == 8
    assert graph.get_cost("CA", "UK") == 8

    # Non-existing route should return None, not crash
    assert graph.get_cost("US", "FR") is None

    print("All checks passed.")
    print("UK -> US cost:", graph.get_cost("UK", "US"))
    print("UK -> FR cost:", graph.get_cost("UK", "FR"))
    print("US -> UK cost:", graph.get_cost("US", "UK"))
    print("CA -> UK cost:", graph.get_cost("CA", "UK"))
