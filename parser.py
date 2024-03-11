import re
from lookup import R_Type, I_Type, S_Type, B_Type, U_Type, J_Type, Registers
import suggester as sg

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
    filepath = input("Enter the address for the file: ")
    file = open(filepath, "r")
    data = file.readlines()
    file.close()

    output_file_bin = open("output_bin.txt", "w")

    binary_output_list = []

    c = sg.colors()
    
    global_correct = True
    for line, one_line in enumerate(data):
        one_line = one_line[:-1] # removing the \n at the end
        one_line_data = list(filter(lambda x: x, re.split(",| |\(|\)", one_line)))

        binary_output = ''
        
        correct = True

        if (one_line_data[0] in All_Instructions):
            correct *= True
        else:
            correct *= False

        if not correct:
            print(c.red(f"Error incountered at line {c.highlight_white(line+1)}"), end=", ")
            sg.suggestions_for(one_line_data[0])
        

        only_registers = filter(lambda x: x[0] in "abcdefghijklmnopqrstuvwxyz", one_line_data[1:])
        
        for i in only_registers:
            if (i not in Unique_Registers):
                correct *= False
                print(c.red(f"Error encountered at line {c.highlight_white(line+1)}, given register {c.highlight_white(i)} does not match any know register."))

        if not correct:
            continue

        #checking for a label
        if one_line_data[0][-1] == ":": 
            continue 

        if (one_line_data[0] in R_Type_Instructions):
            binary_output += R_Type[one_line_data[0]]["opcode"] + Registers[one_line_data[1]] + R_Type[one_line_data[0]]["funct3"] + Registers[one_line_data[2]] + Registers[one_line_data[3]] + R_Type[one_line_data[0]]["funct7"]

        elif (one_line_data[0] in I_Type_Instructions):
            if one_line_data[0] == "lw":
                if (x:=int(one_line_data[2])) > (max:=2**12 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                else:
                    one_line_data[2] = '0'*(14-len(bin(x)))+bin(x)[2:]
          
                    binary_output += I_Type[one_line_data[0]]["opcode"] + Registers[one_line_data[1]] + I_Type[one_line_data[0]]["funct3"] + Registers[one_line_data[3]] + one_line_data[2]

            else:
                if (x:=int(one_line_data[3])) > (max:=2**12 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                else:
                    one_line_data[3] = '0'*(14-len(bin(x)))+bin(x)[2:]
          
                    binary_output += I_Type[one_line_data[0]]["opcode"] + Registers[one_line_data[1]] + I_Type[one_line_data[0]]["funct3"] + Registers[one_line_data[2]] + one_line_data[3]
      
                    
        elif (one_line_data[0] in S_Type_Instructions):
                if (x:=int(one_line_data[2])) > (max:=2**12 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                else:
                    one_line_data[2] = '0'*(14-len(bin(x)))+bin(x)[2:]
          
                    binary_output += S_Type["sw"]["opcode"] + one_line_data[2][0:4] + S_Type["sw"]["funct3"] + Registers[one_line_data[1]] + Registers[one_line_data[3]] + one_line_data[5:11]

        elif (one_line_data[0] in B_Type_Instructions):
                if (x:=int(one_line_data[3])) > (max:=2**12 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                else:
                    one_line_data[3] = '0'*(14-len(bin(x)))+bin(x)[2:]
          
                    binary_output += B_Type[one_line_data[0]]["opcode"] + one_line_data[3][10] + one_line_data[3][0:4] + B_Type[one_line_data[0]]["funct3"] + Registers[one_line_data[1]] + Registers[one_line_data[2]] + one_line_data[3][4:10] + one_line_data[3][11]

        elif (one_line_data[0] in U_Type_Instructions):
                if (x:=int(one_line_data[2])) > (max:=2**20 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                else:
                    one_line_data[2] = '0'*(22-len(bin(x)))+bin(x)[2:]
          
                    binary_output += U_Type[one_line_data[0]]["opcode"] + Registers[one_line_data[1]] + one_line_data[2]

        elif (one_line_data[0] in J_Type_Instructions):
                if (x:=int(one_line_data[2])) > (max:=2**20 - 1):
                    print(c.red_a,f"Immediate value is larger than allowed, maximum value is {c.highlight_white(max)}")
                    continue
                else:
                    one_line_data[2] = '0'*(22-len(bin(x)))+bin(x)[2:]

                    binary_output += J_Type["jal"]["opcode"] + Registers[one_line_data[1]] + one_line_data[2][11:19] + one_line_data[2][10] + one_line_data[2][0:9] + one_line_data[2][19]

        binary_output_list.append(binary_output)
        global_correct *= correct

    
    if global_correct:
        print("\x1b[32mNo errors detected, binary succesfully created.\x1b[0m")
        for x in binary_output_list:
            output_file_bin.write(x)
            output_file_bin.write("\n")
        
    output_file_bin.close()
