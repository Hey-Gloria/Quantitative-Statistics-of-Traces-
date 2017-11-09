# Quantitative-Statistics-of-Traces-
to collect the characteristics of the instructions of scripting languages running in the modern machine.


## [addressing.py]
A collection of functions used to analyze the oprands(shown as a string), including the addressing mode, the bit-length, ... <br> 
<br>
The ADDRESSING MODE part is based on the mode defined as the following(64-ia-32-architectures-software-developer‘s-manual):
 
1. The data for a source operand can be located in:
	* the instruction itself (an immediate operand)
	* a register
	* a memory location

2. `Immediate Operands`: Some instructions use data encoded in the instruction itself as a source operand.

3. `Register Operands` in 64-bit mode can be any of the following:
	* 64-bit general-purpose registers (RAX, RBX, RCX, RDX, RSI, RDI, RSP, RBP, or R8-R15)
	* 32-bit general-purpose registers (EAX, EBX, ECX, EDX, ESI, EDI, ESP, EBP, or R8D-R15D)
	* 16-bit general-purpose registers (AX, BX, CX, DX, SI, DI, SP, BP, or R8W-R15W)
	* 8-bit general-purpose registers: AL, BL, CL, DL, SIL, DIL, SPL, BPL, and R8L-R15L are available using REX prefixes; AL, BL, CL, DL, AH, BH, CH, DH are available without using REX prefixes.
	* Segment registers (CS, DS, SS, ES, FS, and GS)
	* RFLAGS register
	* x87 FPU registers (ST0 through ST7, status word, control word, tag word, data operand pointer, and instruction pointer)
	* MMX registers (MM0 through MM7)
	* XMM registers (XMM0 through XMM15) and the MXCSR register
	* Control registers (CR0, CR2, CR3, CR4, and CR8) and system table pointer registers (GDTR, LDTR, IDTR, and task register)
	* Debug registers (DR0, DR1, DR2, DR3, DR6, and DR7)
	* MSR registers
	* RDX:RAX register pair representing a 128-bit operand

4. For the `Memory Operands`, The offset part of a memory address can be specified directly as:
	* a static value (called a displacement)
	* or through an address computation made up of one or more of the following components:
		+ Displacement — A {None, 8-bit, 16-bit, 32-bit} value.
		+ Base — The value in a general-purpose register.
		+ Index — The value in a general-purpose register.
		+ Scale factor — A value of {1, 2, 4, 8} that is multiplied by the index value.

	Thus, the Offset (or Effective Address) Computation: `Offset = Base + (Index * Scale) + Displacement`.<br>
	For common combinations of address components, there are 6 addressing modes as following:
	1. Displacement -- An absolute/static address<br>
		A displacement alone represents a direct (uncomputed) offset to the operand.
	2. Base<br>
		A base alone represents an indirect offset to the operand.
	3. Base + Displacement
		* the EBP register is the best choice for the base register(automatically selects the stack segment)
	4. (Index * Scale) + Displacement
		* an efficient way to index into a static array when the element size is 2, 4, or 8 bytes.
	5. Base + Index + Displacement
		* either a two-dimensional array (the displacement holds the address of the beginning of the array)
		* or one of several instances of an array of records (the displacement is an offset to a field within the record).
	6. Base + (Index * Scale) + Displacement
		* efficient indexing of a two-dimensional array when the elements of the array are 2, 4, or 8 bytes in size.
<br>
For the ADDRESSING LENGTH part, the minimum length is set to be 0-bit(for 0x0), and the sign-bit are always ignored.<br>
We do this way to follow the example shown in Chapter 2 of `Computer architecture - a quantitative approach, 3rd Edition`.
	
## [statkit.py]
A collection of functions used to generate information-dictionary from trace file, or from the original info-dict.

At present, the information-dictionary holds the following data fields:
* `id`: the instruction id
* `lock`: = 1 if the instruction has a prefix-"lock"
* `rep`: = 1 if the instruction has a prefix-"rep"
* `instr`: the instrucion type
* `nOPs`: how many oprands it has
* `op1`, `op2`, `op3`: its oprands ("" for NULL, there may be 3 oprands for `imul`)
* `op1_mode`, `op2_mode`, `op3_mode`: the addressing mode of the oprand
* `nbytes`: the length of the instruciton (unit: byte)
* `byte0`, `byte1`, `...`: the binary representation of the instruction
* `addr`:
* `taken`: 1 means "taken", 0 means "not taken"
* `executed`: 1 means "executed", 0 means "not executed"

## [toolkit.py]
A collection of functions used to read/write files, or for data visualization
