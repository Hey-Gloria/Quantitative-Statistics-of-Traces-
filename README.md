# Quantitative-Statistics-of-Traces-
to collect the characteristics of the instructions of scripting languages running in the modern machine.


##[addressing.py]
A collection of functions used to determine the addressing mode of a string.
This part is based on the mode defined as the following(64-ia-32-architectures-software-developer‘s-manual):

1. The offset part of a memory address can be specified directly as:
	* a static value (called a displacement)
	* or through an address computation made up of one or more of the following components:
		• Displacement — An 8-, 16-, or 32-bit value.
		• Base — The value in a general-purpose register.
		• Index — The value in a general-purpose register.
		• Scale factor — A value of 2, 4, or 8 that is multiplied by the index value.

	Thus, the Offset (or Effective Address) Computation:
		Offset = Base + (Index * Scale) + Displacement
	
	Also, for each part of the computation formula, there are some limitations:
	1. Base: the Base should be one of {EAX, EBX, ECX, EDX, ESP, EBP, ESI, EDI}
	2. Index: the Index should be one of {EAX, EBX, ECX, EDX, EBP, ESI, EDI}
		* the ESP cannot be used as an index register
	3. Scale: the Scale should be one of {1, 2, 4, 8}
	4. Displacement: the Displacement should be one of {None, 8-bit, 16-bit, 32-bit}

2. The 6 types of addressing mode defined in Intel's Manual:
	(1).Displacement -- An absolute/static address
		A displacement alone represents a direct (uncomputed) offset to the operand.
	(2).Base
		A base alone represents an indirect offset to the operand.
	(3).Base + Displacement
		* the EBP register is the best choice for the base register(automatically selects the stack segment)
	(4).(Index * Scale) + Displacement
		* an efficient way to index into a static array when the element size is 2, 4, or 8 bytes.
	(5).Base + Index + Displacement
		* either a two-dimensional array (the displacement holds the address of the beginning of the array)
		* or one of several instances of an array of records (the displacement is an offset to a field within the record).
	(6).Base + (Index * Scale) + Displacement
		* efficient indexing of a two-dimensional array when the elements of the array are 2, 4, or 8 bytes in size.

