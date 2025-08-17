"""
You are asked to implement the transition logic for a digital wallet using a state machine structure. The wallet can be in one of two states: unauthenticated (before the user logs in) and authenticated (after a successful login).

You must implement a State class that represents each state. The State class needs to be hashable so it can be used as a dictionary key, and two instances of State with the same name should be equal.

You must define a transition table. It is a dictionary which maps each state to a list of allowed transitions. Each transition is represented by a tuple with three elements: the name of the action (for example "login" or "pay"), a checker function, and the next state. A checker function takes three parameters (the action parameter, the wallet password, and the current balance) and returns a tuple of three values. The first return value is a boolean indicating whether the transition should occur. The second value is the updated balance. The third value is an optional output (only required for balance inquiries).

The initial state of the wallet is unauthenticated.

In the unauthenticated state the only allowed action is “login <password>”, which moves the wallet to the authenticated state if the password is correct.
In the authenticated state the allowed actions are:

“logout” which moves back to the unauthenticated state

“topup <amount>” which adds the specified amount to the balance

“pay <amount>” which deducts the specified amount if there is enough balance

“balance” which returns the current balance without changing the state

The input consists of the wallet password on the first line, the initial balance on the second line, the number of actions on the third line, and then one action per line.

For each action you must output a line in the format:

Success=<True or False> <current_state> [optional_value]

The optional value is only printed for the balance action.

Sample Input:
opensesame
30
8
pay 5
login wrong
login opensesame
topup 20
pay 15
balance
logout
pay 10

Sample Output:
Success=False unauthenticated
Success=False unauthenticated
Success=True authenticated
Success=True authenticated
Success=True authenticated
Success=True authenticated 35
Success=True unauthenticated
Success=False unauthenticated
"""

from typing import Any, Optional, Tuple, Dict

class State:
    def __init__(self, state):
        self.state = state
        
    def __eq__(self, other: object):
        return isinstance(other, State) and self.state == other.state
    
    def __hash__(self):
        return hash(self.state)
    
unauthenticated = State("unauthenticated")
authenticated = State("authenticated")

def login(action_param: Optional[Any], wallet_password: str, wallet_balance: int) -> Tuple[bool, int, Optional[Any]]:
    if action_param == wallet_password:
        return (True, wallet_balance, None)
    else:
        return (False, wallet_balance, None)

def logout(action_param: Optional[Any], wallet_password: str, wallet_balance: int) -> Tuple[bool, int, Optional[Any]]:
    return (True, wallet_balance, None)

def topup(action_param: Optional[Any], wallet_password: str, wallet_balance: int) -> Tuple[bool, int, Optional[Any]]:
    return (True, wallet_balance + action_param, None)

def pay(action_param: Optional[Any], wallet_password: str, wallet_balance: int) -> Tuple[bool, int, Optional[Any]]:
    if action_param > wallet_balance:
        return (False, wallet_balance, None)
    else:
        return (True, wallet_balance - action_param, None)

def balance(action_param: Optional[Any], wallet_password: str, wallet_balance: int) -> Tuple[bool, int, Optional[Any]]:
    return(True, wallet_balance, wallet_balance)

transition_table = {
    unauthenticated: [("login", login, authenticated)], 
    authenticated: [("logout", logout, unauthenticated), 
                      ("topup", topup, authenticated), 
                      ("pay", pay, authenticated), 
                      ("balance", balance, authenticated)]
}

class Wallet:
    def __init__(self, init_state: State, init_balance: int, password: str, transition_table: Dict):
        self._state = init_state
        self._balance = init_balance
        self._password = password
        self._transition_table = transition_table

    def next(self, action: str, param: Optional[Any]) -> Tuple[bool, Optional[Any]]:
        try:
            for transition_action, check, next_state in self._transition_table[self._state]:
                if action == transition_action:
                    passed, new_balance, res = check(param, self._password, self._balance)
                    if passed:
                        self._balance = new_balance
                        self._state = next_state
                        return True, res
        except KeyError:
            pass
        return False, None

wallet = Wallet(unauthenticated, 30, "opensesame", transition_table)

print(wallet.next("login", "opensesame"))  # -> (True, None)
print(wallet.next("balance", None))        # -> (True, 30)
print(wallet.next("topup", 20))            # -> (True, None)
print(wallet.next("balance", None))        # -> (True, 50)
print(wallet.next("pay", 15))              # -> (True, None)
print(wallet.next("logout", None))         # -> (True, None)
print(wallet.next("pay", 10))              # -> (False, None)
