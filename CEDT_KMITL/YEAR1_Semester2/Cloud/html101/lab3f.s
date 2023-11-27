    .global _start

_start:

        MOV    R7, #3 @system call 3 คือ read
        MOV    R0, #0 @file descriptor 0 คือ stdin
        MOV    R2, #5 @จำนวน byte ที่จะอ่าน
        LDR    R1, =info    @r1 จะเก็บค่า info
        SWI    0    @system call

        LDR     R2, =out @r2 จะเก็บค่า out
        MOV     R8, #0 @r8 จะเก็บค่า 0

loop:
        LDRB    R5,[R1, R8] @r5 โหลดค่าจาก info มาเก็บไว้ที่ r5
        ADD     R5, R5, #5 @r5 บวก 5
        STRB    R5, [R2, R8] @r5 จะเก็บค่าที่บวกไปแล้วไว้ที่ out

        ADD     R8, R8, #1 @r8 บวก 1
        LDRB     R6, =10 @r6 จะเก็บค่า \n
        STRB    R6, [R2, R8]  @r6 จะเก็บค่า \n ไว้ที่ out  
        ADD     R2, R2, #1 @r2 บวก 1

        CMP     R8, #5 @r8 จะเก็บค่า 5
        BEQ     write @ถ้า r8 เท่ากับ 5 จะไปที่ write
        b       loop   @ถ้าไม่เท่ากับ 5 จะไปที่ loop


write:
        MOV    R7, #4   @system call 4 คือ write
        MOV    R0, #1  @file descriptor 1 คือ stdout
        MOV    R2, #10  @จำนวน byte ที่จะเขียน
        LDR    R1, =out @r1 จะเก็บค่า out
        SWI     0 @system call



_exit:
        MOV    R7, #1   @system call 1 คือ exit
        SWI    0    @system call

  

        .data @ส่วนของข้อมูล

info:   .space 5 @จองพื้นที่ 5 byte
out:    .space 10 @จองพื้นที่ 10 byte