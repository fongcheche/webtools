// patch int3(0xcc) to nop(0x90)

baseAddr = '0x400000'
int_baseAddr = int(baseAddr,16)

buf = open('./xx_warmup_obf','rb').read()
dec_buf = []
for c in buf:
    dec_buf.append(ord(c))

// objdump -M intel -d xx_warmup_obf.path  | grep "int3" > int3addr.txt
with open('./int3addr.txt', 'r') as f:
    for line in f:
        line_addr = line.split(':')[0][2:]
        int_addr = int(line_addr,16)
        rela_addr = int_addr - int_baseAddr
        if dec_buf[rela_addr] == 0xcc:
            dec_buf[rela_addr] = 0x90

m = ''
for i in dec_buf:
    m+=chr(i)

open('xx_warmup_obf.patch','wb').write(m)
            


