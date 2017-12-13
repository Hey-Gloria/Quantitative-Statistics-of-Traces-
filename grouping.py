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


#############################################
#
#   PART 3: MMX Instructions
#
#############################################

# 1. MMX Data Transfer Instructions
mmx_data_transfer = [
    "movd", "movq",
    ]

# 2. MMX Conversion Instructions
mmx_conversion = [
    "packsswb", "packssdw", "packuswb",
    "punpckhbw", "punpckhwd", "punpckhdq",
    "punpcklbw", "punpcklwd", "punpckldq",
    ]

# 3. MMX Packed Arithmetic Instructions
mmx_packed_arithmetic = [
    "paddb", "paddw", "paddd",
    "paddsb", "paddsw", "paddusb", "paddusw",
    "psubb", "psubw", "psubd",
    "psubsb", "psubsw", "psubusb", "psubusw",
    "pmulhw", "pmullw", 
    "pmaddwd",
    ]

# 4. MMX Comparison Instructions
mmx_comparison = [
    "pcmpeqb", "pcmpeqw", "pcmpeqd", 
    "pcmpgtb", "pcmpgtw", "pcmpgtd",
    ]

# 5. MMX Logical Instructions
mmx_logical = [
    "pand", "pandn", "por", "pxor",
    ]

# 6. MMX Shift and Rotate Instructions
mmx_shift_and_rotate = [
    "psllw", "pslld", "psllq",
    "psrlw", "psrld", "psrlq",
    "psraw", "psrad",
    ]

# 7. MMX State Management Instructions
mmx_state_management = [
    "emms",
    ]

MMX_Instructions = [
    mmx_data_transfer,
    mmx_conversion,
    mmx_packed_arithmetic,
    mmx_comparison,
    mmx_logical,
    mmx_shift_and_rotate,
    mmx_state_management,
    ]


#############################################
#
#   PART 4: SSE INSTRUCTIONS
#
#############################################

# SSE SIMD Single-Precision Floating-Point Instructions
# 1. SSE Data Transfer Instructions
sse_data_transfer = [
    "movaps", "movups", 
    "movhps", "movhlps", "movlps", "movlhps",
    "movmskps", "movss",
    ]

# SSE SIMD Single-Precision Floating-Point Instructions
# 2. SSE Packed Arithmetic Instructions
sse_packed_arithmetic = [
    "addps", "addss",
    "subps", "subss",
    "mulps", "mulss",
    "divps", "divss",
    "rcpps", "rcpss",
    "sqrtps", "sqrtss", "rsqrtps", "rsqrtss",
    "maxps", "maxss", "minps", "minss",
    ]

# SSE SIMD Single-Precision Floating-Point Instructions
# 3. SSE Comparison Instructions
sse_comparison = [
    "cmpps", "cmpss",
    "comiss", "ucomiss",
    ]

# SSE SIMD Single-Precision Floating-Point Instructions
# 4. SSE Logical Instructions
sse_logical = [
    "andps", "andnps", "orps", "xorps",
    ]

# SSE SIMD Single-Precision Floating-Point Instructions
# 5. SSE Shuffle and Unpack Instructions
sse_shuffle_and_unpack = [
    "shufps", 
    "unpckhps", "unpcklps",
    ]

# SSE SIMD Single-Precision Floating-Point Instructions
# 6. SSE Conversion Instructions
sse_conversion = [
    "cvtpi2ps", "cvtsi2ss", "cvtps2pi", "cvtss2si",
    "cvttps2pi", "cvttss2si",
    ]

# 7. SSE MXCSR State Management Instructions
sse_mxcsr_state_management = [
    "ldmxcsr", "stmxcsr",
    ]

# 8. SSE 64-Bit SIMD Integer Instructions
sse_simd_integer = [
    "pavgb", "pavgw",
    "pextrw", "pinsrw", 
    "pmaxub", "pmaxsw", "pminub", "pminsw",
    "pmovmskb", 
    "pmulhuw", 
    "psadbw",
    "pshufw",
    ]

# 9. SSE Cacheability Control, Prefetch, and Instruction Ordering Instructions
sse_cache_prefetch_ordering = [
    "maskmovq",
    "movntq", "movntps", 
    "prefetchh",
    "sfence",
    ]


SSE_Instrutions = [
    sse_data_transfer,
    sse_packed_arithmetic,
    sse_comparison,
    sse_logical,
    sse_shuffle_and_unpack,
    sse_conversion,
    sse_mxcsr_state_management,
    sse_simd_integer,
    sse_cache_prefetch_ordering,
    ]


#############################################
#
#   PART 5: SSE2 INSTRUCTIONS
#
#############################################

# SSE2 Packed and Scalar Double-Precision Floating-Point Instructions
# 1. SSE2 Data Movement Instructions
sse2_data_movement = [
    "movapd", "movupd", "movhpd", "movlpd", 
    "movmskpd", 
    "movsd", 
    ]

# SSE2 Packed and Scalar Double-Precision Floating-Point Instructions
# 2. SSE2 Packed Arithmetic Instructions
sse2_packed_arithmetic = [
    "addpd", "addsd", 
    "subpd", "subsd",
    "mulpd", "mulsd",
    "divpd", "divsd",
    "sqrtpd", "sqrtsd",
    "maxpd", "maxsd", "minpd", "minsd",
    ]

# SSE2 Packed and Scalar Double-Precision Floating-Point Instructions
# 3. SSE2 Logical Instructions
sse2_logical = [
    "andpd", "andnpd", 
    "orpd", "xorpd",
    ]

# SSE2 Packed and Scalar Double-Precision Floating-Point Instructions
# 4. SSE2 Compare Instructions
sse2_compare = [
    "cmppd", "cmpsd",
    "comisd", "ucomisd",
    ]

# SSE2 Packed and Scalar Double-Precision Floating-Point Instructions
# 5. SSE2 Shuffle and Unpack Instructions
sse2_shuffle_and_unpack = [
    "shufpd", 
    "unpckhpd", "unpcklpd",
    ]

# SSE2 Packed and Scalar Double-Precision Floating-Point Instructions
# 6. SSE2 Conversion Instructions
sse2_conversion = [
    "cvtpd2pi", "cvttpd2pi", "cvtpi2pd", 
    "cvtpd2dq", "cvttpd2dq", "cvtdq2pd",
    "cvtps2pd", "cvtpd2ps",
    "cvtss2sd", "cvtsd2ss", 
    "cvtsd2si", "cvttsd2si", "cvtsi2sd",
    ]

# 7. SSE2 Packed Single-Precision Floating-Point Instructions
sse2_packed_sp_fp = [
    "cvtdq2ps", "cvtps2dq", "cvttps2dq",
    ]

# 8. SSE2 128-Bit SIMD Integer Instructions
sse2_simd_integer = [
    "movdqa", "movdqu", 
    "movq2dq", "movdq2q",
    "pmuludq",
    "paddq", "psubq", 
    "pshuflw", "pshufhw", 
    "pshufd",
    "pslldq", "psrldq",
    "punpckhqdq", "punpcklqdq",
    ]

# 9. SSE2 Cacheability Control and Ordering Instructions
sse2_cache_ordering = [
    "clflush",
    "lfence", "mfence",
    "pause", 
    "maskmovdqu",
    "movntpd", "movntdq", "movnti",
    ]

SSE2_Instructions = [
    sse2_data_movement,
    sse2_packed_arithmetic,
    sse2_logical,
    sse2_compare,
    sse2_shuffle_and_unpack,
    sse2_conversion,
    sse2_packed_sp_fp,
    sse2_simd_integer,
    sse2_cache_ordering,
    ]


#############################################
#
#   PART 6: SSE3 INSTRUCTIONS
#
#############################################

# 1. SSE3 x87-FP Integer Conversion Instruction
sse3_conversion = [
    "fisttp",
    ]

# 2. SSE3 Specialized 128-bit Unaligned Data Load Instruction
sse3_unaligned_data_load = [
    "lddqu",
    ]

# 3. SSE3 SIMD Floating-Point Packed ADD/SUB Instructions
sse3_packed_add_and_sub = [
    "addsubps", "addsubpd",
    ]

# 4. SSE3 SIMD Floating-Point Horizontal ADD/SUB Instructions
sse3_horizontal_add_and_sub = [
    "haddps", "hsubps", "haddpd", "hsubpd",
    ]

# 5. SSE3 SIMD Floating-Point LOAD/MOVE/DUPLICATE Instructions
sse3_load_move_dup = [
    "movshdup", "movsldup", "movddup",
    ]

# 6. SSE3 Agent Synchronization Instructions
sse3_agent_synchronization = [
    "monitor",
    "mwait",
    ]

SSE3_Instructions = [
    sse3_conversion,
    sse3_unaligned_data_load,
    sse3_packed_add_and_sub,
    sse3_horizontal_add_and_sub,
    sse3_load_move_dup,
    sse3_agent_synchronization,
    ]


#############################################
#
#   PART 7: SUPPLEMENTAL STREAMING SIMD EXTENSIONS 3 (SSSE3) INSTRUCTIONS
#           SSSE3
#
#############################################

# 1. Horizontal Addition/Subtraction
ssse3_horizontal_add_and_sub = [
    "phaddw", "phaddsw", "phaddd",
    "phsubw", "phsubsw", "phsubd",
    ]

# 2. Packed Absolute Values
#   Multiply and Add Packed Signed and Unsigned Bytes
#   Packed Multiply High with Round and Scale
#   Packed Shuffle Bytes
#   Packed Sign
#   Packed Align Right
ssse3_packed = [
    "pabsb", "pabsw", "pabsd",
    "pmaddubsw",
    "pmulhrsw",
    "pshufb",
    "psignb", "psignw", "psignd",
    "palignr",
    ]

SSSE3_Instructions = [
    ssse3_horizontal_add_and_sub,
    ssse3_packed,
    ]


#############################################
#
#   PART 8: SSE4.1 INSTRUCTIONS
#
#############################################

# 1.Dword Multiply Instructions
sse4_1_dword_multiply = [
    "pmulld",
    "pmuldq",
    ]

# 2.Floating-Point Dot Product Instructions
sse4_1_fp_dot_product = [
    "dppd", "dpps",
    ]

# 3.Streaming Load Hint Instruction
sse4_1_streaming_load_hint = [
    "movntdqa",
    ]

# 4.Packed Blending Instructions
sse4_1_packed_blending = [
    "blendpd", "blendps",
    "blendvpd", "blendvps",
    "pblendvb", "pblendw",
    ]

# 5.Packed Integer MIN/MAX Instructions
sse4_1_packed_integer_min_max = [
    "pminuw", "pminud", 
    "pminsb", "pminsd",
    "pmaxuw", "pmaxud",
    "pmaxsb", "pmaxsd",
    ]

# 6.Floating-Point Round Instructions with Selectable Rounding Mode
sse4_1_fp_round = [
    "roundps", "roundpd",
    "roundss", "roundsd",
    ]

# 7.Insertion and Extractions from XMM Registers
sse4_1_insertion_extraction_xmm = [
    "extractps", "insertps",
    "pinsrb", "pinsrd", "pinsrq",
    "pextrb", "pextrw", "pextrd", "pextrq",
    ]

# 8.Packed Integer Format Conversions
sse4_1_packed_integer_format_conversions = [
    "pmovsxbw", "pmovzxbw",
    "pmovsxbd", "pmovzxbd",
    "pmovsxwd", "pmovzxwd",
    "pmovsxbq", "pmovzxbq",
    "pmovsxwq", "pmovzxwq",
    "pmovsxdq", "pmovzxdq",
    ]

# 9.Improved Sums of Absolute Differences (SAD) for 4-Byte Blocks
sse4_1_sum_absolute_differences = [
    "mpsadbw",
    ]

# 10.Horizontal Search
sse4_1_horizontal_search = [
    "phminposuw",
    ]

# 11.Packed Test
sse4_1_packed_test = [
    "ptest",
    ]

# 12.Packed Qword Equality Comparisons
sse4_1_packed_qword_equality_comparisons = [
    "pcmpeqq",
    ]

# 13.Dword Packing With Unsigned Saturation
sse4_1_dword_packing_unsigned_saturation = [
    "packusdw",
    ]

SSE4_1_Instructions = [
    sse4_1_dword_multiply,
    sse4_1_fp_dot_product,
    sse4_1_streaming_load_hint,
    sse4_1_packed_blending,
    sse4_1_packed_integer_min_max,
    sse4_1_fp_round,
    sse4_1_insertion_extraction_xmm,
    sse4_1_packed_integer_format_conversions,
    sse4_1_sum_absolute_differences,
    sse4_1_horizontal_search,
    sse4_1_packed_test,
    sse4_1_packed_qword_equality_comparisons,
    sse4_1_dword_packing_unsigned_saturation,
    ]


#############################################
#
#   PART 9: SSE4.2 INSTRUCTIONS
#
#############################################

# 1.String and Text Processing Instructions
sse4_2_string_text_processing = [
    "pcmpestri", "pcmpestrm",
    "pcmpistri", "pcmpistrm",
    ]

# 2.Packed Comparison SIMD integer Instruction
sse4_2_packed_comparison_SIMD_integer = [
    "pcmpgtq",
    ]

SSE4_2_Instructions = [
    sse4_2_string_text_processing,
    sse4_2_packed_comparison_SIMD_integer,
    ]


#############################################
#
#   PART 10: VIRTUAL-MACHINE EXTENSIONS
#
#############################################

# 1. VMCS-maintenance instructions
vmcs_maintenance = [
    "vmptrld", "vmptrst", 
    "vmclear", "vmread", "vmwrite",
    ]

# 2. VMX management
vmx_management = [
    "vmlaunch", "vmresume",
    "vmxoff", "vmxon",
    ]

# 3. VMX-specific TLB-management
vmx_specific_tlb_management = [
    "invept",  
    "invvpid",
    ]

# 4. guest-available instructions
vm_guest_available = [
    "vmcall",
    "vmfunc",
    ]

Virtual_Machine_Extensions_Instructions = [
    vmcs_maintenance,
    vmx_management,
    vmx_specific_tlb_management,
    vm_guest_available,
    ]


#############################################
#
#   PART 11: Other Extensions
#
#############################################

# 5.12 AESNI AND PCLMULQDQ
aesni_pclmulqdq = [
    "aesdec", "aesdeclast",
    "aesenc", "aesenclast",
    "aesimc",
    "aeskeygenassist",
    "pclmulqdq",
    ]

# 5.14 16-BIT FLOATING-POINT CONVERSION
fp_conversion_16bit = [
    "vcvtph2ps", "vcvtps2ph",
    ]

# 5.17 INTEL® TRANSACTIONAL SYNCHRONIZATION EXTENSIONS (TSX)
transactional_synchronization_extensions = [
    "xabort",
    "xacquire", "xrelease",
    "xbegin", "xend", 
    "xtest",
    ]

# 5.18 SYSTEM INSTRUCTIONS
# mov: Load and store control registers
# mov: Load and store debug registers
# lock(prefix): Lock Bus
system_instructions = [
    "clac", "stac",
    "lgdt", "sgdt",
    "lldt", "sldt",
    "ltr", "str",
    "lidt", "sidt",
    "mov",
    "lmsw", "smsw",
    "clts",
    "arpl",
    "lar", 
    "lsl",
    "verr", "verw",
    "mov",
    "invd", "wbinvd",
    "invlpg", "invpcid",
    "lock",
    "hlt",
    "rsm",
    "rdmsr", "wrmsr",
    "rdpmc",
    "rdtsc", "rdtscp",
    "sysenter", "sysexit",
    "xsave", "xsavec", "xsaveopt", "xsaves",
    "xrstor", "xrstors", 
    "xgetbv", "xsetbv",
    "rdfsbase", "rdgsbase",
    "wrfsbase", "wrgsbase",
    ]

# 5.19 64-BIT MODE INSTRUCTIONS
# movzx(64-bits): Move bytes/words to doublewords/quadwords, zero-extension
mode_64bit = [
    "cdqe", 
    "cmpsq", "cmpxchg16b",
    "lodsq", "movsq", "stosq",
    "movzx", 
    "swapgs",
    "syscall", "sysret",
    ]

# 5.22 INTEL® MEMORY PROTECTION EXTENSIONS
# bndmov: Copy or load from memory of the LowerBound and UpperBound to a register.
# bndmov: Store to memory of the LowerBound and UpperBound from a register.
memory_protection_extensions = [
    "bndmk",
    "bndcl", "bndcu", "bndcn", 
    "bndmov",
    "bndmov",
    "bndldx", "bndstx",
    ]

Other_Extension_Instructions = [
    aesni_pclmulqdq,
    fp_conversion_16bit,
    transactional_synchronization_extensions,
    system_instructions,
    mode_64bit,
    memory_protection_extensions,
    ]


#############################################

allSet = [
    General_Purpose_Instructions,
    X87_FPU_Instructions,
    MMX_Instructions,
    SSE_Instrutions,
    SSE2_Instructions,
    SSE3_Instructions,
    SSSE3_Instructions,
    SSE4_1_Instructions,
    SSE4_2_Instructions,
    Virtual_Machine_Extensions_Instructions,
    Other_Extension_Instructions,
]

# 5.13 AVX     Table 14-2,3,4,5,6,7
# 5.15 FMA     Table 14-15,
# 5.16 AVX2    Table 14-18,19
# 5.21 SAFER MODE EXTENSIONS
# 5.23 INTEL® SECURITY GUARD EXTENSIONS





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
