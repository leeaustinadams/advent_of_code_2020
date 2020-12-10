import re

instruction_regex = re.compile(r'(acc|jmp|nop) (\+|-)(\d+)')

def parse(filename):
    with open(filename, 'rt') as f:
        data = f.read()

    lines = data.splitlines()
    instructions = []
    for line in lines:
        match = instruction_regex.match(line)
        if match:
            op, sign, value = match.groups()
            value = int(value)
            if sign == '-':
                value *= -1
            instructions.append((op, value))

    return instructions

class VirtualMachine:
    def __init__(self):
        self.reset()

    def reset(self):
        self.instruction_index = 0
        self.accumulator = 0
        self.executed = set()

    def eval(self, instructions):
        while self.instruction_index < len(instructions):
            if self.instruction_index in self.executed:
                return

            self.executed.add(self.instruction_index)

            op, value = instructions[self.instruction_index]

            if op == 'acc':
                self.accumulator += value
                self.instruction_index += 1
            elif op == 'jmp':
                self.instruction_index += value
            elif op == 'nop':
                self.instruction_index += 1

def main():
    instructions = parse('input')

    vm = VirtualMachine()

    for i in range(0, len(instructions)):
        op, value = instructions[i]

        # mutate instructions
        if op == 'jmp':
            instructions[i] = ('nop', value)
        elif op == 'nop':
            instructions[i] = ('jmp', value)

        vm.eval(instructions)

        if vm.instruction_index >= len(instructions):
            print("Success", vm.accumulator)
            return

        # un-mutate instructions
        instructions[i] = (op, value)
        vm.reset()

if __name__ == '__main__':
    main()
