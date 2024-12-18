
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

print(f' Input: {p.prog_string}')

revers_program = list(map(int, p.prog_string.split(',')))[::-1]
#
dAs = list(map(int, '01234567'))
base_A = 0
found = False
i, j = 0, 0
while i < len(revers_program):
    print(f'i = {i}')
    n = revers_program[i]
    found_next_A = False
    for dA in dAs[j:]:
        cur_A = base_A + dA
        if cur_A == 0:
            continue
        print(f'A + da = {cur_A}')
        p.reset()
        p.registers['A'] = base_A + dA
        p.update_combos()
        # print(f'A = {p.registers['A']}')
        p.run()
        print(f'Output: {p.output}')
        if int(p.output.split(',')[-2]) == n:
            base_A = cur_A * 8
            found_next_A = True
            break
        if p.output[:-1] == p.prog_string:
            print(f'Part 2: {cur_A}')
            found = True
        # if 0 in new_dAs:
        #     new_dAs.remove(0)
    if found:
        break
    if not found_next_A:
        j = len(dAs)
        base = len(dAs) // 8
        for f in range(1, 8):
            for val in dAs[:]:
                dAs.append(base * f + val)
        print(dAs)
        input('...')
    else:
        i += 1
        j = 0
        input('...')
