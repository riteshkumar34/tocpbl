# Turning machine

import json

class SpaceBoundedTM:
    def __init__(self, tape, start_state, final_states, transitions, space_limit):
        self.tape = list(tape) + ['_'] * (space_limit - len(tape))  
        self.head = 0
        self.state = start_state
        self.final_states = final_states
        self.transitions = transitions
        self.space_limit = space_limit

    def step(self):
        if self.state in self.final_states:
            return False  
        
        symbol = self.tape[self.head]
        if (self.state, symbol) in self.transitions:
            new_state, new_symbol, move = self.transitions[(self.state, symbol)]
            self.tape[self.head] = new_symbol
            self.state = new_state

            if move == 'R':
                self.head = min(self.head + 1, self.space_limit - 1)  
            elif move == 'L':
                self.head = max(self.head - 1, 0)
            return True
        return False  

    def run(self):
        print("Initial Tape: ", "".join(self.tape))
        while self.step():
            print("Tape:", "".join(self.tape), " | State:", self.state)
        print("Final Tape: ", "".join(self.tape))
