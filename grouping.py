# -*- coding:UTF-8 -*-
import sys, re
reload(sys)
sys.setdefaultencoding('utf-8')

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








