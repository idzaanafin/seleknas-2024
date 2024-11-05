```
from pwn import *

context.binary = elf = ELF('./chall')

if args.REMOTE:
    p = remote('chall.selekda.idcyberskills.com', 11101)
else:
    p = elf.process()
    p = process(['python3', ''])

p.interactive()
```
