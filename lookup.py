'''
A lookup table which contains all the binary encodings of every instruction.
'''

R_Type = {
        "add": {"opcode": "0110011", "funct3": "000", "funct7": "0000000"},
        "sub": {"opcode": "0110011", "funct3": "000", "funct7": "0100000"},
        "sll": {"opcode": "0110011", "funct3": "001", "funct7": "0000000"},
        "slt": {"opcode": "0110011", "funct3": "010", "funct7": "0000000"},
        "sltu": {"opcode": "0110011", "funct3": "011", "funct7": "0000000"},
        "xor": {"opcode": "0110011", "funct3": "100", "funct7": "0000000"},
        "srl": {"opcode": "0110011", "funct3": "101", "funct7": "0000000"},
        "or": {"opcode": "0110011", "funct3": "110", "funct7": "0000000"},
        "and": {"opcode": "0110011", "funct3": "111", "funct7": "0000000"}

}

I_Type = {
        "lw": {"opcode": "0000011", "funct3": "010"},
        "lb": {"opcode": "0000011", "funct3": "010"},
        "lh": {"opcode": "0000011", "funct3": "010"}, 
        "ld": {"opcode": "0000011", "funct3": "010"},
        "addi": {"opcode": "0010011", "funct3": "000"},
        "sltiu": {"opcode": "0010011", "funct3": "011"},
        "jalr": {"opcode": "1100111", "funct3": "000"}
}

S_Type = {
        "sw": {"opcode": "0100011", "funct3": "010"}
}

B_Type = {
    "beq": {"opcode": "1100011", "funct3": "000"},
    "bne": {"opcode": "1100011", "funct3": "001"},
    "blt": {"opcode": "1100011", "funct3": "100"},
    "bge": {"opcode": "1100011", "funct3": "101"},
    "bltu": {"opcode": "1100011", "funct3": "110"},
    "bgeu": {"opcode": "1100011", "funct3": "111"}
}

U_Type = {
    "lui": {"opcode": "0110111"},
    "auipc": {"opcode": "0010111"}
}

J_Type = {
        "jal": {"opcode": "1101111"}
}

Registers = {
    "zero": "00000",
    "ra": "00001",
    "sp": "00010",
    "gp": "00011",
    "tp": "00100",
    "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "s0": "01000",
    "fp": "01000",
    "s1": "01001",
    "a0": "01010",
    "a1": "01011",
    "a2": "01100",
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",
    "s2": "10010",
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",
    "t3": "11100",
    "t4": "11101",
    "t5": "11110",
    "t6": "11111"
}

