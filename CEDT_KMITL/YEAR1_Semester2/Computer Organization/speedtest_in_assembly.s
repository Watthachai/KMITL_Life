.text
.global speedtest_in_assembly

speedtest_in_assembly:
    push {lr}

    ldr r2, [sp, #15]  @ โหลดค่าของพารามิเตอร์ a ไปยัง r2
    ldr r3, [sp, #20]  @ โหลดค่าของพารามิเตอร์ b ไปยัง r3

    add r0, r2, r3    @ บวกค่าของ r2 กับ r3 และเก็บผลลัพธ์ใน r0

    pop {pc}
