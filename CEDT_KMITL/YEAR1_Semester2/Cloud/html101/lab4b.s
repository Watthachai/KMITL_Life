.global _start

_start:
       
_read:
        mov R7 , #3 @รับค่า
        mov r0 , #0 @รับค่าจาก stdin
        mov r2 , #20 @ขนาด ของตัวอักษร
        ldr r1, =instr1 @ที่อยู่ของตัวอักษร
        swi 0 

        

        mov R7 , #3 @รับค่า
        mov r0 , #0 @รับค่าจาก stdin
        mov r2 , #20  @ขนาด ของตัวอักษร
        ldr r1, =instr2 @ที่อยู่ของตัวอักษร
        swi 0

        ldr r1,=instr1 @เอาค่าที่อยู่ของตัวอักษรมาเก็บไว้ใน r1
        ldr r2,=instr2 @เอาค่าที่อยู่ของตัวอักษรมาเก็บไว้ใน r2

        mov r3,#0 


for_one:
        ldrb r4, [r1, r3] @เอาค่าตัวอักษรมาเก็บไว้ใน r4
        cmp r4 ,#10 @เช็คว่าเป็นตัวอักษรหรือไม่
        add r3 ,r3,#1 @เพิ่มค่า r3
        bne for_one @ถ้าไม่ใช่ตัวอักษรก็ข้ามไป

        mov r5, #0 @เอาไว้เก็บค่า r3


for_two: 
        ldrb r4 , [r2,r5] @เอาค่าตัวอักษรมาเก็บไว้ใน r4
        cmp r4 ,#10 @เช็คว่าเป็นตัวอักษรหรือไม่
        add  r5,r5 ,#1 @เพิ่มค่า r5
        bne for_two @ถ้าไม่ใช่ตัวอักษรก็ข้ามไป
        


        mov r4 , #0 @เอาไว้เก็บค่า r5
        mov r6 , #0 @เอาไว้เก็บค่า r7

        sub r3 ,r3 ,#1 @ลดค่า r3
        sub r5 ,r5 ,#1 @ลดค่า r5

range: 
        cmp r4 ,r3 @เช็คว่า r4 มากกว่า r3 หรือไม่
        add r4,r4 ,#1 @เพิ่มค่า r4
        mov r6 ,#0 @เอาไว้เก็บค่า r7
        mov r7 ,#0  @เอาไว้เก็บค่า r6
        
        blt _loop  @ถ้า r4 น้อยกว่า r3 ก็ข้ามไป
        b ans_no @ถ้า r4 มากกว่า r3 ก็ไปที่ ans_no
        

_loop:
        cmp r7 ,r3 @เช็คว่า r7 มากกว่า r3 หรือไม่
        blt compare_check @ถ้า r7 น้อยกว่า r3 ก็ข้ามไป
        b range @ถ้า r7 มากกว่า r3 ก็ไปที่ range

compare_check:

        ldrb r8, [r1 , r7] @เอาค่าตัวอักษรมาเก็บไว้ใน r8
        ldrb r9 ,[r2 , r6] @เอาค่าตัวอักษรมาเก็บไว้ใน r9

        add r7 ,r7 , #1 @เพิ่มค่า r7

        cmp r8 ,r9 @เช็คว่า r8 เท่ากันหรือไม้ r9 หรือไม่
        bne set_s @ถ้า r8 น้อยกว่า r9 ก็ไปที่ set_s
        add r6 ,r6, #1 @เพิ่มค่า r6

        cmp  r6,r5 @เช็คว่า r6 มากกว่า r5 หรือไม่
        bne _loop @ถ้า r6 น้อยกว่า r5 ก็ไปที่ _loop
        b ans_yes @ถ้า r6 มากกว่า r5 ก็ไปที่ ans_yes

set_s:
        mov r6,#0 @เอาไว้เก็บค่า r7
        b _loop @ไปที่ _loop


ans_yes:
        mov r7 ,#4 @รับค่า
        mov r0 ,#1 @รับค่าจาก stdin
        mov r2 ,#4 @ขนาด ของตัวอักษร
        ldr r1,=res_yes @ที่อยู่ของตัวอักษร
        swi 0 
        b _exit @ไปที่ _exit

ans_no:
        mov r7 ,#4 @รับค่า
        mov r0 ,#1 @รับค่าจาก stdin
        mov r2 ,#4 @ขนาด ของตัวอักษร
        ldr r1,=res_no @ที่อยู่ของตัวอักษร
        swi 0 
        b _exit @ไปที่ _exit

_exit: 
        mov r0 , r10 @เอาค่า r10 มาเก็บไว้ใน r0
        mov r7 , #1 @รับค่า
        swi 0 




.data

instr1: .asciz "                "
instr2: .asciz "                "

res_yes : .ascii "Yes\n"
res_no : .ascii "No\n"