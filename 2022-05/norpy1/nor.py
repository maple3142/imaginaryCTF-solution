#!/usr/bin/env python3

from copy import deepcopy

DEBUG = False

def die(reason="Unknown error.", *args):
    print(reason, *args)
    exit()

class Nor():
    def __init__(self, in1, in2, out):
        # these are wire names
        self.in1 = in1
        self.in2 = in2
        self.out = out

    def step(self, wires):
        if any(i not in wires for i in [self.in1, self.in2, self.out]):
            die(f"Unknown wire! One of ({self.in1}, {self.in2}, {self.out})")
        return {self.out: not(wires[self.in1] or wires[self.in2])}

class Circuit():
    def __init__(self):
        self.wires = {}
        self.inputs = set()
        self.outputs = set()
        self.gates = []

        self.done = False
        self.timestep = 0

    def step(self):
        if DEBUG:
            self.print_wires()

        new_wires = deepcopy(self.wires)
        for gate in self.gates:
            updated_wires = gate.step(self.wires)
            for wire in updated_wires:
                new_wires[wire] = updated_wires[wire]

        changed = False
        for wire in new_wires:
            changed |= self.wires[wire] != new_wires[wire]
            self.wires[wire] = new_wires[wire]
        if not changed:
            self.done = True
        self.timestep += 1

    def run(self, time_limit=100):
        while not self.done and self.timestep < time_limit:
            self.step()
        print(f"Circuit ran for {self.timestep} steps.")
        return self.timestep

    def print_wires(self):
        print(f"Wires at timestep {self.timestep}:")
        for wire in self.wires:
            print(f"\t{wire}: {self.wires[wire]}")

    @classmethod
    def from_input(cls):
        ret = Circuit()
        print("Enter up to 10 gates in the form of:")
        print("\t{input_wire1} {input_wire2} {output_wire}")
        print("Enter a blank line if you'd like to stop before 10 gates.")
        for num_gates in range(10):
            gate = input('>>> ')
            if len(gate.strip()) == 0:
                break
            gate_wires = gate.strip().split()
            if len(gate_wires) != 3:
                die("Number of wires is not 3!")
            new_gate = Nor(*gate_wires)
            ret.gates.append(new_gate)
            ret.inputs |= {gate_wires[0], gate_wires[1]}
            if gate_wires[2] in ret.outputs:
                die(f"Wire {gate_wires[2]} is overdefined!")
            ret.outputs |= {gate_wires[2]}

        if len(ret.gates) == 10:
            print("That's all you get!\n")

        print("Please enter all inputs that should start as True, separated by spaces.")
        true_inputs = input(">>> ")
        for wire in true_inputs.strip().split():
            if wire in ret.inputs:
                ret.wires[wire] = True

        print()
        print("Please enter all inputs that should start as False, separated by spaces.")
        false_inputs = input(">>> ")
        for wire in false_inputs.strip().split():
            if wire in ret.inputs:
                ret.wires[wire] = False

        for wire in ret.outputs:
            ret.wires[wire] = None

        for wire in ret.inputs:
            if wire not in ret.wires:
                ret.wires[wire] = None

        return ret

if __name__ == '__main__':
    circuit = Circuit.from_input()
    print("Running...")
    print("This may take a few seconds.")
    steps = circuit.run(50000)
    if steps >= 50000:
        print(open('flag.txt').read())
    else:
        print("Better luck next time!")