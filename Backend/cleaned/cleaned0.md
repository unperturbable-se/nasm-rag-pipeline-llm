# NASM – The Netwide Assembler
**version 3.02**

© 1996-2025 The NASM Development Team — All Rights Reserved
This document is redistributable under the license given in the section "License".

## Contents
* **Chapter 1: Introduction** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
  * **1.1 What Is NASM?** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
    * **1.1.1 License** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
* **Chapter 2: Running NASM** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
  * **2.1 NASM Command-Line Syntax** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
    * **2.1.1 The -o Option: Output File Name** . . . . . . . . . . . . . . . . . . . . . . . 23
    * **2.1.2 The -f Option: Output File Format** . . . . . . . . . . . . . . . . . . . . . . 23
    * **2.1.3 The -l Option: Generating a Listing File** . . . . . . . . . . . . . . . . . . . 24
    * **2.1.4 The -L Option: Additional or Modified Listing Info** . . . . . . . . . . . . . . 24
    * **2.1.5 The -M Option: Generate Makefile Dependencies** . . . . . . . . . . . . . . . . 25
    * **2.1.6 The -MG Option: Generate Makefile Dependencies** . . . . . . . . . . . . . . . . 25
    * **2.1.7 The -MF Option: Set Makefile Dependency File** . . . . . . . . . . . . . . . . . 25
    * **2.1.8 The -MD Option: Assemble and Generate Dependencies** . . . . . . . . . . . . . . 25
    * **2.1.9 The -MT Option: Dependency Target Name** . . . . . . . . . . . . . . . . . . . 26
    * **2.1.10 The -MQ Option: Dependency Target Name (Quoted)** . . . . . . . . . . . . . . . 26
    * **2.1.11 The -MP Option: Emit Phony Makefile Targets** . . . . . . . . . . . . . . . . . 26
    * **2.1.12 The -MW Option: Watcom make quoting style** . . . . . . . . . . . . . . . . . . 26
    * **2.1.13 The -F Option: Debug Information Format** . . . . . . . . . . . . . . . . . . 26
    * **2.1.14 The -g Option: Enabling Debug Information** . . . . . . . . . . . . . . . . . . 26
    * **2.1.15 The -X Option: Selecting an Error Reporting Format** . . . . . . . . . . . . . . 26
    * **2.1.16 The -Z Option: Send Errors to a File** . . . . . . . . . . . . . . . . . . . . 27
    * **2.1.17 The -s Option: Send Errors to stdout** . . . . . . . . . . . . . . . . . . . . 27
    * **2.1.18 The -i Option: Include File Search Directories** . . . . . . . . . . . . . . . . 27
    * **2.1.19 The -p Option: Pre-Include a File** . . . . . . . . . . . . . . . . . . . . . . 27
    * **2.1.20 The -d Option: Pre-Define a Macro** . . . . . . . . . . . . . . . . . . . . . 28
    * **2.1.21 The -u Option: Undefine a Macro** . . . . . . . . . . . . . . . . . . . . . . 28
    * **2.1.22 The -E Option: Preprocess Only** . . . . . . . . . . . . . . . . . . . . . . 28
    * **2.1.23 The -a Option: Suppress Preprocessing** . . . . . . . . . . . . . . . . . . . 28
    * **2.1.24 The -O Option: Multipass Optimization** . . . . . . . . . . . . . . . . . . . 28
    * **2.1.25 The -t Option: TASM Compatibility Mode** . . . . . . . . . . . . . . . . . . 29
    * **2.1.26 The -w and -W Options: Enable or Disable Assembly Warnings** . . . . . . . . . . . 29
    * **2.1.27 The -v Option: Display Version Info** . . . . . . . . . . . . . . . . . . . . 30
    * **2.1.28 The --[gl]prefix and --[gl]postfix Options** . . . . . . . . . . . . . . . . 30
    * **2.1.29 The --pragma Option** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
    * **2.1.30 The --before Option** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
    * **2.1.31 The --bits Option** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
    * **2.1.32 The --limit- Options** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
    * **2.1.33 The --keep-all Option** . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
    * **2.1.34 The --no-line Option** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
    * **2.1.35 The --reproducible Option** . . . . . . . . . . . . . . . . . . . . . . . . . 31
    * **2.1.36 The NASMENV Environment Variable** . . . . . . . . . . . . . . . . . . . . . . 31
  * **2.2 Quick Start for MASM Users** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
    * **2.2.1 NASM Is Case-Sensitive** . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
    * **2.2.2 NASM Requires Square Brackets For Memory References** . . . . . . . . . . . . . . 32
    * **2.2.3 NASM Doesn’t Store Variable Types** . . . . . . . . . . . . . . . . . . . . . 33
    * **2.2.4 NASM Doesn’t ASSUME** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
    * **2.2.5 NASM Doesn’t Support Memory Models** . . . . . . . . . . . . . . . . . . . . . 33
    * **2.2.6 Floating-Point Differences** . . . . . . . . . . . . . . . . . . . . . . . . . . 33
    * **2.2.7 Other Differences** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
    * **2.2.8 MASM compatibility package** . . . . . . . . . . . . . . . . . . . . . . . . . 33
* **Chapter 3: The NASM Language** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
  * **3.1 Layout of a NASM Source Line** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
  * **3.2 Pseudo-Instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
    * **3.2.1 Dx: Declaring Initialized Data** . . . . . . . . . . . . . . . . . . . . . . . . . 36
    * **3.2.2 RESB and Friends: Declaring Uninitialized Data** . . . . . . . . . . . . . . . . . 37
    * **3.2.3 INCBIN: Including External Binary Files** . . . . . . . . . . . . . . . . . . . . 37
    * **3.2.4 EQU: Defining Constants** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
    * **3.2.5 TIMES: Repeating Instructions or Data** . . . . . . . . . . . . . . . . . . . . . 38
  * **3.3 Effective Addresses** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
  * **3.4 Constants** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
    * **3.4.1 Numeric Constants** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
    * **3.4.2 Character Strings** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
    * **3.4.3 Character Constants** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
    * **3.4.4 String Constants** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
    * **3.4.5 Unicode Strings** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
    * **3.4.6 Floating-Point Constants** . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
    * **3.4.7 Packed BCD Constants** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
  * **3.5 Expressions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
    * **3.5.1 ? ... :: Conditional Operator** . . . . . . . . . . . . . . . . . . . . . . . . . 43
    * **3.5.2 : ||: Boolean OR Operator** . . . . . . . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.3 : ^^: Boolean XOR Operator** . . . . . . . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.4 : &&: Boolean AND Operator** . . . . . . . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.5 : Comparison Operators** . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.6 |: Bitwise OR Operator** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.7 ^: Bitwise XOR Operator** . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.8 &: Bitwise AND Operator** . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.9 Bit Shift Operators** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.10 + and -: Addition and Subtraction Operators** . . . . . . . . . . . . . . . . 44
    * **3.5.11 Multiplication, Division and Modulo** . . . . . . . . . . . . . . . . . . . . 44
    * **3.5.12 Unary Operators** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
  * **3.6 SEG and WRT** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
  * **3.7 STRICT: Inhibiting Optimization** . . . . . . . . . . . . . . . . . . . . . . . . . . 45
  * **3.8 Critical Expressions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
  * **3.9 Local Labels** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
* **Chapter 4: Syntax Quirks and Summaries** . . . . . . . . . . . . . . . . . . . . . . . . . . 49
  * **4.1 Summary of the JMP and CALL Syntax** . . . . . . . . . . . . . . . . . . . . . . . . 49
    * **4.1.1 Near Jumps** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
    * **4.1.2 Infinite Loop Trick** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
    * **4.1.3 Jumps and Mixed Sizes** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
    * **4.1.4 Calling Procedures Outside of a Shared Library** . . . . . . . . . . . . . . . . 49
    * **4.1.5 FAR Calls and Jumps** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
    * **4.1.6 64-bit absolute jump (JMPABS)** . . . . . . . . . . . . . . . . . . . . . . . . 50
    * **4.1.7 Optimizing jump lengths and sizes** . . . . . . . . . . . . . . . . . . . . . . 50
  * **4.2 Compact NDS/NDD Operands** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
  * **4.3 64-bit moffs** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
  * **4.4 Split EA Addressing Syntax** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
  * **4.5 No Syntax for Ternary Logic Instruction** . . . . . . . . . . . . . . . . . . . . . . 51
  * **4.6 APX Instruction Syntax** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
    * **4.6.1 Extended General Purpose Registers (EGPRs)** . . . . . . . . . . . . . . . . . 52
    * **4.6.2 New Data Destination (NDD)** . . . . . . . . . . . . . . . . . . . . . . . . . 52
    * **4.6.3 Suppress Modifying Flags (NF)** . . . . . . . . . . . . . . . . . . . . . . . . 52
    * **4.6.4 Zero Upper (ZU)** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
    * **4.6.5 Source Condition Code (Scc) and Default Flags Value (DFV)** . . . . . . . . . . . 53
    * **4.6.6 PUSH and POP Extensions** . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
    * **4.6.7 APX and the NASM optimizer** . . . . . . . . . . . . . . . . . . . . . . . . . 54
    * **4.6.8 Force APX Encoding** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
* **Chapter 5: The NASM Preprocessor** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
  * **5.1 Preprocessor Expansions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
    * **5.1.1 Continuation Line Collapsing** . . . . . . . . . . . . . . . . . . . . . . . . . 55
    * **5.1.2 Comment Removal** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
    * **5.1.3 %line directives** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
    * **5.1.4 Conditionals, Loops and Multi-Line Macro Definitions** . . . . . . . . . . . . . . 55
    * **5.1.5 Directives processing** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
    * **5.1.6 Inline expansions and other directives** . . . . . . . . . . . . . . . . . . . . 56
    * **5.1.7 Multi-Line Macro Expansion** . . . . . . . . . . . . . . . . . . . . . . . . . 56
    * **5.1.8 Detokenization** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
  * **5.2 Preprocessor caveats** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
    * **5.2.1 Case Insensitivity** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
  * **5.3 Single-Line Macros** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
    * **5.3.1 The Normal Way: %define** . . . . . . . . . . . . . . . . . . . . . . . . . . 57
    * **5.3.2 Resolving %define: %xdefine** . . . . . . . . . . . . . . . . . . . . . . . . . 58
    * **5.3.3 Macro Indirection: %[...]** . . . . . . . . . . . . . . . . . . . . . . . . . . 59
    * **5.3.4 Concatenating Single Line Macro Tokens: %+** . . . . . . . . . . . . . . . . . . 59
    * **5.3.5 The Macro Name Itself: %? and %??** . . . . . . . . . . . . . . . . . . . . . 60
    * **5.3.6 The Single-Line Macro Name: %*? and %*??** . . . . . . . . . . . . . . . . . . 60
    * **5.3.7 Undefining Single-Line Macros: %undef** . . . . . . . . . . . . . . . . . . . 61
    * **5.3.8 Preprocessor Variables: %assign** . . . . . . . . . . . . . . . . . . . . . . . 61
    * **5.3.9 Defining Strings: %defstr** . . . . . . . . . . . . . . . . . . . . . . . . . . 62
    * **5.3.10 Defining Tokens: %deftok** . . . . . . . . . . . . . . . . . . . . . . . . . . 62
    * **5.3.11 Defining Aliases: %defalias** . . . . . . . . . . . . . . . . . . . . . . . . 62
    * **5.3.12 Conditional Comma Operator: %,** . . . . . . . . . . . . . . . . . . . . . . 63
  * **5.4 String Manipulation in Macros** . . . . . . . . . . . . . . . . . . . . . . . . . . 63
    * **5.4.1 Concatenating Strings: %strcat** . . . . . . . . . . . . . . . . . . . . . . . 63
    * **5.4.2 String Length: %strlen** . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
    * **5.4.3 Extracting Substrings: %substr** . . . . . . . . . . . . . . . . . . . . . . . 63
  * **5.5 Preprocessor Functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
    * **5.5.1 %abs() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
    * **5.5.2 %b2hs() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
    * **5.5.3 %chr() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
    * **5.5.4 %cond() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
    * **5.5.5 %count() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
    * **5.5.6 %depend() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
    * **5.5.7 %env() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
    * **5.5.8 %eval() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
    * **5.5.9 %find() and %findi() Functions** . . . . . . . . . . . . . . . . . . . . . . . 65
    * **5.5.10 %hex() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
    * **5.5.11 %hs2b() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
    * **5.5.12 %is() Family Functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
    * **5.5.13 %limit() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
    * **5.5.14 %map() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
    * **5.5.15 %null() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
    * **5.5.16 %num() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
    * **5.5.17 %ord() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
    * **5.5.18 %pathsearch() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
    * **5.5.19 %realpath() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
    * **5.5.20 %sel() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
    * **5.5.21 %selbits() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
    * **5.5.22 %str() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
    * **5.5.23 %strcat() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
    * **5.5.24 %strlen() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
    * **5.5.25 %substr() Function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
    * **5.5.26 %tok() function** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
  * **5.6 Multi-Line Macros: %macro** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
    * **5.6.1 Overloading Multi-Line Macros** . . . . . . . . . . . . . . . . . . . . . . . 70
    * **5.6.2 Macro-Local Labels** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
    * **5.6.3 Greedy Macro Parameters** . . . . . . . . . . . . . . . . . . . . . . . . . . 71
    * **5.6.4 Macro Parameters Range** . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
    * **5.6.5 Default Macro Parameters** . . . . . . . . . . . . . . . . . . . . . . . . . . 73
    * **5.6.6 %0: Macro Parameter Counter** . . . . . . . . . . . . . . . . . . . . . . . . 74
    * **5.6.7 %00: Label Preceding Macro** . . . . . . . . . . . . . . . . . . . . . . . . . 74
    * **5.6.8 %rotate: Rotating Macro Parameters** . . . . . . . . . . . . . . . . . . . . . 74
    * **5.6.9 Concatenating Macro Parameters** . . . . . . . . . . . . . . . . . . . . . . . 75
    * **5.6.10 Condition Codes as Macro Parameters** . . . . . . . . . . . . . . . . . . . . 75
    * **5.6.11 Disabling Listing Expansion.nolist** . . . . . . . . . . . . . . . . . . . . 76
    * **5.6.12 Undefining Multi-Line Macros: %unmacro, %unimacro** . . . . . . . . . . . . . . 76
    * **5.6.13 %exitmacro: Stop Expanding a Multi-Line Macro** . . . . . . . . . . . . . . . . 77
  * **5.7 Conditional Assembly** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
    * **5.7.1 %if: Testing Arbitrary Numeric Expressions** . . . . . . . . . . . . . . . . . 77
    * **5.7.2 %ifdef: Testing Single-Line Macro Existence** . . . . . . . . . . . . . . . . . 77
    * **5.7.3 %ifdefalias: Testing Single-Line Macro Alias Existence** . . . . . . . . . . . . . . 78
    * **5.7.4 %ifmacro: Testing Multi-Line Macro Existence** . . . . . . . . . . . . . . . . . 78
    * **5.7.5 %ifctx: Testing the Context Stack** . . . . . . . . . . . . . . . . . . . . . . 78
    * **5.7.6 %ifidn and %ifidni: Testing Exact Text Identity** . . . . . . . . . . . . . . . 79
    * **5.7.7 %ifid, %ifnum, %ifstr: Testing Token Types** . . . . . . . . . . . . . . . . . 79
    * **5.7.8 %iftoken: Test for a Single Token** . . . . . . . . . . . . . . . . . . . . . . 80
    * **5.7.9 %ifempty: Test for Empty Expansion** . . . . . . . . . . . . . . . . . . . . . 80
    * **5.7.10 %ifdirective: Test If a Directive Is Supported** . . . . . . . . . . . . . . . 80
    * **5.7.11 %ifusable and %ifusing: Test For Standard Macro Packages** . . . . . . . . . . . 80
    * **5.7.12 %iffile: Test If a File Exists** . . . . . . . . . . . . . . . . . . . . . . . . 81
    * **5.7.13 %ifenv: Test If Environment Variable Exists** . . . . . . . . . . . . . . . . . 81
    * **5.7.14 Backwards Compatibility Caveat** . . . . . . . . . . . . . . . . . . . . . . 81
  * **5.8 Preprocessor Loops: %rep** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
  * **5.9 Source Files and Dependencies** . . . . . . . . . . . . . . . . . . . . . . . . . . 82
    * **5.9.1 %include: Including Other Files** . . . . . . . . . . . . . . . . . . . . . . . 82
    * **5.9.2 %pathsearch: Search the Include Path** . . . . . . . . . . . . . . . . . . . . . 83
    * **5.9.3 %depend: Add Dependent Files** . . . . . . . . . . . . . . . . . . . . . . . . 83
    * **5.9.4 %use: Include Standard Macro Package** . . . . . . . . . . . . . . . . . . . . 83
  * **5.10 The Context Stack** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
    * **5.10.1 %push and %pop: Creating and Removing Contexts** . . . . . . . . . . . . . . 84
    * **5.10.2 Context-Local Labels** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
    * **5.10.3 Context-Local Single-Line Macros** . . . . . . . . . . . . . . . . . . . . . . 84
    * **5.10.4 Context Fall-Through Lookup (deprecated)** . . . . . . . . . . . . . . . . . . 85
    * **5.10.5 %repl: Renaming a Context** . . . . . . . . . . . . . . . . . . . . . . . . . 85
    * **5.10.6 Example Use of the Context Stack: Block IFs** . . . . . . . . . . . . . . . . . 86
  * **5.11 Stack Relative Preprocessor Directives** . . . . . . . . . . . . . . . . . . . . . . 87
    * **5.11.1 %arg Directive** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
    * **5.11.2 %stacksize Directive** . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
    * **5.11.3 %local Directive** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
  * **5.12 Reporting User-generated Diagnostics: %error, %warning, %fatal, %note** . . . . . . . . . 88
  * **5.13 %pragma: Setting Options** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
    * **5.13.1 Preprocessor Pragmas** . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
  * **5.14 Other Preprocessor Directives** . . . . . . . . . . . . . . . . . . . . . . . . . . 90
    * **5.14.1 %line Directive** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
    * **5.14.2 %!variable: Read an Environment Variable.** . . . . . . . . . . . . . . . . . 90
    * **5.14.3 %clear: Clear All Macro Definitions** . . . . . . . . . . . . . . . . . . . . . 91
* **Chapter 6: Standard Macros** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
  * **6.1 NASM Version Macros** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
    * **6.1.1 \_\_?NASM\_VERSION\_ID?\_\_: NASM Version ID** . . . . . . . . . . . . . . . . . . . . 93
    * **6.1.2 \_\_?NASM\_VER?\_\_: NASM Version String** . . . . . . . . . . . . . . . . . . . . . . 93
  * **6.2 \_\_?FILE?\_\_ and \_\_?LINE?\_\_: File Name and Line Number** . . . . . . . . . . . . . . . . . . 93
  * **6.3 \_\_?BITS?\_\_: Current Code Generation Mode** . . . . . . . . . . . . . . . . . . . . . . 94
  * **6.4 \_\_?DEFAULT?\_\_: DEFAULT directive settings** . . . . . . . . . . . . . . . . . . . . . . . . 94
  * **6.5 \_\_?OUTPUT\_FORMAT?\_\_: Current Output Format** . . . . . . . . . . . . . . . . . . . . . . 94
  * **6.6 \_\_?DEBUG\_FORMAT?\_\_: Current Debug Format** . . . . . . . . . . . . . . . . . . . . . . . 94
  * **6.7 Assembly Date and Time Macros** . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
  * **6.8 \_\_?NASM\_LIMITS?\_\_: List of Resource Limits** . . . . . . . . . . . . . . . . . . . . . . 95
  * **6.9 \_\_?NASM\_HAS\_IFDIRECTIVE?\_\_: Directive Probing Support** . . . . . . . . . . . . . . . . . . 95
  * **6.10 \_\_?USE\_package?\_\_: Package Include Test** . . . . . . . . . . . . . . . . . . . . . . . 95
  * **6.11 \_\_?LIST\_OPTIONS?\_\_: Current Listing Options** . . . . . . . . . . . . . . . . . . . . . 96
  * **6.12 \_\_?LIST\_OPTIONS\_DEFAULT?\_\_: Default Listing Options** . . . . . . . . . . . . . . . . . . 96
  * **6.13 \_\_?PASS?\_\_: Assembly Pass** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
  * **6.14 Structure Data Types** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
    * **6.14.1 STRUC and ENDSTRUC: Declaring Structure Data Types** . . . . . . . . . . . . . . 96
    * **6.14.2 ISTRUC, AT and IEND: Declaring Instances of Structures** . . . . . . . . . . . . . . 97
  * **6.15 Alignment Control** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
    * **6.15.1 ALIGN and ALIGNB: Code and Data Alignment** . . . . . . . . . . . . . . . . . . 98
    * **6.15.2 SECTALIGN: Section Alignment** . . . . . . . . . . . . . . . . . . . . . . . . . 98
* **Chapter 7: Standard Macro Packages** . . . . . . . . . . . . . . . . . . . . . . . . . . . .101
  * **7.1 altreg: Alternate Register Names** . . . . . . . . . . . . . . . . . . . . . . . . . . .101
  * **7.2 smartalign: Smart ALIGN Macro** . . . . . . . . . . . . . . . . . . . . . . . . . . . .101
  * **7.3 fp: Floating-point macros** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .102
  * **7.4 ifunc: Integer functions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .102
    * **7.4.1 Integer logarithms** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .102
  * **7.5 masm: MASM compatibility** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .102
  * **7.6 vtern: Ternary Logic Assist** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .103
* **Chapter 8: Assembler Directives** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .105
  * **8.1 BITS: Target Processor Mode** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .105
    * **8.1.1 USE16 & USE32: Aliases for BITS** . . . . . . . . . . . . . . . . . . . . . . . . .106
  * **8.2 DEFAULT: Change the assembler defaults** . . . . . . . . . . . . . . . . . . . . . . . .106
    * **8.2.1 REL, ABS: RIP-relative addressing** . . . . . . . . . . . . . . . . . . . . . . . .106
    * **8.2.2 BND, NOBND: BND prefix** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .106
  * **8.3 SECTION or SEGMENT: Changing and Defining Sections** . . . . . . . . . . . . . . . . . . .106
    * **8.3.1 The \_\_?SECT?\_\_ Macro** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .107
  * **8.4 ABSOLUTE: Defining Absolute Labels** . . . . . . . . . . . . . . . . . . . . . . . . . .107
  * **8.5 EXTERN: Importing Symbols from Other Modules** . . . . . . . . . . . . . . . . . . . . .108
  * **8.6 REQUIRED: Unconditionally Importing Symbols from Other Modules** . . . . . . . . . . . . .109
  * **8.7 GLOBAL: Exporting Symbols to Other Modules** . . . . . . . . . . . . . . . . . . . . . .109
  * **8.8 COMMON: Defining Common Data Areas** . . . . . . . . . . . . . . . . . . . . . . . . . .109
  * **8.9 STATIC: Local Symbols within Modules** . . . . . . . . . . . . . . . . . . . . . . . . .110
  * **8.10 [[GL]PREFIX], [[GL]SUFFIX]: Mangling Symbols** . . . . . . . . . . . . . . . . . . . . .110
  * **8.11 CPU: Defining CPU Dependencies** . . . . . . . . . . . . . . . . . . . . . . . . . . .111
  * **8.12 [DOLLARHEX]: Enable or disable $ hexadecimal syntax** . . . . . . . . . . . . . . . . . .112
  * **8.13 FLOAT: Handling of floating-point constants** . . . . . . . . . . . . . . . . . . . . .112
  * **8.14 [WARNING]: Enable or disable warnings** . . . . . . . . . . . . . . . . . . . . . . . .112
  * **8.15 [LIST]: Locally disable list file output** . . . . . . . . . . . . . . . . . . . . . . .113
* **Chapter 9: Output Formats** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .115
  * **9.1 bin: Flat-Form Binary Output** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .115
    * **9.1.1 ORG: Binary File Program Origin** . . . . . . . . . . . . . . . . . . . . . . . .115
    * **9.1.2 bin Extensions to the SECTION Directive** . . . . . . . . . . . . . . . . . . . . .115
    * **9.1.3 Multisection Support for the bin Format** . . . . . . . . . . . . . . . . . . . . .116
    * **9.1.4 Map Files** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .116
  * **9.2 ith: Intel Hex Output** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .116
  * **9.3 srec: Motorola S-Records Output** . . . . . . . . . . . . . . . . . . . . . . . . . . .117
  * **9.4 obj: Microsoft OMF Object Files** . . . . . . . . . . . . . . . . . . . . . . . . . . .117
    * **9.4.1 obj Extensions to the SEGMENT Directive** . . . . . . . . . . . . . . . . . . . . .117
    * **9.4.2 GROUP: Defining Groups of Segments** . . . . . . . . . . . . . . . . . . . . . .118
    * **9.4.3 UPPERCASE: Disabling Case Sensitivity in Output** . . . . . . . . . . . . . . . . .119
    * **9.4.4 IMPORT: Importing DLL Symbols** . . . . . . . . . . . . . . . . . . . . . . . .119
    * **9.4.5 EXPORT: Exporting DLL Symbols** . . . . . . . . . . . . . . . . . . . . . . . .119
    * **9.4.6 ..start: Defining the Program Entry Point** . . . . . . . . . . . . . . . . . . .120
    * **9.4.7 obj Extensions to the EXTERN Directive** . . . . . . . . . . . . . . . . . . . . .120
    * **9.4.8 obj Extensions to the COMMON Directive** . . . . . . . . . . . . . . . . . . . . .120
    * **9.4.9 Embedded File Dependency Information** . . . . . . . . . . . . . . . . . . . . .121
  * **9.5 obj2: OS/2 32-bit OMF Object Files** . . . . . . . . . . . . . . . . . . . . . . . . .121
  * **9.6 win32: Microsoft Win32 Object Files** . . . . . . . . . . . . . . . . . . . . . . . . .121
    * **9.6.1 win32 Extensions to the SECTION Directive** . . . . . . . . . . . . . . . . . . .122
    * **9.6.2 win32: Safe Structured Exception Handling** . . . . . . . . . . . . . . . . . . .123
    * **9.6.3 win32: Special Symbol and WRT** . . . . . . . . . . . . . . . . . . . . . . . . .124
    * **9.6.4 win32 Extensions to the GLOBAL, EXTERN and STATIC Directives** . . . . . . . . . . .124
    * **9.6.5 Debugging formats for Windows** . . . . . . . . . . . . . . . . . . . . . . . .125
  * **9.7 win64: Microsoft Win64 Object Files** . . . . . . . . . . . . . . . . . . . . . . . . .125
    * **9.7.1 win64: Writing Position-Independent Code** . . . . . . . . . . . . . . . . . . .125
    * **9.7.2 win64: Structured Exception Handling** . . . . . . . . . . . . . . . . . . . . .126
  * **9.8 coff: Common Object File Format** . . . . . . . . . . . . . . . . . . . . . . . . . .128
  * **9.9 macho32 and macho64: Mach Object File Format** . . . . . . . . . . . . . . . . . . . . .128
    * **9.9.1 macho extensions to the SECTION Directive** . . . . . . . . . . . . . . . . . . .128
    * **9.9.2 Thread Local Storage in Mach-O: macho special symbols and WRT** . . . . . . . . . . .129
    * **9.9.3 macho specific directive subsections\_via\_symbols** . . . . . . . . . . . . . . . .129
    * **9.9.4 macho specific directive no\_dead\_strip** . . . . . . . . . . . . . . . . . . . . .129
    * **9.9.5 macho specific extensions to the GLOBAL Directive: private\_extern** . . . . . . . . . .129
    * **9.9.6 macho specific directive build\_version** . . . . . . . . . . . . . . . . . . . . .130
  * **9.10 elf32, elf64, elfx32: Executable and Linkable Format Object Files** . . . . . . . . . . . .130
    * **9.10.1 ELF specific directive osabi** . . . . . . . . . . . . . . . . . . . . . . . . .130
    * **9.10.2 ELF extensions to the SECTION Directive** . . . . . . . . . . . . . . . . . . .130
    * **9.10.3 Position-Independent Code: ELF Special Symbols and WRT** . . . . . . . . . . . . .132
    * **9.10.4 Thread Local Storage in ELF: elf Special Symbols and WRT** . . . . . . . . . . . . .132
    * **9.10.5 elf Extensions to the GLOBAL Directive** . . . . . . . . . . . . . . . . . . . .133
    * **9.10.6 elf Extensions to the EXTERN Directive** . . . . . . . . . . . . . . . . . . . .133
    * **9.10.7 elf Extensions to the COMMON Directive** . . . . . . . . . . . . . . . . . . . .133
    * **9.10.8 16-bit code and ELF** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .134
    * **9.10.9 Debug formats and ELF** . . . . . . . . . . . . . . . . . . . . . . . . . . .134
  * **9.11 aout: Linux a.out Object Files** . . . . . . . . . . . . . . . . . . . . . . . . . . .134
  * **9.12 aoutb: NetBSD/FreeBSD/OpenBSD a.out Object Files** . . . . . . . . . . . . . . . . . . .134
  * **9.13 as86: Minix/Linux as86 Object Files** . . . . . . . . . . . . . . . . . . . . . . . . .134
  * **9.14 dbg: Debugging Format** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .135
* **Chapter 10: Writing 16-bit Code (DOS, Windows 3/3.1)** . . . . . . . . . . . . . . . . . . . . . . .137
  * **10.1 Producing .EXE Files** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .137
    * **10.1.1 Using the obj Format To Generate .EXE Files** . . . . . . . . . . . . . . . . . .137
    * **10.1.2 Using the bin Format To Generate .EXE Files** . . . . . . . . . . . . . . . . . .138
  * **10.2 Producing .COM Files** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .139
    * **10.2.1 Using the bin Format To Generate .COM Files** . . . . . . . . . . . . . . . . . .139
    * **10.2.2 Using the obj Format To Generate .COM Files** . . . . . . . . . . . . . . . . . .139
  * **10.3 Producing .SYS Files** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .140
  * **10.4 Interfacing to 16-bit C Programs** . . . . . . . . . . . . . . . . . . . . . . . . . .140
    * **10.4.1 External Symbol Names** . . . . . . . . . . . . . . . . . . . . . . . . . . .140
    * **10.4.2 Memory Models** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .141
    * **10.4.3 Function Definitions and Function Calls** . . . . . . . . . . . . . . . . . . .141
    * **10.4.4 Accessing Data Items** . . . . . . . . . . . . . . . . . . . . . . . . . . . .143
    * **10.4.5 c16.mac: Helper Macros for the 16-bit C Interface** . . . . . . . . . . . . . . .144
  * **10.5 Interfacing to Borland Pascal Programs** . . . . . . . . . . . . . . . . . . . . . . . .145
    * **10.5.1 The Pascal Calling Convention** . . . . . . . . . . . . . . . . . . . . . . . .145
    * **10.5.2 Borland Pascal Segment Name Restrictions** . . . . . . . . . . . . . . . . . . .146
    * **10.5.3 Using c16.mac With Pascal Programs** . . . . . . . . . . . . . . . . . . . . .147
* **Chapter 11: Writing 32-bit Code (Unix, Win32, DJGPP)** . . . . . . . . . . . . . . . . . . . . . . .149
  * **11.1 Interfacing to 32-bit C Programs** . . . . . . . . . . . . . . . . . . . . . . . . . .149
    * **11.1.1 External Symbol Names** . . . . . . . . . . . . . . . . . . . . . . . . . . .149
    * **11.1.2 Function Definitions and Function Calls** . . . . . . . . . . . . . . . . . . .149
    * **11.1.3 Accessing Data Items** . . . . . . . . . . . . . . . . . . . . . . . . . . . .151
    * **11.1.4 c32.mac: Helper Macros for the 32-bit C Interface** . . . . . . . . . . . . . . .151
  * **11.2 Writing NetBSD/FreeBSD/OpenBSD and Linux/ELF Shared Libraries** . . . . . . . . . . . .152
    * **11.2.1 Obtaining the Address of the GOT** . . . . . . . . . . . . . . . . . . . . . .152
    * **11.2.2 Finding Your Local Data Items** . . . . . . . . . . . . . . . . . . . . . . . .153
    * **11.2.3 Finding External and Common Data Items** . . . . . . . . . . . . . . . . . . .153
    * **11.2.4 Exporting Symbols to the Library User** . . . . . . . . . . . . . . . . . . . . .154
    * **11.2.5 Calling Procedures Outside the Library** . . . . . . . . . . . . . . . . . . . .154
    * **11.2.6 Generating the Library File** . . . . . . . . . . . . . . . . . . . . . . . . . .155
* **Chapter 12: Mixing 16- and 32-bit Code** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .157
  * **12.1 Mixed-Size Jumps** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .157
  * **12.2 Addressing Between Different-Size Segments** . . . . . . . . . . . . . . . . . . . . . .157
  * **12.3 Other Mixed-Size Instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . .158
* **Chapter 13: Writing 64-bit Code (Unix, Win64)** . . . . . . . . . . . . . . . . . . . . . . . . .161
  * **13.1 Register Names in 64-bit Mode** . . . . . . . . . . . . . . . . . . . . . . . . . . .161
  * **13.2 Immediates and Displacements in 64-bit Mode** . . . . . . . . . . . . . . . . . . . . .161
    * **13.2.1 Immediate 64-bit Operands** . . . . . . . . . . . . . . . . . . . . . . . . .161
    * **13.2.2 64-bit Displacements** . . . . . . . . . . . . . . . . . . . . . . . . . . . .162
  * **13.3 Interfacing to 64-bit C Programs (Unix)** . . . . . . . . . . . . . . . . . . . . . . .162
  * **13.4 Interfacing to 64-bit C Programs (Win64)** . . . . . . . . . . . . . . . . . . . . . . .163
* **Chapter 14: Troubleshooting** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .165
  * **14.1 Common Problems** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .165
    * **14.1.1 NASM Generates Inefficient Code** . . . . . . . . . . . . . . . . . . . . . . .165
    * **14.1.2 My Jumps are Out of Range** . . . . . . . . . . . . . . . . . . . . . . . . . .165
    * **14.1.3 ORG Doesn’t Work** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .165
    * **14.1.4 TIMES Doesn’t Work** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .166
* **Appendix A: List of Warning Classes** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .167
  * **A.1 Warning Classes** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .167
    * **A.1.1 Enabled by default** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .167
    * **A.1.2 Enabled and promoted to error by default** . . . . . . . . . . . . . . . . . . . .171
    * **A.1.3 Disabled by default** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .171
  * **A.2 Warning Class Groups** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .173
  * **A.3 Warning Class Aliases for Backward Compatiblity** . . . . . . . . . . . . . . . . . . . .175
* **Appendix B: Ndisasm** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .177
  * **B.1 Introduction** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .177
  * **B.2 Running NDISASM** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .177
    * **B.2.1 Specifying the Input Origin** . . . . . . . . . . . . . . . . . . . . . . . . . . .177
    * **B.2.2 Code Following Data: Synchronization** . . . . . . . . . . . . . . . . . . . . .177
    * **B.2.3 Mixed Code and Data: Automatic (Intelligent) Synchronization** . . . . . . . . . . .178
    * **B.2.4 Other Options** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .179
* **Appendix C: NASM Version History** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .181
  * **C.1 NASM 3 Series** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .181
    * **C.1.1 Version 3.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .181
    * **C.1.2 Version 3.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .182
    * **C.1.3 Version 3.00** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .183
  * **C.2 NASM 2 Series** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .184
    * **C.2.1 Version 2.16.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .184
    * **C.2.2 Version 2.16.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .184
    * **C.2.3 Version 2.16.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .186
    * **C.2.4 Version 2.16** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .186
    * **C.2.5 Version 2.15.05** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .187
    * **C.2.6 Version 2.15.04** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .187
    * **C.2.7 Version 2.15.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .187
    * **C.2.8 Version 2.15.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .188
    * **C.2.9 Version 2.15.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .188
    * **C.2.10 Version 2.15** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .188
    * **C.2.11 Version 2.14.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .189
    * **C.2.12 Version 2.14.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .190
    * **C.2.13 Version 2.14.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .190
    * **C.2.14 Version 2.14** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .190
    * **C.2.15 Version 2.13.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .191
    * **C.2.16 Version 2.13.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .191
    * **C.2.17 Version 2.13.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .192
    * **C.2.18 Version 2.13** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .192
    * **C.2.19 Version 2.12.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .193
    * **C.2.20 Version 2.12.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .193
    * **C.2.21 Version 2.12** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .193
    * **C.2.22 Version 2.11.09** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .194
    * **C.2.23 Version 2.11.08** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .194
    * **C.2.24 Version 2.11.07** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .194
    * **C.2.25 Version 2.11.06** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .194
    * **C.2.26 Version 2.11.05** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .194
    * **C.2.27 Version 2.11.04** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .195
    * **C.2.28 Version 2.11.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .195
    * **C.2.29 Version 2.11.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .195
    * **C.2.30 Version 2.11.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .195
    * **C.2.31 Version 2.11** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .195
    * **C.2.32 Version 2.10.09** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .196
    * **C.2.33 Version 2.10.08** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .196
    * **C.2.34 Version 2.10.07** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .196
    * **C.2.35 Version 2.10.06** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .196
    * **C.2.36 Version 2.10.05** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .197
    * **C.2.37 Version 2.10.04** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .197
    * **C.2.38 Version 2.10.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .197
    * **C.2.39 Version 2.10.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .197
    * **C.2.40 Version 2.10.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .197
    * **C.2.41 Version 2.10** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .197
    * **C.2.42 Version 2.09.10** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .197
    * **C.2.43 Version 2.09.09** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198
    * **C.2.44 Version 2.09.08** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198
    * **C.2.45 Version 2.09.07** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198
    * **C.2.46 Version 2.09.06** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198
    * **C.2.47 Version 2.09.05** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198
    * **C.2.48 Version 2.09.04** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198
    * **C.2.49 Version 2.09.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198
    * **C.2.50 Version 2.09.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198
    * **C.2.51 Version 2.09.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .199
    * **C.2.52 Version 2.09** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .199
    * **C.2.53 Version 2.08.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .199
    * **C.2.54 Version 2.08.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .200
    * **C.2.55 Version 2.08** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .200
    * **C.2.56 Version 2.07** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .200
    * **C.2.57 Version 2.06** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .201
    * **C.2.58 Version 2.05.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .201
    * **C.2.59 Version 2.05** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .201
    * **C.2.60 Version 2.04** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .202
    * **C.2.61 Version 2.03.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .202
    * **C.2.62 Version 2.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .203
    * **C.2.63 Version 2.02** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .203
    * **C.2.64 Version 2.01** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .204
    * **C.2.65 Version 2.00** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .204
  * **C.3 NASM 0.98 Series** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .205
    * **C.3.1 Version 0.98.39** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .205
    * **C.3.2 Version 0.98.38** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .205
    * **C.3.3 Version 0.98.37** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .205
    * **C.3.4 Version 0.98.36** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .206
    * **C.3.5 Version 0.98.35** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .206
    * **C.3.6 Version 0.98.34** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .206
    * **C.3.7 Version 0.98.33** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .206
    * **C.3.8 Version 0.98.32** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .207
    * **C.3.9 Version 0.98.31** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .207
    * **C.3.10 Version 0.98.30** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .207
    * **C.3.11 Version 0.98.28** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.12 Version 0.98.26** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.13 Version 0.98.25alt** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.14 Version 0.98.25** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.15 Version 0.98.24p1** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.16 Version 0.98.24** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.17 Version 0.98.23** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.18 Version 0.98.22** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.19 Version 0.98.21** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.20 Version 0.98.20** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.21 Version 0.98.19** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.22 Version 0.98.18** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.23 Version 0.98.17** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.24 Version 0.98.16** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .208
    * **C.3.25 Version 0.98.15** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209
    * **C.3.26 Version 0.98.14** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209
    * **C.3.27 Version 0.98.13** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209
    * **C.3.28 Version 0.98.12** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209
    * **C.3.29 Version 0.98.11** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209
    * **C.3.30 Version 0.98.10** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209
    * **C.3.31 Version 0.98.09** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209
    * **C.3.32 Version 0.98.08** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209
    * **C.3.33 Version 0.98.09b with John Coffman patches released 28-Oct-2001** . . . . . . . .209
    * **C.3.34 Version 0.98.07 released 01/28/01** . . . . . . . . . . . . . . . . . . . . . . . .210
    * **C.3.35 Version 0.98.06f released 01/18/01** . . . . . . . . . . . . . . . . . . . . . . . .210
    * **C.3.36 Version 0.98.06e released 01/09/01** . . . . . . . . . . . . . . . . . . . . . . . .210
    * **C.3.37 Version 0.98p1** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .210
    * **C.3.38 Version 0.98bf (bug-fixed)** . . . . . . . . . . . . . . . . . . . . . . . . . .211
    * **C.3.39 Version 0.98.03 with John Coffman’s changes released 27-Jul-2000** . . . . . . . .211
    * **C.3.40 Version 0.98.03** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .211
    * **C.3.41 Version 0.98** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .214
    * **C.3.42 Version 0.98p9** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .214
    * **C.3.43 Version 0.98p8** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .214
    * **C.3.44 Version 0.98p7** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .215
    * **C.3.45 Version 0.98p6** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .215
    * **C.3.46 Version 0.98p3.7** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .216
    * **C.3.47 Version 0.98p3.6** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .216
    * **C.3.48 Version 0.98p3.5** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .216
    * **C.3.49 Version 0.98p3.4** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .216
    * **C.3.50 Version 0.98p3.3** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .216
    * **C.3.51 Version 0.98p3.2** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .217
    * **C.3.52 Version 0.98p3-hpa** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .217
    * **C.3.53 Version 0.98 pre-release 3** . . . . . . . . . . . . . . . . . . . . . . . . . .217
    * **C.3.54 Version 0.98 pre-release 2** . . . . . . . . . . . . . . . . . . . . . . . . . .217
    * **C.3.55 Version 0.98 pre-release 1** . . . . . . . . . . . . . . . . . . . . . . . . . .217
  * **C.4 NASM 0.90-0.97** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .218
    * **C.4.1 Version 0.97 released December 1997** . . . . . . . . . . . . . . . . . . . . . . .219
    * **C.4.2 Version 0.96 released November 1997** . . . . . . . . . . . . . . . . . . . . . . .219
    * **C.4.3 Version 0.95 released July 1997** . . . . . . . . . . . . . . . . . . . . . . . . .221
    * **C.4.4 Version 0.94 released April 1997** . . . . . . . . . . . . . . . . . . . . . . . . .223
    * **C.4.5 Version 0.93 released January 1997** . . . . . . . . . . . . . . . . . . . . . . . .223
    * **C.4.6 Version 0.92 released January 1997** . . . . . . . . . . . . . . . . . . . . . . . .224
    * **C.4.7 Version 0.91 released November 1996** . . . . . . . . . . . . . . . . . . . . . . .224
    * **C.4.8 Version 0.90 released October 1996** . . . . . . . . . . . . . . . . . . . . . . . .224
* **Appendix D: Building NASM from Source** . . . . . . . . . . . . . . . . . . . . . . . . . .225
  * **D.1 Building from a Source Archive** . . . . . . . . . . . . . . . . . . . . . . . . . .225
  * **D.2 Optional Build Tools** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .225
  * **D.3 Building Optional Components** . . . . . . . . . . . . . . . . . . . . . . . . . .226
  * **D.4 Building from the git Repository** . . . . . . . . . . . . . . . . . . . . . . . . . .226
  * **D.5 Modifying the Sources** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .227
* **Appendix E: Contact Information** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .229
  * **E.1 Website** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .229
    * **E.1.1 User Forums** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .229
    * **E.1.2 Development Community** . . . . . . . . . . . . . . . . . . . . . . . . . .229
  * **E.2 Reporting Bugs** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .229
* **Appendix F: Instruction List** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .231
  * **F.1 Introduction** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .231
    * **F.1.1 Special instructions (pseudo-ops)** . . . . . . . . . . . . . . . . . . . . . . .231
    * **F.1.2 No operation** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .231
    * **F.1.3 Integer data move instructions** . . . . . . . . . . . . . . . . . . . . . . .231
    * **F.1.4 Load effective address** . . . . . . . . . . . . . . . . . . . . . . . . . . . .232
    * **F.1.5 The basic 8 arithmetic operations** . . . . . . . . . . . . . . . . . . . . . .232
    * **F.1.6 Bitwise testing** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .236
    * **F.1.7 The basic shift and rotate operations** . . . . . . . . . . . . . . . . . . . . .236
    * **F.1.8 APX EVEX versions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .240
    * **F.1.9 Other basic integer arithmetic** . . . . . . . . . . . . . . . . . . . . . . . .244
    * **F.1.10 Interleaved flags arithmetic** . . . . . . . . . . . . . . . . . . . . . . . .246
    * **F.1.11 Double width shift** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .246
    * **F.1.12 Bit operations** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .246
    * **F.1.13 BMI1 and BMI2 bit operations** . . . . . . . . . . . . . . . . . . . . . . .247
    * **F.1.14 AMD XOP bit operations** . . . . . . . . . . . . . . . . . . . . . . . . . .248
    * **F.1.15 Decimal arithmetic** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .248
    * **F.1.16 Endianness handling** . . . . . . . . . . . . . . . . . . . . . . . . . . . .248
    * **F.1.17 Sign and zero extension** . . . . . . . . . . . . . . . . . . . . . . . . . .248
    * **F.1.18 Atomic operations** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .249
    * **F.1.19 Jumps** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .250
    * **F.1.20 Call and return** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .252
    * **F.1.21 Interrupts, system calls, and returns** . . . . . . . . . . . . . . . . . . . .253
    * **F.1.22 Flag register instructions** . . . . . . . . . . . . . . . . . . . . . . . . . .253
    * **F.1.23 String instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .253
    * **F.1.24 Synchronization and fencing** . . . . . . . . . . . . . . . . . . . . . . . .254
    * **F.1.25 Memory management and control** . . . . . . . . . . . . . . . . . . . . . .254
    * **F.1.26 Special reads: timestamp, CPU number, performance counters, randomness** . . .254
    * **F.1.27 Machine control and management instructions** . . . . . . . . . . . . . . . .254
    * **F.1.28 System management mode** . . . . . . . . . . . . . . . . . . . . . . . . . .255
    * **F.1.29 Power management** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .255
    * **F.1.30 I/O instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .256
    * **F.1.31 Segment handling instructions** . . . . . . . . . . . . . . . . . . . . . . .256
    * **F.1.32 x87 floating point** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .257
    * **F.1.33 MMX (SIMD using the x87 register file)** . . . . . . . . . . . . . . . . . . .260
    * **F.1.34 Stack operations** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .262
    * **F.1.35 MMX instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .263
    * **F.1.36 Permanently undefined instructions** . . . . . . . . . . . . . . . . . . . . . .263
    * **F.1.37 Conditional instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . .264
    * **F.1.38 Katmai Streaming SIMD instructions (SSE –– a.k.a. KNI, XMM, MMX2)** . . . . . . .264
    * **F.1.39 Introduced in Deschutes but necessary for SSE support** . . . . . . . . . . . . . .265
    * **F.1.40 XSAVE group (AVX and extended state)** . . . . . . . . . . . . . . . . . . . . .265
    * **F.1.41 Generic memory operations** . . . . . . . . . . . . . . . . . . . . . . . . . .266
    * **F.1.42 New MMX instructions introduced in Katmai** . . . . . . . . . . . . . . . . . . .266
    * **F.1.43 AMD Enhanced 3DNow! (Athlon) instructions** . . . . . . . . . . . . . . . . . . .266
    * **F.1.44 Willamette SSE2 Cacheability Instructions** . . . . . . . . . . . . . . . . . . .266
    * **F.1.45 Willamette MMX instructions (SSE2 SIMD Integer Instructions)** . . . . . . . . . . .266
    * **F.1.46 Willamette Streaming SIMD instructions (SSE2)** . . . . . . . . . . . . . . . . . .268
    * **F.1.47 Prescott New Instructions (SSE3)** . . . . . . . . . . . . . . . . . . . . . . .269
    * **F.1.48 VMX/SVM Instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .269
    * **F.1.49 Extended Page Tables VMX instructions** . . . . . . . . . . . . . . . . . . . . .269
    * **F.1.50 SEV-SNP AMD instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . .270
    * **F.1.51 Tejas New Instructions (SSSE3)** . . . . . . . . . . . . . . . . . . . . . . . .270
    * **F.1.52 AMD SSE4A** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .270
    * **F.1.53 New instructions in Barcelona** . . . . . . . . . . . . . . . . . . . . . . . . .270
    * **F.1.54 Penryn New Instructions (SSE4.1)** . . . . . . . . . . . . . . . . . . . . . . .270
    * **F.1.55 Nehalem New Instructions (SSE4.2)** . . . . . . . . . . . . . . . . . . . . . . .271
    * **F.1.56 Intel SMX** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .272
    * **F.1.57 Geode (Cyrix) 3DNow! additions** . . . . . . . . . . . . . . . . . . . . . . . . .272
    * **F.1.58 Intel new instructions in ???** . . . . . . . . . . . . . . . . . . . . . . . . . .272
    * **F.1.59 Intel AES instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .272
    * **F.1.60 Intel AVX AES instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . .272
    * **F.1.61 Intel AES Key Locker** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .272
    * **F.1.62 Intel instruction extension based on pub number 319433-030 dated October 2017** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .272
    * **F.1.63 Intel AVX instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .273
    * **F.1.64 Intel Carry-Less Multiplication instructions (CLMUL)** . . . . . . . . . . . . . . .283
    * **F.1.65 Intel AVX Carry-Less Multiplication instructions (CLMUL)** . . . . . . . . . . . . .283
    * **F.1.66 Intel Fused Multiply-Add instructions (FMA)** . . . . . . . . . . . . . . . . . . .283
    * **F.1.67 Intel post-32 nm processor instructions** . . . . . . . . . . . . . . . . . . . . .286
    * **F.1.68 Supervisor Mode Access Prevention (SMAP)** . . . . . . . . . . . . . . . . . . .287
    * **F.1.69 VIA (Centaur) security instructions** . . . . . . . . . . . . . . . . . . . . . . .287
    * **F.1.70 AMD Lightweight Profiling (LWP) instructions** . . . . . . . . . . . . . . . . . .287
    * **F.1.71 AMD XOP and FMA4 instructions (SSE5)** . . . . . . . . . . . . . . . . . . . . .287
    * **F.1.72 Intel AVX2 instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .289
    * **F.1.73 Intel Transactional Synchronization Extensions (TSX)** . . . . . . . . . . . . . .292
    * **F.1.74 Intel Memory Protection Extensions (MPX)** . . . . . . . . . . . . . . . . . . . .292
    * **F.1.75 Intel SHA acceleration instructions** . . . . . . . . . . . . . . . . . . . . . . .292
    * **F.1.76 S3M hash instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .293
    * **F.1.77 SM4 hash instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .293
    * **F.1.78 AVX no exception conversions** . . . . . . . . . . . . . . . . . . . . . . . . .293
    * **F.1.79 AVX Vector Neural Network Instructions** . . . . . . . . . . . . . . . . . . . . .293
    * **F.1.80 AVX Vector Neural Network Instructions INT8** . . . . . . . . . . . . . . . . . . .293
    * **F.1.81 AVX Vector Neural Network Instructions INT16** . . . . . . . . . . . . . . . . . .294
    * **F.1.82 AVX Integer Fused Multiply-Add** . . . . . . . . . . . . . . . . . . . . . . . . .294
    * **F.1.83 AVX-512 mask register instructions** . . . . . . . . . . . . . . . . . . . . . . .294
    * **F.1.84 AVX-512 instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .298
    * **F.1.85 Intel memory protection keys for userspace (PKU aka PKEYs)** . . . . . . . . . . . .330
    * **F.1.86 Read Processor ID** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .330
    * **F.1.87 Processor trace write** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .330
    * **F.1.88 Instructions from the Intel Instruction Set Extensions,** . . . . . . . . . . . . . . .330
    * **F.1.89 doc 319433-034 May 2018** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .330
    * **F.1.90 doc 319433-058 June 2025** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .330
    * **F.1.91 Galois field operations (GFNI)** . . . . . . . . . . . . . . . . . . . . . . . . .330
    * **F.1.92 AVX512 Vector Bit Manipulation Instructions 2** . . . . . . . . . . . . . . . . . .331
    * **F.1.93 AVX512 VNNI** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .331
    * **F.1.94 AVX512 Bit Algorithms** . . . . . . . . . . . . . . . . . . . . . . . . . . . . .332
    * **F.1.95 AVX512 4-iteration Multiply-Add** . . . . . . . . . . . . . . . . . . . . . . . . .332
    * **F.1.96 AVX512 4-iteration Dot Product** . . . . . . . . . . . . . . . . . . . . . . . . .332
    * **F.1.97 Intel Software Guard Extensions (SGX)** . . . . . . . . . . . . . . . . . . . . .332
    * **F.1.98 Intel Control-Flow Enforcement Technology (CET)** . . . . . . . . . . . . . . . .332
    * **F.1.99 Instructions from ISE doc 319433-040, June 2020** . . . . . . . . . . . . . . . . .332
    * **F.1.100 AVX512 Bfloat16 instructions** . . . . . . . . . . . . . . . . . . . . . . . . .333
    * **F.1.101 AVX512 mask intersect instructions** . . . . . . . . . . . . . . . . . . . . . .333
    * **F.1.102 Intel Advanced Matrix Extensions (AMX)** . . . . . . . . . . . . . . . . . . . . .333
    * **F.1.103 Intel AVX512-FP16 instructions** . . . . . . . . . . . . . . . . . . . . . . . . .334
    * **F.1.104 RAO-INT weakly ordered atomic operations** . . . . . . . . . . . . . . . . . . .338
    * **F.1.105 User interrupts** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .338
    * **F.1.106 Flexible Return and Exception Delivery** . . . . . . . . . . . . . . . . . . . . .338
    * **F.1.107 History reset** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .338
    * **F.1.108 AVX10.2 BF16 instructions** . . . . . . . . . . . . . . . . . . . . . . . . . . .338
    * **F.1.109 AVX10.2 Compare scalar fp with enhanced eflags instructions** . . . . . . . . . . .339
    * **F.1.110 AVX10.2 Convert instructions** . . . . . . . . . . . . . . . . . . . . . . . . . .340
    * **F.1.111 AVX10.2 Integer and FP16 VNNI, media new instructions** . . . . . . . . . . . . . .340
    * **F.1.112 AVX10.2 MINMAX instructions** . . . . . . . . . . . . . . . . . . . . . . . . . .341
    * **F.1.113 AVX10.2 Saturating convert instructions** . . . . . . . . . . . . . . . . . . . . .341
    * **F.1.114 AVX10.2 Zero-extending partial vector copy instructions** . . . . . . . . . . . . .342
    * **F.1.115 AVX512BMM** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .342
    * **F.1.116 Systematic names for the hinting nop instructions** . . . . . . . . . . . . . . . .342

---

## Chapter 1: Introduction

### 1.1 What Is NASM?
The Netwide Assembler, NASM, is an 80x86 and x86-64 assembler designed for portability and modularity. It supports a range of object file formats, including Linux and BSD a.out, ELF, Mach-O, 16-bit and 32-bit .obj (OMF) format, COFF (including its Win32 and Win64 variants.) It can also output plain binary files, Intel hex and Motorola S-Record formats. Its syntax is designed to be simple and easy to understand, similar to the syntax in the Intel Software Developer Manual with minimal complexity. It supports all currently known x86 architectural extensions, and has strong support for macros.

### 1.1.1 License
NASM is under the so-called 2-clause BSD license, also known as the simplified BSD license:

**Copyright 1996-2025 the NASM Authors – All rights reserved.**

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

*THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.*

---

## Chapter 2: Running NASM

### 2.1 NASM Command-Line Syntax
To assemble a file, you issue a command of the form:

```bash
nasm -f <format> <filename> [-o <output>]
```

For example,

```bash
nasm -f elf myfile.asm
```

will assemble `myfile.asm` into an 32-bit ELF object file `myfile.o`. And

```bash
nasm -f bin myfile.asm -o myfile.com
```

will assemble `myfile.asm` into a raw binary file `myfile.com`.

To produce a listing file, with the hex codes output from NASM displayed on the left of the original sources, use the `-l` option to give a listing file name, for example:

```bash
nasm -f coff myfile.asm -l myfile.lst
```

To get further usage instructions from NASM, try typing:

```bash
nasm -h
```

The option `--help` is an alias for the `-h` option.

Like Unix compilers and assemblers, NASM is silent unless it goes wrong: you won’t see any output at all, unless it gives error messages.

### 2.1.1 The -o Option: Output File Name
NASM will normally choose the name of your output file for you; precisely how it does this is dependent on the object file format. For Microsoft object file formats (obj, win32 and win64), it will remove the `.asm` extension (or whatever extension you like to use – NASM doesn’t care) from your source file name and substitute `.obj`. For Unix object file formats (aout, as86, coff, elf32, elf64, elfx32, ieee, macho32 and macho64) it will substitute `.o`. For dbg, ith and srec, it will use `.dbg`, `.ith` and `.srec`, respectively, and for the bin format it will simply remove the extension, so that `myfile.asm` produces the output file `myfile`.

If the output file already exists, NASM will overwrite it, unless it has the same name as the input file, in which case it will give a warning and use `nasm.out` as the output file name instead.

For situations in which this behaviour is unacceptable, NASM provides the `-o` command-line option, which allows you to specify your desired output file name. You invoke `-o` by following it with the name you wish for the output file, either with or without an intervening space. For example:

```bash
nasm -f bin program.asm -o program.com
nasm -f bin driver.asm -odriver.sys
```

Note that this is a small `o`, and is different from a capital `O`, which is used to specify the number of optimization passes required. See section 2.1.24.

### 2.1.2 The -f Option: Output File Format
If you do not supply the `-f` option to NASM, it will choose an output file format for you itself. In the distribution versions of NASM, the default is always `bin`; if you’ve compiled your own copy of NASM, you can redefine `OF_DEFAULT` at compile time and choose what you want the default to be.

Like `-o`, the intervening space between `-f` and the output file format is optional; so `-f elf` and `-felf` are both valid.

A complete list of the available output file formats can be given by issuing the command `nasm -h`.

### 2.1.3 The -l Option: Generating a Listing File
If you supply the `-l` option to NASM, followed (with the usual optional space) by a file name, NASM will generate a source-listing file for you, in which addresses and generated code are listed on the left, and the actual source code, with expansions of multi-line macros (except those which specifically request no expansion in source listings: see section 5.6.11) on the right. For example:

```bash
nasm -f elf myfile.asm -l myfile.lst
```

If a list file is selected, you may turn off listing for a section of your source with `[list -]`, and turn it back on with `[list +]`, (the default, obviously). There is no "user form" (without the brackets). This can be used to list only sections of interest, avoiding excessively long listings.

### 2.1.4 The -L Option: Additional or Modified Listing Info
Use this option to specify listing output details.

`-L` options for general use are:
* `-Lb` show builtin macro packages (standard and `%use`, see section 5.9.4)
* `-Lc` list the data from `INCBIN` files (see section 3.2.3)
* `-Ld` show byte and repeat counts in decimal, not hex
* `-Le` show the preprocessed output
* `-Lf` ignore `.nolist` (force output) (see section 5.6.11)
* `-LF` ignore `[LIST -]` directives (force output) (see section 8.15)
* `-Lm` show multi-line macro calls with expanded parameters
* `-Lp` output a list file every pass, in case of errors
* `-Ls` show all single-line macro definitions
* `-Lt` list the full output from `TIMES` and `ALIGN` directives
* `-L+` equivalent to `-LbdefFmps`
* `-L++` equivalent to `-L+ -Lct`

`-L` options intended for the debugging of NASM itself (including bug reporting), and not likely to be otherwise useful:
* `-Lw` flush the output after every line (very slow!)
* `-LX` list instruction pattern line numbers from `insns.xda`
* `-L!` enable all listing options including debugging ones

For forward compatibility reasons, an undefined flag will be ignored. Thus, a new flag introduced in a newer version of NASM can be specified without breaking older versions. Listing flags will always be a single alphanumeric character and are case sensitive.

These options can be enabled or disabled at runtime using the `%pragma list options` directive:

```nasm
%pragma list options [+|-|*]{!|flags}...
```

`+`, `-` and `*` adds, removes, or restores to the command-line default the flags that follow.

For example, to turn on the `d` and `m` flags but disable the `s` flag:

```nasm
%pragma list options +dm -s
```

The `+` and `++` shorthands available in on the command line are not available when using `%pragma list options`; each listing option needs to be specified explicitly, or `!` can be used to specify all options.

Spaces, quotation marks, and commas in the argument are explicitly ignored; thus, specifying the options as one or more quoted strings is valid.

The built-in macros `__?LIST_OPTIONS?__` and `__?LIST_OPTIONS_DEFAULT?__` contain the currently active and the command-line default listing options, respectively, as quoted strings.

To save and restore the listing options, one can use:

```nasm
%macro ...
%define %%saved_list_options __?LIST_OPTIONS?__
; ... do stuff with special listing options ...
%pragma list options -! +%%saved_list_options
%endmacro
```

The statement:

```nasm
%pragma list options -! +__?LIST_OPTIONS_DEFAULT?__
```

... is exactly equivalent to ...

```nasm
%pragma list options *!
```

### 2.1.5 The -M Option: Generate Makefile Dependencies
This option can be used to generate makefile dependencies on `stdout`. This can be redirected to a file for further processing. For example:

```bash
nasm -M myfile.asm > myfile.dep
```

### 2.1.6 The -MG Option: Generate Makefile Dependencies
This option can be used to generate makefile dependencies on `stdout`. This differs from the `-M` option in that if a nonexisting file is encountered, it is assumed to be a generated file and is added to the dependency list without a prefix.

### 2.1.7 The -MF Option: Set Makefile Dependency File
This option can be used with the `-M` or `-MG` options to send the output to a file, rather than to `stdout`. For example:

```bash
nasm -M -MF myfile.dep myfile.asm
```

### 2.1.8 The -MD Option: Assemble and Generate Dependencies
The `-MD` option acts as the combination of the `-M` and `-MF` options (i.e. a filename has to be specified.) However, unlike the `-M` or `-MG` options, `-MD` does not inhibit the normal operation of the assembler. Use this to automatically generate updated dependencies with every assembly session. For example:

```bash
nasm -f elf -o myfile.o -MD myfile.dep myfile.asm
```

If the argument after `-MD` is an option rather than a filename, then the output filename is the first applicable one of:
* the filename set in the `-MF` option;
* the output filename from the `-o` option with `.d` appended;
* the input filename with the extension set to `.d`.

### 2.1.9 The -MT Option: Dependency Target Name
The `-MT` option can be used to override the default name of the dependency target. This is normally the same as the output filename, specified by the `-o` option.

### 2.1.10 The -MQ Option: Dependency Target Name (Quoted)
The `-MQ` option acts as the `-MT` option, except it tries to quote characters that have special meaning in Makefile syntax. This is not foolproof, as not all characters with special meaning are quotable in make. The default output (if no `-MT` or `-MQ` option is specified) is automatically quoted.

### 2.1.11 The -MP Option: Emit Phony Makefile Targets
When used with any of the dependency generation options, the `-MP` option causes NASM to emit a phony target without dependencies for each header file. This prevents make from complaining if a header file has been removed.

### 2.1.12 The -MW Option: Watcom make quoting style
This option causes NASM to attempt to quote dependencies according to Watcom make conventions rather than POSIX make conventions (also used by most other make variants.) This quotes `#` as `$#` rather than `\#`, uses `&` rather than `\` for continuation lines, and encloses filenames containing whitespace in double quotes.

### 2.1.13 The -F Option: Debug Information Format
This option is used to select the format of the debug information emitted into the output file, to be used by a debugger (or will be). Prior to version 2.03.01, the use of this switch did not enable output of the selected debug info format. Use `-g`, see section 2.1.14, to enable output. Versions 2.03.01 and later automatically enable `-g` if `-F` is specified.

A complete list of the available debug file formats for an output format can be seen by issuing the command `nasm -h`. Not all output formats currently support debugging output.

This should not be confused with the `-f dbg` output format option, see section 9.14.

### 2.1.14 The -g Option: Enabling Debug Information.
This option can be used to generate debugging information in the specified format. See section 2.1.13. Using `-g` without `-F` results in emitting debug info in the default format, if any, for the selected output format. If no debug information is currently implemented in the selected output format, `-g` is silently ignored.

### 2.1.15 The -X Option: Selecting an Error Reporting Format
This option can be used to select an error reporting format for any error messages that might be produced by NASM.

Currently, two error reporting formats may be selected. They are the `-Xvc` option and the `-Xgnu` option. The GNU format is the default and looks like this:

```text
filename.asm:65: error: specific error message
```

where `filename.asm` is the name of the source file in which the error was detected, `65` is the source file line number on which the error was detected, `error` is the severity of the error (this could be warning), and `specific error message` is a more detailed text message which should help pinpoint the exact problem.

The other format, specified by `-Xvc` is the style used by Microsoft Visual C++ and some other programs. It looks like this:

```text
filename.asm(65) : error: specific error message
```

where the only difference is that the line number is in parentheses instead of being delimited by colons.

See also the Visual C++ output format, section 9.6.

### 2.1.16 The -Z Option: Send Errors to a File
Under MS-DOS it can be difficult (though there are ways) to redirect the standard-error output of a program to a file. Since NASM usually produces its warning and error messages on `stderr`, this can make it hard to capture the errors if (for example) you want to load them into an editor.

NASM therefore provides the `-Z` option, taking a filename argument which causes errors to be sent to the specified files rather than standard error. Therefore you can redirect the errors into a file by typing:

```bash
nasm -Z myfile.err -f obj myfile.asm
```

In earlier versions of NASM, this option was called `-E`, but it was changed since `-E` is an option conventionally used for preprocessing only, with disastrous results. See section 2.1.22.

### 2.1.17 The -s Option: Send Errors to stdout
The `-s` option redirects error messages to `stdout` rather than `stderr`, so it can be redirected under MS-DOS. To assemble the file `myfile.asm` and pipe its output to the `more` program, you can type:

```bash
nasm -s -f obj myfile.asm | more
```

See also the `-Z` option, section 2.1.16.

### 2.1.18 The -i Option: Include File Search Directories
When NASM sees the `%include` or `%pathsearch` directive in a source file (see section 5.9.1, section 5.9.2 or section 3.2.3), it will search for the given file not only in the current directory, but also in any directories specified on the command line by the use of the `-i` option. Therefore you can include files from a macro library, for example, by typing:

```bash
nasm -ic:\macrolib\ -f obj myfile.asm
```

(As usual, a space between `-i` and the path name is allowed, and optional).

Prior NASM 2.14 a path provided in the option has been considered as a verbatim copy and providing a path separator been up to a caller. One could implicitly concatenate a search path together with a filename. Still this was rather a trick than something useful. Now the trailing path separator is made to always present, thus `-ifoo` will be considered as the `-ifoo/` directory.

If you want to define a standard include search path, similar to `/usr/include` on Unix systems, you should place one or more `-i` directives in the `NASMENV` environment variable (see section 2.1.36).

For Makefile compatibility with many C compilers, this option can also be specified as `-I`.

### 2.1.19 The -p Option: Pre-Include a File
NASM allows you to specify files to be pre-included into your source file, by the use of the `-p` option. So running:

```bash
nasm myfile.asm -p myinc.inc
```

is equivalent to running `nasm myfile.asm` and placing the directive `%include "myinc.inc"` at the start of the file.

`--include` option is also accepted.

For consistency with the `-I`, `-D` and `-U` options, this option can also be specified as `-P`.

### 2.1.20 The -d Option: Pre-Define a Macro
Just as the `-p` option gives an alternative to placing `%include` directives at the start of a source file, the `-d` option gives an alternative to placing a `%define` directive. You could code:

```bash
nasm myfile.asm -dFOO=100
```

as an alternative to placing the directive:

```nasm
%define FOO 100
```

at the start of the file. You can miss off the macro value, as well: the option `-dFOO` is equivalent to coding `%define FOO`. This form of the directive may be useful for selecting assembly-time options which are then tested using `%ifdef`, for example `-dDEBUG`.

For Makefile compatibility with many C compilers, this option can also be specified as `-D`.

### 2.1.21 The -u Option: Undefine a Macro
The `-u` option undefines a macro that would otherwise have been pre-defined, either automatically or by a `-p` or `-d` option specified earlier on the command lines.

For example, the following command line:

```bash
nasm myfile.asm -dFOO=100 -uFOO
```

would result in `FOO` not being a predefined macro in the program. This is useful to override options specified at a different point in a Makefile.

For Makefile compatibility with many C compilers, this option can also be specified as `-U`.

### 2.1.22 The -E Option: Preprocess Only
NASM allows the preprocessor to be run on its own, up to a point. Using the `-E` option (which requires no arguments) will cause NASM to preprocess its input file, expand all the macro references, remove all the comments and preprocessor directives, and print the resulting file on standard output (or save it to a file, if the `-o` option is also used).

This option cannot be applied to programs which require the preprocessor to evaluate expressions which depend on the values of symbols: so code such as:

```nasm
%assign tablesize ($-tablestart)
```

will cause an error in preprocess-only mode.

For compatibility with older version of NASM, this option can also be written `-e`. `-E` in older versions of NASM was the equivalent of the current `-Z` option, section 2.1.16.

### 2.1.23 The -a Option: Suppress Preprocessing
If NASM is being used as the back end to a compiler, it might be desirable to suppress preprocessing completely and assume the compiler has already done it, to save time and increase compilation speeds. The `-a` option, requiring no argument, instructs NASM to replace its powerful preprocessor with a stub preprocessor which does nothing.

### 2.1.24 The -O Option: Multipass Optimization
Using the `-O` option, you can tell NASM to carry out different levels of optimization. Multiple flags can be specified after the `-O` options, some of which can be combined in a single option, e.g. `-Oxv`.

* **`-O0`**: No optimization. All operands take their long forms, if a short form is not specified, except conditional jumps. This is intended to match NASM 0.98 behavior.
* **`-O1`**: Minimal optimization. As above, but immediate operands which will fit in a signed byte are optimized, unless the long form is specified. Conditional jumps default to the long form unless otherwise specified.
* **`-Ox`** (where `x` is the actual letter `x`): Multipass optimization. Minimize branch offsets and signed immediate bytes, overriding size specification unless the `strict` keyword has been used (see section 3.7). For compatibility with earlier releases, the letter `x` may also be any number greater than one. This number has no effect on the actual number of passes.
* **`-Ov`**: At the end of assembly, print the number of passes actually executed.

The `-Ox` mode is recommended for most uses, and is the default since NASM 2.09. Any other mode will generate worse quality output. Use `-O0` or `-O1` only if you need the finer programmer-level control of output and `strict` is not suitable for your use case.

Note that this is a capital `O`, and is different from a small `o`, which is used to specify the output file name. See section 2.1.1.

### 2.1.25 The -t Option: TASM Compatibility Mode
NASM includes a limited form of compatibility with Borland’s TASM. When NASM’s `-t` option is used, the following changes are made:
* local labels may be prefixed with `@@` instead of `.`
* size override is supported within brackets. In TASM compatible mode, a size override inside square brackets changes the size of the operand, and not the address type of the operand as it does in NASM syntax. E.g. `mov eax,[DWORD val]` is valid syntax in TASM compatibility mode. Note that you lose the ability to override the default address type for the instruction.
* unprefixed forms of some directives supported (`arg`, `elif`, `else`, `endif`, `if`, `ifdef`, `ifdifi`, `ifndef`, `include`, `local`)

### 2.1.26 The -w and -W Options: Enable or Disable Assembly Warnings
NASM can observe many conditions during the course of assembly which are worth mentioning to the user, but not a sufficiently severe error to justify NASM refusing to generate an output file. These conditions are reported like errors, but come up with the word ‘warning’ before the message. Warnings do not prevent NASM from generating an output file and returning a success status to the operating system.

Some conditions are even less severe than that: they are only sometimes worth mentioning to the user. Therefore NASM supports the `-w` command-line option, which enables or disables certain classes of assembly warning. Such warning classes are described by a name, for example `label-orphan`; you can enable warnings of this class by the command-line option `-w+label-orphan` and disable it by `-w-label-orphan`.

Since version 2.15, NASM has group aliases for all prefixed warnings, so they can be used to enable or disable all warnings in the group. For example, `-w+float` enables all warnings with names starting with `float-*`.

Since version 2.00, NASM has also supported the gcc–like syntax `-Wwarning-class` and `-Wno-warning-class` instead of `-w+warning-class` and `-w-warning-class`, respectively; both syntaxes work identically.

The option `-w+error` or `-Werror` can be used to treat warnings as errors. This can be controlled on a per warning class basis (`-w+error=warning-class` or `-Werror=warning-class`); if no `warning-class` is specified NASM treats it as `-w+error=all`; the same applies to `-w-error` or `-Wno-error`, of course.

In addition, you can control warnings in the source code itself, using the `[WARNING]` directive. See section 8.14.

See appendix A for the complete list of warning classes.

### 2.1.27 The -v Option: Display Version Info
Typing `nasm -v` will display the version of NASM which you are using, and the date on which it was compiled.

You will need the version number if you report a bug.

For command-line compatibility with Yasm, the form `--v` is also accepted for this option starting in NASM version 2.11.05.

### 2.1.28 The --[gl]prefix and --[gl]postfix Options
The `--gprefix` option prepends the given argument to all extern, common, static, and global symbols, and the `--lprefix` option prepends to all other symbols. Similarly, `--gpostfix` and `--lpostfix` options append the argument, in a manner similar to the `--[gl]prefix` options.

Running this:

```bash
nasm -f macho --gprefix _
```

is equivalent to placing the directive `%pragma macho gprefix _` at the start of the file (section 8.10). It will prepend the underscore to all global and external variables, as C requires it in some, but not all, system calling conventions.

`--prefix` is an alias for `--gprefix`.

See section 8.10 for the equivalent directives and pragmas.

Earlier versions of NASM called the pragmas `suffix` and the options `--postfix`, and did not implement directives at all despite being so documented. Since NASM 3.01, the directive forms are implemented, and directives, pragmas and options all support all spellings.

### 2.1.29 The --pragma Option
NASM accepts an argument as `%pragma option`, which is like placing a `%pragma preprocess` statement at the beginning of the source. Running this:

```bash
nasm -f macho --pragma "macho gprefix _"
```

is equivalent to the example in section 2.1.28. See section 5.13.

### 2.1.30 The --before Option
Insert a statement (usually, but not necessarily) a preprocess statement before the input file. The example shown in section 2.1.29 is the same as running this:

```bash
nasm -f macho --before "%pragma macho gprefix _"
```

### 2.1.31 The --bits Option
Set the processor mode by inserting a `BITS` directive (see section 8.1) before the input file. The following two statements are exactly equivalent:

```bash
nasm -f bin --bits 16 file.asm
nasm -f bin --before "BITS 16" file.asm
```

The `--bits` option was introduced in NASM 3.01; the `--before` form can be used for compatibility with older versions of NASM.

### 2.1.32 The --limit- Options
These options allows user to setup various maximum values after which NASM will terminate with a fatal error rather than consume arbitrary amount of compute time. Each limit can be set to a positive number, `unlimited`, `maximum`, or `default`.

* **`--limit-passes`**: Number of maximum allowed passes. Default is unlimited.
* **`--limit-stalled-passes`**: Maximum number of allowed unfinished passes. Default is 1000.
* **`--limit-macro-levels`**: Define maximum depth of macro expansion (in preprocess). Default is 10000
* **`--limit-macro-tokens`**: Maximum number of tokens processed during single-line macro expansion. Default is 10000000.
* **`--limit-mmacros`**: Maximum number of multi-line macros processed before returning to the top-level input. Default is 100000.
* **`--limit-rep`**: Maximum number of allowed preprocessor loop, defined under `%rep`. Default is 1000000.
* **`--limit-eval`**: This number sets the maximum allowed expression length. Default is 8192 on most systems.
* **`--limit-lines`**: Total number of source lines allowed to be processed. Default is 2000000000.
* **`--limit-params`**: Maximum number of multi-line macro parameters. Default is 16383.

For example, set the maximum line count to 1000:

```bash
nasm --limit-lines 1000
```

Limits can also be set via the directive `%pragma limit`, for example:

```nasm
%pragma limit lines 1000
```

Specifying the limit value as `*` or `reset` resets the limit to the value specified on the command line or the default value, undoing any previous `%pragma limit`.

See also the `%limit()` preprocessor function (section 5.5.13) and the `__?NASM_LIMITS?__` standard macro (section 6.8).

### 2.1.33 The --keep-all Option
This option prevents NASM from deleting any output files even if an error happens.

### 2.1.34 The --no-line Option
If this option is given, all `%line` directives in the source code are ignored. This can be useful for debugging already preprocessed code. See section 5.14.1.

### 2.1.35 The --reproducible Option
If this option is given, NASM will not emit information that is inherently dependent on the NASM version or different from run to run (such as timestamps) into the output file.

### 2.1.36 The NASMENV Environment Variable
If you define an environment variable called `NASMENV`, the program will interpret it as a list of extra command-line options, which are processed before the real command line. You can use this to define standard search directories for include files, by putting `-i` options in the `NASMENV` variable.

The value of the variable is split up at white space, so that the value `-s -ic:\nasmlib\` will be treated as two separate options. However, that means that the value `-dNAME="my name"` won’t do what you might want, because it will be split at the space and the NASM command-line processing will get confused by the two nonsensical words `-dNAME="my` and `name"`.

To get round this, NASM provides a feature whereby, if you begin the `NASMENV` environment variable with some character that isn’t a minus sign, then NASM will treat this character as the separator character for options. So setting the `NASMENV` variable to the value `!-s!-ic:\nasmlib\` is equivalent to setting it to `-s -ic:\nasmlib\`, but `!-dNAME="my name"` will work.

This environment variable was previously called `NASM`. This was changed with version 0.98.31.

---

## 2.2 Quick Start for MASM Users
If you’re used to writing programs with MASM, or with TASM in MASM-compatible (non-Ideal) mode, or with a86, this section attempts to outline the major differences between MASM’s syntax and NASM’s. If you’re not already used to MASM, it’s probably worth skipping this section.

### 2.2.1 NASM Is Case-Sensitive
One simple difference is that NASM is case-sensitive. It makes a difference whether you call your label `foo`, `Foo` or `FOO`. If you’re assembling to DOS or OS/2 `.OBJ` files, you can invoke the `UPPERCASE` directive (documented in section 9.4) to ensure that all symbols exported to other code modules are forced to be upper case; but even then, within a single module, NASM will distinguish between labels differing only in case.

### 2.2.2 NASM Requires Square Brackets For Memory References
NASM was designed with simplicity of syntax in mind. One of the design goals of NASM is that it should be possible, as far as is practical, for the user to look at a single line of NASM code and tell what opcode is generated by it. You can’t do this in MASM: if you declare, for example,

```nasm
foo equ 1
bar dw 2
```

then the two lines of code

```nasm
mov ax,foo
mov ax,bar
```

generate completely different opcodes, despite having identical-looking syntaxes.

NASM avoids this undesirable situation by having a much simpler syntax for memory references. The rule is simply that **any access to the contents of a memory location requires square brackets around the address, and any access to the address of a variable doesn’t.** So an instruction of the form `mov ax,foo` will always refer to a compile-time constant, whether it’s an `EQU` or the address of a variable; and to access the contents of the variable `bar`, you must code `mov ax,[bar]`.

This also means that NASM has no need for MASM’s `OFFSET` keyword, since the MASM code `mov ax,offset bar` means exactly the same thing as NASM’s `mov ax,bar`. If you’re trying to get large amounts of MASM code to assemble sensibly under NASM, you can always code:

```nasm
%idefine offset
```

to make the preprocessor treat the `OFFSET` keyword as a no-op.

This issue is even more confusing in a86, where declaring a label with a trailing colon defines it to be a ‘label’ as opposed to a ‘variable’ and causes a86 to adopt NASM-style semantics; so in a86, `mov ax,var` has different behaviour depending on whether `var` was declared as `var: dw 0` (a label) or `var dw 0` (a word-size variable). NASM is very simple by comparison: everything is a label.

NASM, in the interests of simplicity, also does not support the hybrid syntaxes supported by MASM and its clones, such as `mov ax,table[bx]`, where a memory reference is denoted by one portion outside square brackets and another portion inside. The correct syntax for the above is `mov ax,[table+bx]`. Likewise, `mov ax,es:[di]` is wrong and `mov ax,[es:di]` is right.

### 2.2.3 NASM Doesn’t Store Variable Types
NASM, by design, chooses not to remember the types of variables you declare. Whereas MASM will remember, on seeing `var dw 0`, that you declared `var` as a word-size variable, and will then be able to fill in the ambiguity in the size of the instruction `mov var,2`, NASM will deliberately remember nothing about the symbol `var` except where it begins, and so you must explicitly code `mov word [var],2`.

For this reason, NASM doesn’t support the `LODS`, `MOVS`, `STOS`, `SCAS`, `CMPS`, `INS`, or `OUTS` instructions, but only supports the forms such as `LODSB`, `MOVSW`, and `SCASD`, which explicitly specify the size of the components of the strings being manipulated.

### 2.2.4 NASM Doesn’t ASSUME
As part of NASM’s drive for simplicity, it also does not support the `ASSUME` directive. NASM will not keep track of what values you choose to put in your segment registers, and will never automatically generate a segment override prefix.

### 2.2.5 NASM Doesn’t Support Memory Models
NASM also does not have any directives to support different 16-bit memory models. The programmer has to keep track of which functions are supposed to be called with a far call and which with a near call, and is responsible for putting the correct form of `RET` instruction (`RETN` or `RETF`; NASM accepts `RET` itself as an alternate form for `RETN`); in addition, the programmer is responsible for coding `CALL FAR` instructions where necessary when calling external functions, and must also keep track of which external variable definitions are far and which are near.

### 2.2.6 Floating-Point Differences
NASM uses different names to refer to floating-point registers from MASM: where MASM would call them `ST(0)`, `ST(1)` and so on, and a86 would call them simply `0`, `1` and so on, NASM chooses to call them `st0`, `st1` etc.

### 2.2.7 Other Differences
For historical reasons, NASM uses the keyword `TWORD` where MASM and compatible assemblers use `TBYTE`.

Historically, NASM does not declare uninitialized storage in the same way as MASM: where a MASM programmer might use `stack db 64 dup (?)`, NASM requires `stack resb 64`, intended to be read as ‘reserve 64 bytes’. As of NASM 2.15, the MASM syntax is also supported.

In addition to all of this, macros and directives work completely differently to MASM. See chapter 5 and chapter 8 for further details.

### 2.2.8 MASM compatibility package
The MASM compatibility macro package can be used to improve MASM compatibility. See section 7.5.

---

## Chapter 3: The NASM Language

### 3.1 Layout of a NASM Source Line
Like most assemblers, each NASM source line contains (unless it is a macro, a preprocessor directive or an assembler directive: see chapter 5 and chapter 8) some combination of the four fields:

```nasm
label: instruction operands ; comment
```

As usual, most of these fields are optional; the presence or absence of any combination of a label, an instruction and a comment is allowed. Of course, the operand field is either required or forbidden by the presence and nature of the instruction field.

NASM uses backslash (`\`) as the line continuation character; if a line ends with backslash, the next line is considered to be a part of the backslash-ended line.

NASM places no restrictions on white space within a line: labels may have white space before them, or instructions may have no space before them, or anything. The colon after a label is also optional. (Note that this means that if you intend to code `lodsb` alone on a line, and type `lodab` by accident, then that’s still a valid source line which does nothing but define a label. Running NASM with the command-line option `-w+orphan-labels` will cause it to warn you if you define a label alone on a line without a trailing colon.)

Valid characters in labels are letters, numbers, `_`, `$`, `#`, `@`, `~`, `.`, and `?`. The only characters which may be used as the first character of an identifier are letters, `.` (with special meaning: see section 3.9), `_` and `?`. An identifier may also be prefixed with a `$` to indicate that it is intended to be read as an identifier and not a reserved word; thus, if some other module you are linking with defines a symbol called `eax`, you can refer to `$eax` in NASM code to distinguish the symbol from the register. Maximum length of an identifier is 4095 characters.

The instruction field may contain any machine instruction: Pentium and P6 instructions, FPU instructions, MMX instructions and even undocumented instructions are all supported. The instruction may be prefixed by `LOCK`, `REP`, `REPE/REPZ`, `REPNE/REPNZ`, `XACQUIRE/XRELEASE` or `BND/NOBND`, in the usual way. Explicit address-size and operand-size prefixes `A16`, `A32`, `A64`, `O16` and `O32`, `O64` are provided – one example of their use is given in chapter 12. You can also use the name of a segment register as an instruction prefix: coding `es mov [bx],ax` is equivalent to coding `mov [es:bx],ax`. We recommend the latter syntax, since it is consistent with other syntactic features of the language, but for instructions such as `LODSB`, which has no operands and yet can require a segment override, there is no clean syntactic way to proceed apart from:

```nasm
es mov [bx],ax
mov [es:bx],ax
es lodsb
```

An instruction is not required to use a prefix: prefixes such as `CS`, `A32`, `LOCK` or `REPE` can appear on a line by themselves, and NASM will just generate the prefix bytes.

In addition to actual machine instructions, NASM also supports a number of pseudo-instructions, described in section 3.2.

Instruction operands may take a number of forms: they can be registers, described simply by the register name (e.g. `ax`, `bp`, `ebx`, `cr0`: NASM does not use the gas–style syntax in which register names must be prefixed by a `%` sign), or they can be effective addresses (see section 3.3), constants (section 3.4) or expressions (section 3.5).

For x87 floating-point instructions, NASM accepts a wide range of syntaxes: you can use two-operand forms like MASM supports, or you can use NASM’s native single-operand forms in most cases. For example, you can code:

```nasm
fadd st1 ; this sets st0 := st0 + st1
fadd st0,st1 ; so does this
fadd st1,st0 ; this sets st1 := st1 + st0
fadd to st1 ; so does this
```

Almost any x87 floating-point instruction that references memory must use one of the prefixes `DWORD`, `QWORD` or `TWORD` to indicate what size of memory operand it refers to.

### 3.2 Pseudo-Instructions
Pseudo-instructions are things which, though not real x86 machine instructions, are used in the instruction field anyway because that’s the most convenient place to put them. The current pseudo-instructions are `DB`, `DW`, `DD`, `DQ`, `DT`, `DO`, `DY` and `DZ`; their uninitialized counterparts `RESB`, `RESW`, `RESD`, `RESQ`, `REST`, `RESO`, `RESY` and `RESZ`; the `INCBIN` command, the `EQU` command, and the `TIMES` prefix.

In this documentation, the notation "Dx" and "RESx" is used to indicate all the `DB` and `RESB` type directives, respectively.

#### 3.2.1 Dx: Declaring Initialized Data
`DB`, `DW`, `DD`, `DQ`, `DT`, `DO`, `DY` and `DZ` (collectively "Dx" in this documentation) are used, much as in MASM, to declare initialized data in the output file. They can be invoked in a wide range of ways:

```nasm
db 0x55 ; just the byte 0x55
db 0x55,0x56,0x57 ; three bytes in succession
db ’a’,0x55 ; character constants are OK
db ’hello’,13,10,’$’ ; so are string constants
dw 0x1234 ; 0x34 0x12
dw ’a’ ; 0x61 0x00 (it’s just a number)
dw ’ab’ ; 0x61 0x62 (character constant)
dw ’abc’ ; 0x61 0x62 0x63 0x00 (string)
dd 0x12345678 ; 0x78 0x56 0x34 0x12
dd 1.234567e20 ; floating-point constant
dq 0x123456789abcdef0 ; eight byte constant
dq 1.234567e20 ; double-precision float
dt 1.234567e20 ; extended-precision float
```

`DT`, `DO`, `DY` and `DZ` do not accept integer numeric constants as operands.

Starting in NASM 2.15, a the following MASM–like features have been implemented:
* A `?` argument to declare uninitialized storage:

```nasm
db ? ; uninitialized
```

* A superset of the `DUP` syntax. The NASM version of this has the following syntax specification; capital letters indicate literal keywords:

```text
dx := DB | DW | DD | DQ | DT | DO | DY | DZ
type := BYTE | WORD | DWORD | QWORD | TWORD | OWORD | YWORD | ZWORD
atom := expression | string | float | ’?’
parlist := ’(’ value [’,’ value ...] ’)’
duplist := expression DUP [type] [’%’] parlist
list := duplist | ’%’ parlist | type [’%’] parlist
value := [type] atom | list
stmt := dx value [’,’ value ...]
```

Note that a list needs to be prefixed with a `%` sign unless prefixed by either `DUP` or a type in order to avoid confusing it with a parenthesis starting an expression. The following expressions are all valid:

```nasm
db 33
db (44) ; Integer expression
; db (44,55) ; Invalid - error
db %(44,55)
db %(’XX’,’YY’)
db (’AA’) ; Integer expression - outputs single byte
db %(’BB’) ; List, containing a string
db ?
db 6 dup (33)
db 6 dup (33, 34)
db 6 dup (33, 34), 35
db 7 dup (99)
db 7 dup dword (?, word ?, ?)
dw byte (?,44)
dw 3 dup (0xcc, 4 dup byte (’PQR’), ?), 0xabcd
dd 16 dup (0xaaaa, ?, 0xbbbbbb)
dd 64 dup (?)
```

The use of `$` (current address) in a Dx statement is undefined in the current version of NASM, except in the following cases:
* For the first expression in the statement, either a `DUP` or a data item.
* An expression of the form `"value - $"`, which is converted to a self-relative relocation.

Future versions of NASM is likely to produce a different result or issue an error this case. There is no such restriction on using `$$` or section-relative symbols.

#### 3.2.2 RESB and Friends: Declaring Uninitialized Data
`RESB`, `RESW`, `RESD`, `RESQ`, `REST`, `RESO`, `RESY` and `RESZ` are designed to be used in the BSS section of a module: they declare uninitialized storage space. Each takes a single operand, which is the number of bytes, words, doublewords or whatever to reserve. The operand to a `RESB`–type pseudo-instruction would be a critical expression (see section 3.8), except that for legacy compatibility reasons forward references are permitted, however the code will be extremely fragile and this should be considered a severe programming error. A warning will be issued; code generating this warning should be remedied as quickly as possible (see the forward class in appendix A.)

For example:

```nasm
buffer: resb 64 ; reserve 64 bytes
wordvar: resw 1 ; reserve a word
realarray resq 10 ; array of ten reals
ymmval: resy 1 ; one YMM register
zmmvals: resz 32 ; 32 ZMM registers
```

Since NASM 2.15, the MASM syntax of using `?` and `DUP