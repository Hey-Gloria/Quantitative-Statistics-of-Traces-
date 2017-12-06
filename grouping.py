# -*- coding:UTF-8 -*-
import sys, re
reload(sys)
sys.setdefaultencoding('utf-8')

#############################################
#
#   PART 1: General-Purpose Instructions
#
#############################################

# 1. Data Transfer
data_transfer_instructions = [
    "mov",
    "cmove", "cmovz", "cmovne", "cmovnz",
    "cmova", "cmovnbe", "cmovae", "cmovnb", "cmovb", "cmovnae", "cmovbe", "cmovna",
    "cmovg", "cmovnle", "cmovge", "cmovnl", "cmovl", "cmovnge", "cmovle", "cmovng",
    "cmovc", "cmovnc", "cmovo", "cmovno",
    "cmovs", "cmovns",
    "cmovp", "cmovpe", "cmovnp", "cmovpo",
    "xchg", "bswap", "xadd",
    "cmpxchg", "cmpxchg8b",
    "push", "pop", "pusha", "pushad", "popa", "popad",
    "cwd", "cdq", "cbw", "cwde",
    "movsx", "movzx",
    ]

# 2. Binary Arithmetic
binary_arithmetic_instructions = [
    "adcx", "adox",
    "add", "adc",
    "sub", "sbb",
    "imul", "mul",
    "idiv", "div",
    "inc", "dec",
    "neg",
    "cmp",
    ]

# 3. Decimal Arithmetic
decimal_arithmetic_instructions = [
    "daa", "das",
    "aaa", "aas", "aam", "aad",
]

# 4. logical
logical_instructions = [
    "and", "or", "xor", "not"
    ]

# 5. shift and rotate
shift_and_rotate_instructions = [
    "sar", "shr", "sal", "shl", "shrd", "shld", 
    "ror", "rol", "rcr", "rcl", 
    ]

# 6. bit and byte
bit_and_byte_instructions = [
    "bt", "bts", "btr", "btc", "bsf", "bsr", 
    "sete", "setz", "setne", "setnz",
    "seta", "setnbe", "setae", "setnb", "setb", "setnae", "setbe", "setna", 
    "setg", "setnle", "setge", "setnl", "setl", "setnge", "setle", "setng", 
    "setnc", "setc", "sets", "setns", "seto", "setno",
    "setpe", "setp", "setpo", "setnp",
    "test",
    "crc32",
    "popcnt", 
    ]

# 7. Control Transfer
control_transfer_instructions = [
    "jmp", 
    "je", "jz", "jne", "jnz", 
    "ja", "jnbe", "jae", "jnb", "jb", "jnae", "jbe", "jna", 
    "jg", "jnle", "jge", "jnl", "jl", "jnge", "jle", "jng", 
    "jc", "jnc", "jo", "jno", "js", "jns", "jpo", "jnp", "jpe", "jp", 
    "jcxz", "jecxz", 
    "loop", "loopz", "loope", "loopnz", "loopne", 
    "call", "ret", "iret", "int", "into", "bound", 
    "enter", "leave", 
    ]

# 8. String
string_instructions = [
    "movs", "movsb", "movsw", "movsd",
    "cmps", "cmpsb", "cmpsw", "cmpsd",
    "scas", "scasb", "scasw", "scasd",
    "lods", "lodsb", "lodsw", "lodsd",
    "stos", "stosb", "stosw", "stosd",
    "rep", "repe", "repz", "repne", "repnz",
    ]

# 9. I/O
input_and_output_instructions = [
    "in", "out", 
    "ins", "insb", "insw", "insd",
    "outs", "outsb", "outsw", "outsd",
    ]

# 10. Enter and Leave
enter_and_leave_instructions = [
    "enter", "leave"
    ]

# 11. Flag Control
flag_control_instructions = [
    "stc", "clc", "cmc", 
    "cld", "std", 
    "lahf", "sahf", 
    "pushf", "pushfd", 
    "popf", "popfd", 
    "sti", "cli", 
    ]

# 12. Segment Register
segment_register_instructions = [
    "lds", "les", "lfs", "lgs", "lss"
    ]

# 13. Miscellaneous
miscellaneous_instructions = [
    "lea",
    "nop",
    "ud2",
    "xlat", "xlatb",
    "cpuid",
    "movbe",
    "prefetchw", "prefetchwt1",
    "clflush", "clflushopt",
    ]

# 14. User Mode Extended Sate Save and Restore
user_mode_extended_sate_save_and_restore_instructions = [
    "xsave", "xsavec", "xsaveopt",
    "xrstor", "xgetbv"
    ]

# 15. Random Number Generator
random_number_generator_instructions = [
    "rdrand", "rdseed"
    ]

# 16. BMI1, BMI2
bmi1_bmi2_instructions = [
    "andn", 
    "bextr", "blsi", "blsmsk", "blsr", "bzhi", 
    "lzcnt", 
    "mulx", 
    "pdep", "pext", 
    "rorx", 
    "sarx", "shlx", "shrx", 
    "tzcnt",
    ]

General_Purpose_Instructions = [
    data_transfer_instructions,
    binary_arithmetic_instructions,
    decimal_arithmetic_instructions,
    logical_instructions,
    shift_and_rotate_instructions,
    bit_and_byte_instructions,
    control_transfer_instructions,
    string_instructions,
    input_and_output_instructions,
    enter_and_leave_instructions,
    flag_control_instructions,
    segment_register_instructions,
    miscellaneous_instructions,
    user_mode_extended_sate_save_and_restore_instructions,
    random_number_generator_instructions,
    bmi1_bmi2_instructions,
    ]


#############################################
#
#   PART 2: X87 FPU Instructions
# 
#           X87 FPU AND SIMD STATE MANAGEMENT INSTRUCTIONS
#
#############################################

# 1. x87 FPU Data Transfer Instructions
x87_data_transfer = [
    "fld", "fst", "fstp", 
    "fild", "fist", "fistp",
    "fbld", "fbstp",
    "fxch", 
    "fcmove", "fcmovne", "fcmovb", "fcmovbe", "fcmovnb", "fcmovenbe", "fcmovu", "fcmovnu",
    ]

# 2. x87 FPU Basic Arithmetic Instructions
x87_arithmetic = [
    "fadd", "faddp", "fiadd", 
    "fsub", "fsubp", "fisub", "fsubr", "fsubrp", "fisubr",
    "fmul", "fmulp", "fimul",
    "fdiv", "fdivp", "fidiv", "fdivr", "fdivrp", "fidivr",
    "fprem", "fprem1",
    "fabs", "fchs", "frndint", "fscale", "fsqrt", "fxtract",
    ]

# 3. x87 FPU Comparison Instructions
x87_comparison = [
    "fcom", "fcomp", "fcompp", 
    "fucom", "fucomp", "fucompp",
    "ficom", "ficomp", 
    "fcomi", "fucomi", "fcomip", "fucomip",
    "ftst", "fxam",
    ]

# 4. x87 FPU Transcendental Instructions
x87_transcendental = [
    "fsin", "fcos", "fsincos", 
    "fptan", "fpatan",
    "f2xm1", "fyl2x", "fyl2xp1",
    ]

# 5. x87 FPU Load Constants Instructions
x87_load_constants = [
    "fld1", "fldz", 
    "fldpi", 
    "fldl2e", "fldln2", "fldl2t", "fldlg2",
    ]

# 6. x87 FPU Control Instructions
x87_control = [
    "fincstp", "fdecstp", 
    "ffree", 
    "finit", "fninit", "fclex", "fnclex", 
    "fstcw", "fnstcw", "fldcw",
    "fstenv", "fnstenv", "fldenv", 
    "fsave", "fnsave",
    "frstor", "fstsw", "fnstsw",
    "wait", "fwait", "fnop",
    ]

# 7. X87 FPU AND SIMD STATE MANAGEMENT INSTRUCTIONS
x87_FPU_SIMD_state_management = [
    "fxsave", "fxrstor",
    ]

X87_FPU_Instructions = [
    x87_data_transfer, 
    x87_arithmetic,
    x87_comparison,
    x87_transcendental,
    x87_load_constants,
    x87_control,
    x87_FPU_SIMD_state_management,
    ]






allSet = [
    General_Purpose_Instructions,
    X87_FPU_Instructions,
]


f_map_name = "/Users/Gloria/Desktop/instruction_map.c"
name_dict = []


with open(f_map_name) as f:
    for line in f:
        names = re.findall(r'\"(\w*)\"', line)
        for name in names:

            setSkip = False
            for oneSet in allSet:
                skip = False
                for oneList in oneSet:
                    if name in oneList:
                        skip = True
                        break
                if skip:
                    setSkip = True
                    break
            if setSkip: continue

            name_dict.append(name)
    f.close()

name_dict.sort()
for name in name_dict:
    print name
