#!/usr/bin/env python3

from copy import deepcopy

DEBUG = 0

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
        if all(i is None for i in [wires[self.in1], wires[self.in2]]):
            return {self.out: None}
        return {self.out: not(wires[self.in1] or wires[self.in2])}

class Circuit():
    def __init__(self):
        self.wires = {}
        self.inputs = set()
        self.outputs = set()
        self.gates = []

        self.done = False
        self.timestep = 0
        self.records = {}

    def step(self):
        if DEBUG:
            self.print_wires()

        new_wires = deepcopy(self.wires)
        for gate in self.gates:
            updated_wires = gate.step(self.wires)
            # print(gate.in1, gate.in2, gate.out, updated_wires)
            for wire in updated_wires:
                new_wires[wire] = updated_wires[wire]

        changed = False
        for wire in new_wires:
            changed |= self.wires[wire] != new_wires[wire]
            self.wires[wire] = new_wires[wire]
        if not changed:
            self.done = True

        for wire in self.wires:
            if wire not in self.records:
                self.records[wire] = ''

            if self.wires[wire] is True:
                self.records[wire] += 'T'
            elif self.wires[wire] is False:
                self.records[wire] += 'F'
            elif self.wires[wire] is None:
                self.records[wire] += 'N'

        self.timestep += 1

    def run(self, time_limit=100):
        while not self.done and self.timestep < time_limit:
            self.step()
        print(f"Circuit ran for {self.timestep} steps.")
        if DEBUG:
            self.print_wires()
            self.print_records()
        return self.timestep

    def print_wires(self):
        print(f"Wires at timestep {self.timestep}:")
        for wire in sorted(self.wires):
            print(f"\t{wire}: {self.wires[wire]}")

    def print_records(self):
        print(f"Records at timestep {self.timestep}:")
        for wire in sorted(self.wires):
            print(f"\t{wire}: {self.records[wire]}")

    @classmethod
    def from_file(cls, s):
        ret = Circuit()
        lines = [i for i in s.splitlines() if len(i) == 0 or i[0] != '#']
        while len(lines) > 0:
            gate = lines[0]
            lines = lines[1:]
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

        while len(lines) < 2:
            lines.append('')

        true_inputs = lines[0]
        lines = lines[1:]
        for wire in true_inputs.strip().split():
            if wire in ret.inputs:
                ret.wires[wire] = True

        false_inputs = lines[0]
        for wire in false_inputs.strip().split():
            if wire in ret.inputs:
                ret.wires[wire] = False

        for wire in ret.outputs:
            ret.wires[wire] = None

        for wire in ret.inputs:
            if wire not in ret.wires:
                ret.wires[wire] = None

        return ret
