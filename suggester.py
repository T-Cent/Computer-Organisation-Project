import parser as ps

class colors:
    red_a = "\x1b[31m"
    cyan_a = "\x1b[36m"
    green_a = "\x1b[32m"
    hl_red_a = "\x1b[41m"
    hl_white_a = "\x1b[107m"
    hl_green_a = "\x1b[42m"
    end = "\x1b[0m"

    def red(self, x):
        return self.red_a + str(x) + self.end
    def cyan(self, x):
        return self.cyan_a + str(x) + self.end
    def green(self, x):
        return self.green_a + str(x) + self.end
    def highlight_white(self, x):
        return self.hl_white_a + str(x) + self.end
    def highlight_green(self, x):
        return self.hl_green_a + str(x) + self.end
    def highlight_red(self, x):
        return self.hl_red_a + str(x) + self.end
        

def suggestions_for(instruction):
    all_instructions = ps.R_Type_Instructions + ps.I_Type_Instructions + ps.S_Type_Instructions + ps.B_Type_Instructions + ps.U_Type_Instructions + ps.J_Type_Instructions + ps.Bonus

    def suggester_f(instruction):
        def suggester(i):
                count = 0
                for x in instruction:
                    if (x in i):
                        count += 1
                return count
        return suggester
    
    c = colors()

    suggester = suggester_f(instruction)
    all_instructions.sort(key=suggester, reverse=True)
    all_instructions = filter(lambda x: suggester(x)>len(x)-2, all_instructions)
    print(f"{c.red(instruction)} {c.highlight_red(' did not match any known instruction, perhaps you meant')}", end=" ") 
    print(c.cyan_a, end="")
    print(*all_instructions, sep=", ", end="?")
    print(c.end)
