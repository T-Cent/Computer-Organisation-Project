import sys
import re
from lookup import R_Type, I_Type, S_Type, B_Type, U_Type, J_Type, Registers
import suggester as sg

'''
the RISCV assembler, used lookup.py and suggester.py as helper modules to keep things less complicated.
'''
R_Type_Instructions = ["add", "sub", "slt", "sltu", "xor", "sll", "srl", "or", "and"]
I_Type_Instructions = ["lw", "addi", "sltiu", "jalr"]
S_Type_Instructions = ["sw"]
B_Type_Instructions = ["beq", "bne", "bge", "bgeu", "blt", "bltu"]
U_Type_Instructions = ["auipc", "lui"]
J_Type_Instructions = ["jal"]
Bonus = ["mul", "rst", "halt", "rvrs"]
Unique_Registers = ["zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0", "fp", "s1", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"]
All_Instructions = R_Type_Instructions + I_Type_Instructions + S_Type_Instructions + B_Type_Instructions + U_Type_Instructions + J_Type_Instructions



if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    data = file.readlines()
    file.close()

    output_file_bin = open(sys.argv[2], "w")

    binary_output_list = []
    #stores the label name and its corresponding location in memory.
    labels_pointer = {}
    stack_pointer = 0

    c = sg.colors()
    
    global_correct = True

    #a helper function which the two's complement of a binary. if positive, the width is adjusted later
    def twos_complement(bits, number):
        if number >= 0:
            return bin(number)
        else:
            x = bin(abs(number))
            x = "0"*(bits+2-len(x)) + x[2:]
            y = "1"*bits
            #xor with 11...11 flips the bit 
            x = int(x, base=2)^int(y, base=2) 
            x += 0b1
            return bin(x)
      
    #a helper function which takes the indexes of registers and checks if they are valid
    def check_registers(line, *reg):
        correct_f = True
        for j in reg:
            i = one_line_data[j]
            if (i not in Unique_Registers):
                correct_f = False
                print(c.red(f"Error encountered at line {c.highlight_white(line+1)}, given register {c.highlight_red(i)} does not match any known register."))

        if not correct_f:
            global global_correct
            global_correct = False
            return True
    
    #the assembler was also made with the logical assumption that opcode should be on the left, this fixes this (for sure)
    def hot_fix_1(*args):
        x = ''
        for i in args[::-1]:
            x += str(i)

        return x
    
    #apparently labels should not be on their separate lines! have to throw an instruction on the same line! this assembler was not made like that, this loop is to fix that.
    corrections = 0
    for index, line in enumerate(data):
        if (":" in line):
            x_l = data[:index+corrections]
            x_r = data[index+1+corrections:]
            line = line.split(":")
            line[0] += ":"
            data = x_l + line + x_r
            corrections += 1

    #getting all labels and their corresponding pointers first
    for line, one_line in enumerate(data):
        one_line_data = list(filter(lambda x: x, re.split(",| |\(|\)|\t|\n", one_line)))
        
        stack_pointer += 4

        #ignoring empty lines
        if not len(one_line_data):
            stack_pointer -= 4
            continue

        #checking for a label
        if one_line_data[0][-1] == ":":
            #we do not increment the stack pointer for labels.
            stack_pointer -= 4 
            labels_pointer[one_line_data[0][:-1]] = stack_pointer
            continue 


    for line, one_line in enumerate(data):
        one_line_data = list(filter(lambda x: x, re.split(",| |\(|\)|\t|\n", one_line)))

        binary_output = ''
        
        correct = True

        #checking for empty lines
        if not len(one_line_data):
            continue

        temp_labels = list(map(lambda x: x+":", list(labels_pointer.keys())))
        if (one_line_data[0] in (All_Instructions+temp_labels)):
            correct *= True
        else:
            correct *= False

        if not correct:
            print(c.red(f"Error encountered at line {c.highlight_white(line+1)}"), end=", ")
            sg.suggestions_for(one_line_data[0])
        

        global_correct *= correct

        if not correct:
            continue



        if (one_line_data[0] in R_Type_Instructions):
            if check_registers(line, 1, 2, 3):
                continue
            binary_output += hot_fix_1(R_Type[one_line_data[0]]["opcode"], Registers[one_line_data[1]], R_Type[one_line_data[0]]["funct3"], Registers[one_line_data[2]], Registers[one_line_data[3]], R_Type[one_line_data[0]]["funct7"])

        elif (one_line_data[0] in I_Type_Instructions):
            if one_line_data[0] == "lw":
                if check_registers(line, 1, 3):
                    continue
                if (x:=int(one_line_data[2])) > (max:= 2**11 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                if (x:=int(one_line_data[2])) < (min:= -2**11):
                    print(c.red_a,f"Immediate value is smaller than allowed, minimum value is {c.highlight_white(min)}")
                    continue
                else:
                    x = twos_complement(12, x)
                    one_line_data[2] = '0'*(14-len(x))+x[2:]
          
                    binary_output += hot_fix_1(I_Type[one_line_data[0]]["opcode"], Registers[one_line_data[1]], I_Type[one_line_data[0]]["funct3"], Registers[one_line_data[3]], one_line_data[2])

            else:
                if check_registers(line, 1, 2):
                    continue
                if (x:=int(one_line_data[3])) > (max:=2**11 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                if (x:=int(one_line_data[3])) < (min:= -2**11):
                    print(c.red_a,f"Immediate value is smaller than allowed, minimum value is {c.highlight_white(min)}")
                    continue
                else:
                    x = twos_complement(12, x)
                    one_line_data[3] = '0'*(14-len(x))+x[2:]

                    binary_output += hot_fix_1(I_Type[one_line_data[0]]["opcode"], Registers[one_line_data[1]], I_Type[one_line_data[0]]["funct3"], Registers[one_line_data[2]], one_line_data[3])
      
                    
        elif (one_line_data[0] in S_Type_Instructions):
                if check_registers(line, 1, 3):
                    continue
                if (x:=int(one_line_data[2])) > (max:=2**11 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                if (x:=int(one_line_data[2])) < (min:= -2**11):
                    print(c.red_a,f"Immediate value is smaller than allowed, minimum value is {c.highlight_white(min)}")
                    continue
                else:
                    x = twos_complement(12, x)
                    one_line_data[2] = '0'*(14-len(x))+x[2:]
                    one_line_data[2] = one_line_data[2][::-1]

                binary_output += one_line_data[2][11:4:-1] + Registers[one_line_data[1]] + Registers[one_line_data[3]] + S_Type["sw"]["funct3"] + one_line_data[2][4::-1] + S_Type["sw"]["opcode"]


        elif (one_line_data[0] in B_Type_Instructions):
            if check_registers(line, 1, 2):
                continue
            try:
                if (x:=int(one_line_data[3])) > (max:=2**11 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                if (x:=int(one_line_data[3])) < (min:= -2**11):
                    print(c.red_a,f"Immediate value is smaller than allowed, minimum value is {c.highlight_white(min)}")
                    continue

            except ValueError:
                if ((x:=one_line_data[3]) in labels_pointer.keys()):
                    x = twos_complement(12, 4*line-labels_pointer[x])
                else:
                    global_correct = False
                    sg.suggestions_for(x, list(labels_pointer.keys()), "label")

            try:
                int(one_line_data[3])
                x = twos_complement(12, x)
            except ValueError:
                pass

            one_line_data[3] = '0'*(14-len(str(x)))+str(x)[2:]
            one_line_data[3] = one_line_data[3][::-1]

            binary_output +=  one_line_data[3][11] + one_line_data[3][9:3:-1] + Registers[one_line_data[2]] + Registers[one_line_data[1]] + B_Type[one_line_data[0]]["funct3"] + one_line_data[3][3::-1] + one_line_data[3][10] + B_Type[one_line_data[0]]["opcode"]

        elif (one_line_data[0] in U_Type_Instructions):
                if check_registers(line, 1):
                    continue

                if (x:=int(one_line_data[2])) > (max:=2**19 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                if (x:=int(one_line_data[2])) < (min:= -2**19):
                    print(c.red_a,f"Immediate value is smaller than allowed, minimum value is {c.highlight_white(min)}")
                    continue
                else:
                    x = twos_complement(20, x)
                    one_line_data[2] = '0'*(22-len(x))+x[2:]
                
                    binary_output += hot_fix_1(U_Type[one_line_data[0]]["opcode"], Registers[one_line_data[1]], one_line_data[2])

        elif (one_line_data[0] in J_Type_Instructions):
            if check_registers(line, 1):
                continue
            try:
                if (x:=int(one_line_data[2])) > (max:=2**19 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                if (x:=int(one_line_data[2])) < (min:= -2**19):
                    print(c.red_a,f"Immediate value is smaller than allowed, minimum value is {c.highlight_white(min)}")
                    continue

            except ValueError:
                if ((x:=one_line_data[2]) in labels_pointer.keys()):
                    x = twos_complement(20, 4*line-labels_pointer[x])
                else:
                    global_correct = False
                    sg.suggestions_for(x, list(labels_pointer.keys()), "label")
    
            try:
                int(one_line_data[2])
                x = twos_complement(20, x)
                one_line_data[2] = '0'*(22-len(x))+x[2:]
                one_line_data[2] = one_line_data[2][::-1]
            except ValueError:
                one_line_data[2] = '0'*(22-len(str(x)))+str(x)[2:]
                one_line_data[2] = one_line_data[2][::-1]

            binary_output += one_line_data[2][19] + one_line_data[2][9::-1] + one_line_data[2][10] + one_line_data[2][18:10:-1] + Registers[one_line_data[1]] + J_Type["jal"]["opcode"]

        binary_output_list.append(binary_output)

    if binary_output_list[-1] != "00000000000000000000000001100011":
        print(c.highlight_red("Virtual halt not found, binary cannot be created"))
        global_correct = False
    
    if global_correct:
        print("\x1b[32mNo errors detected, binary successfully created.\x1b[0m")
        for x in binary_output_list:
            if len(x) != 0:
                output_file_bin.write(x)
                output_file_bin.write("\n")
        
    output_file_bin.close()
