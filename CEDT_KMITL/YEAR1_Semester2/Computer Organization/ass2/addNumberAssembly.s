.text
.global addNumbersAssembly

addNumbersAssembly:
    push {lr}

    ldr r2, [sp, #15] 
    ldr r3, [sp, #20]  

    add r0, r2, r3    

    pop {pc}