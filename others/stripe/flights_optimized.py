from typing import Dict, Tuple


class Flight:
    def __init__(self, source, destination, airline, cost):
        self.source = source
        self.destination = destination
        self.airline = airline
        self.cost = cost


class FlightGraph:
    def __init__(self, input: str) -> None:
        self.routes: Dict[Tuple[str, str], Flight] = {}
        self._parse_routes(input)

    def _parse_routes(self, input: str) -> None:
        if not input:
            return

        for token in input.split(","):
            source, destination, airline, cost = token.split(":")

            # Quick checks
            if not source or not destination:
                raise ValueError(f"Source and destination must be non-empty in {token}")

            try:
                cost = int(cost)
            except ValueError as exc:
                raise ValueError(f"Invalid cost {cost} in {token}")

            if cost < 0:
                raise ValueError(
                    f"Cost {cost} must be a nonnegative integer in {token}"
                )

            self.routes[(source, destination)] = Flight(
                source, destination, airline, cost
            )

    def get_cost(self, source: str, dest: str):
        flight = self.routes.get((source, dest))
        if flight: 
            return flight.cost
        return None


def build_flight_graph(input: str) -> FlightGraph:
    return FlightGraph(input)


if __name__ == "__main__":
    routes = "UK:US:FedEx:4,UK:FR:Jet1:2,US:UK:RyanAir:8,CA:UK:CanadaAir:8"
    graph = build_flight_graph(routes)

    assert graph.get_cost("UK", "US") == 4
    assert graph.get_cost("UK", "FR") == 2
    assert graph.get_cost("US", "UK") == 8
    assert graph.get_cost("CA", "UK") == 8

    assert graph.get_cost("US", "FR") is None

    print("UK -> US cost:", graph.get_cost("UK", "US"))
    print("UK -> FR cost:", graph.get_cost("UK", "FR"))
    print("US -> UK cost:", graph.get_cost("US", "UK"))
    print("CA -> UK cost:", graph.get_cost("CA", "UK"))
