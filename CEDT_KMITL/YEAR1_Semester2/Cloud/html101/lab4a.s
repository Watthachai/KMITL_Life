.global _start

_start:
   MOV R7, #3        @ Request to read from file
   MOV R0, #1        @ File descriptor of input, stdin
   MOV R2, #2        @ Number of bytes to read, i.e., two bytes
   LDR R1, =Lab4     @ Address of buffer to read data into
   SWI 0             @ Invoke kernel to read from file

   LDRB R0, [R1, #0] @ Load the first character from the input buffer
   LDRB R2, [R1, #1] @ Load the second character from the input buffer
   SUB R0, R0, #48   @ Convert the ASCII digit to a decimal value
   SUB R2, R2, #48   @ Convert the ASCII digit to a decimal value

   MOV R10, #10      @ Set the multiplier to 10
   MUL R11, R0, R10  @ Multiply the first decimal digit by 10
   ADDS R9, R11, R2  @ Add the second decimal digit to the product

   MOV R11, #0       @ Initialize the counter for the binary digits
   LDR R6, =Set      @ Load the address of the binary buffer

loop_binary:
   MOV R10, #2       @ Set the divisor to 2
   UDIV R12, R9, R10 @ Divide the decimal number by 2, quotient in R12, remainder in R9
   MUL R8, R12, R10  @ Multiply the quotient by 2
   SUB R0, R9, R8    @ Subtract the product from the decimal number
   ADD R8, R0, #'0'  @ Convert the remainder to an ASCII digit

   STR R8, [R6, R11] @ Store the binary digit in the buffer
   MOV R9, R12       @ Move the quotient to R9 for the next division
   ADD R11, R11, #1  @ Increment the counter for the binary digits

   CMP R9,#0         @ Check if the quotient is zero
   BNE loop_binary   @ If not, continue to divide

   MOV R3, R11       @ Move the counter to R3 for Set_binary
   MOV R4, #0        @ Initialize the counter for Set_binary
   B Set_binary

Set_binary:
   LDR R0, =Show     @ Load the address of the output buffer
   LDR R1, =Set      @ Load the address of the binary buffer
   LDRB R5, [R1,R3]  @ Load the binary digit from the buffer
   STR R5, [R0, R4]  @ Store the binary digit in the output buffer

   CMP R3, #0        @ Check if all binary digits have been stored
   ADD R4, R4, #1    @ Increment the counter for the output buffer
   SUB R3, R3, #1    @ Decrement the counter for the binary digits
   BNE Set_binary    @ If not, continue to store binary digits

   SWI 0             @ Invoke kernel to write the binary number to stdout

_show:
   MOV R7, #4        @ Request to write to file
   MOV R0, #2        @ File descriptor of output, stdout
   MOV R2, #9        @ Number of bytes to write, i.e., nine bytes
   LDR R1, =Show     @ Address of buffer to write data from
   SWI 0            @ Invoke kernel to write to file

_exit:
   MOV R7, #1       @ Request to exit
   SWI 0            @ Invoke kernel to exit

    .data
Lab4: .ascii " "    @ Buffer to read two decimal digits into
Set: .ascii "0000000\n \n"  @ Buffer to store the binary digits into
Show: .ascii "0000000\n \n" @ Buffer to write the binary digits from

    .end