# import parser as ps


# if __name__ == "__main__":
#     all_instructions = ps.R_Type_Instructions + ps.I_Type_Instructions + ps.S_Type_Instructions + ps.B_Type_Instructions + ps.U_Type_Instructions + ps.J_Type_Instructions + ps.Bonus
#     print(all_instructions)
#     def suggester_f(instruction):
#         def suggester(i):
#                 count = 0
#                 for x in instruction:
#                     if (x in i):
#                         count += 1
#                 return count
#         return suggester
    
#     def suggest(instruction):
#         suggester = suggester_f(instruction)
#         all_instructions = list(filter(lambda x: suggester(x)>len(x)-2, all_instructions))
#         all_instructions.sort(key=suggester, reverse=True)
#         print(f"{instruction} did not match any known instruction, perhaps you meant") 
#         print(*all_instructions, sep=", ")

#     suggest("adb")

import parser as ps
# import sys

def suggestions_for(instruction):
    all_instructions = ps.R_Type_Instructions + ps.I_Type_Instructions + ps.S_Type_Instructions + ps.B_Type_Instructions + ps.U_Type_Instructions + ps.J_Type_Instructions + ps.Bonus

    # instruction = sys.argv[1]

    def suggester_f(instruction):
        def suggester(i):
                count = 0
                for x in instruction:
                    if (x in i):
                        count += 1
                return count
        return suggester

    suggester = suggester_f(instruction)
    all_instructions.sort(key=suggester, reverse=True)
    all_instructions = filter(lambda x: suggester(x)>len(x)-2, all_instructions)
    print(f"{instruction} did not match any known instruction, perhaps you meant") 
    print(*all_instructions, sep=", ")
