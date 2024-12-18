class Program:
    def __init__(self, data):
        self.registers = {'A': 0, 'B': 0, 'C': 0}
        self.prog, self.prog_string = None, None
        self.pointer, self.move_pointer = 0, True
        self.output = ''
        self.setup_program(data)
        self.base_r = self.registers.copy()
        self.opcodes = {0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz, 4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv}
        self.combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: self.registers['A'], 5: self.registers['B'], 6: self.registers['C'], 7: None}

    def adv(self, operand):
        self.registers['A'] = self.registers['A'] // (2 ** self.combo[operand])

    def bxl(self, operand):
        self.registers['B'] = operand ^ self.registers['B']

    def bst(self,operand):
        self.registers['B'] = self.combo[operand] % 8

    def jnz(self,operand):
        if self.registers['A'] != 0:
            self.pointer = operand
            self.move_pointer = False

    def bxc(self,operand):
        self.registers['B'] = self.registers['B'] ^ self.registers['C']

    def out(self,operand):
        # print(f'Output {self.combo[operand]} % 8 = {self.combo[operand] % 8}')
        # print(self.registers['A'])
        self.output += str((self.combo[operand] % 8)) + ','

    def bdv(self,operand):
        self.registers['B'] = self.registers['A'] // (2 ** self.combo[operand])

    def cdv(self,operand):
        self.registers['C'] = self.registers['A'] // (2 ** self.combo[operand])

    def run(self):
        # print(self.prog)
        # print(self.registers)
        while self.pointer < len(self.prog):
            opcode, operand = self.prog[self.pointer], self.prog[self.pointer + 1]
            self.opcodes[opcode](operand)
            if self.move_pointer:
                self.pointer += 2
            else:
                self.move_pointer = True
            # print(f'oc = {opcode}, op = {operand} --> {self.registers}')
            self.update_combos()
        return None

    def update_combos(self):
        self.combo[4] = self.registers['A']
        self.combo[5] = self.registers['B']
        self.combo[6] = self.registers['C']

    def reset(self):
        self.pointer = 0
        self.output = ''
        self.registers = self.base_r.copy()
        self.update_combos()

    def setup_program(self, data):
        for line in data:
            if 'A:' in line:
                self.registers['A'] = int(line.split(' ')[-1])
            elif 'B:' in line:
                self.registers['B'] = int(line.split(' ')[-1])
            elif 'C:' in line:
                self.registers['C'] = int(line.split(' ')[-1])
            elif 'Prog' in line:
                self.prog = list(map(int, line.split(' ')[-1].split(',')))
        self.prog_string = ','.join(map(str, self.prog))

file = 'input.txt'
# file = 'example_02.txt'

with open(file, encoding="utf8") as f:
    data = f.read().splitlines()

p = Program(data)
p.run()
print(f'Part 1: {p.output[:-1]}')

As = [0]
found = False
while len(As) != 0:
    A = As.pop(0)
    for dA in range(8):
        p.reset()
        p.registers['A'] = A + dA
        p.update_combos()
        p.run()
        string = p.output[:-1]
        if p.prog_string == string:
            print(f'Part 2: {A + dA}')
            found = True
            break
        if p.prog_string.endswith(string) and A + dA != 0:
            As.append((A + dA) * 8)
    if found:
        break
