class Flight:
    def __init__(self, source: str, dest: str, airline: str, price: int):
        self.source = source
        self.destination = dest
        self.airline = airline
        self.price = int(price)

map = {}

def populate_map(input: str) -> int:
    input_list = input.split(',')
    
    for i in range(len(input_list)):
        input_list[i] = input_list[i].split(':')
        map[input_list[i][0] + '-' + input_list[i][1]] = Flight(input_list[i][0], input_list[i][1], input_list[i][2], input_list[i][3])
        
populate_map("UK:US:FedEx:4,UK:FR:Jet1:2,US:UK:RyanAir:8,CA:UK:CanadaAir:8")

def getCost(source: str, dest: str):
    return f"{source}-{dest} cost: {map[source + '-' + dest].price}"

# Testing
print(getCost("UK", "US"))
print(getCost("UK", "FR"))
print(getCost("US", "UK"))
print(getCost("CA", "UK"))