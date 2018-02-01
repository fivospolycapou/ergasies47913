import sys

class Brainf_ck():
    
    class ProgramError(StandardError): pass
    
    def __init__(self, src):
        self._tokens = src
        self._jumps = self._analyze_jumps(self._tokens)
    
    def run(self):
        tape = []
        pc = 0
        cur = 0
        
        while pc < len(self._tokens):
            if cur >= len(tape):
                tape.append(0)
            if self._tokens[pc] == '+':
                tape[cur] += 1
            elif self._tokens[pc] == '-':
                tape[cur] -= 1
            elif self._tokens[pc] == '>':
                cur += 1
            elif self._tokens[pc] == '<':
                cur -= 1
                if cur < 0: raise self.ProgramError(u'It can not move to the left from the starting point')
            elif self._tokens[pc] == '.':
                print chr(tape[cur]),
            elif self._tokens[pc] == ',':
                tape[cur] = ord(raw_input().strip())
            elif self._tokens[pc] == '[':
                if tape[cur] == 0:
                    pc = self._jumps[pc]
            elif self._tokens[pc] == ']':
                if tape[cur] != 0:
                    pc = self._jumps[pc]
            pc += 1
    
    def _analyze_jumps(self, tokens):
        jumps = {}
        starts = []
        
        for i, c in enumerate(tokens):
            if c == '[':
                starts.append(i)
            elif c == ']':
                if not starts: raise self.ProgramError(u'There are too many ')
                frm = starts.pop()
                to = i
                
                jumps[frm] = to
                jumps[to] = frm
        if starts: raise ProgramError(u'There are too many')
        
        return jumps

try:
    src = open(sys.argv[1]).read()
except IOError:
    src = sys.argv[1]
except IndexError:
    src = raw_input()

try:
    Brainf_ck(src).run()
except Brainf_ck.ProgramError:
    print u'Brainf_ckProgram execution failed'