from typing import Dict, Optional, Tuple

def arm(action_param: Optional[str], system_pin: str, current_logs: list) -> Tuple[bool, list, Optional[str]]:
    if action_param == system_pin:
        return (True, current_logs, None)
    else:
        return (False, current_logs, None)

def disarm(action_param: Optional[str], system_pin: str, current_logs: list) -> Tuple[bool, list, Optional[str]]:
    if action_param == system_pin:
        return (True, current_logs, None)
    else:
        return (False, current_logs, None)

def trigger(action_param: Optional[str], system_pin: str, current_logs: list) -> Tuple[bool, list, Optional[str]]:
    current_logs.append(action_param)
    return(True, current_logs, None)

def view_logs(action_param: Optional[str], system_pin: str, current_logs: list) -> Tuple[bool, list, Optional[str]]:
    return(True, current_logs, current_logs)

class State:
    def __init__(self, state: str):
        self.state = state
    
    def __eq__(self, other: object):
        return self.state == other.state
    
    def __hash__(self):
        return hash(self.state)
        
    def __repr__(self):
        return f"{self.state}"
    
disarmed = State("disarmed")
armed = State("armed")

transition_table = {disarmed: [("arm", arm, armed)],
                    armed: [("disarm", disarm, disarmed), ("trigger", trigger, armed), ("view_logs", view_logs, armed)]}
    
    
class SecuritySystem:
    def __init__(self, init_state: State, system_pin: str, transition_table: Dict):
        self.state = init_state
        self.pin = system_pin
        self.logs = []
        self.transition_table = transition_table

    def next(self, action: str, param: Optional[str]) -> Tuple[bool, Optional[str]]:
        try:
            for transition_action, check, next_state in self.transition_table[self.state]:
                if action == transition_action:
                    passed, new_logs, res = check(param, self.pin, self.logs)
                    if passed:
                        self.logs = new_logs
                        self.state = next_state
                    return passed, res
        except KeyError:
            pass
        return False, None

system = SecuritySystem(disarmed, "1234", transition_table)
actions = [
    ("view_logs", None),
    ("arm", "1111"),
    ("arm", "1234"),
    ("trigger", "backdoor"),
    ("view_logs", None),
    ("disarm", "1234")
]
for action, param in actions:
    success, res = system.next(action, param)
    if res is not None:
        print(f"Success={success} {system.state} {res}")
    else:
        print(f"Success={success} {system.state}")

