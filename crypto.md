```
def solve_quadratic(a, b, c):
    # Calculate the discriminant

    discriminant = b**2 - 4*a*c    
    # Check if the discriminant is negative (no real roots)

    if discriminant < 0:
        return None, None

    # Calculate the square root of the discriminant
    sqrt_discriminant = nroot(discriminant,2)
    
    # Calculate the roots
    root1 = (-b + sqrt_discriminant) // (2*a)
    root2 = (-b - sqrt_discriminant) // (2*a)
    
    return root1, root2
```

```
def dlog(g, x, p):
    return int(pari(f"znlog({int((x)%p)},Mod({g},{int(p)}))"))
```


```
def solve_transformation(known_tmp_arr):
        plaintext = [BitVec(f'plaintext_{i}', 8) for i in range(8)]
        s1 = Solver()
        tmp_arr = [BitVec(f'tmp_arr_{j}', 8) for j in range(8)]
        for i in range(8):
            for j in range(8):
                byte_val = (plaintext[i] ^ xbox[(i * 8) + j]) >> tbox[i][j]
                byte_val = Extract(0, 0, byte_val)
                s1.add(Extract(7-i, 7-i, tmp_arr[j]) == byte_val)
        for j in range(8):
            s1.add(tmp_arr[j] == known_tmp_arr[j])
        if s1.check() == sat:
            model = s1.model()
            plaintext_values = bytearray([model[plaintext[i]].as_long() for i in range(8)])
            return plaintext_values
```


```
P.<x> = PolynomialRing(Zmod(n))
equation = persamaan
```


- https://crypto.stackexchange.com/questions/100766/how-to-break-rsa-when-q-e-1-bmod-p
- https://crypto.stackexchange.com/questions/103615/in-rsa-how-to-calculate-the-private-exponent-d-after-choosing-e
- https://stackoverflow.com/questions/16531958/rsa-algorithm-known-n-how-to-get-p-q
- https://github.com/Adamkadaban
- https://medium.com/@muhammadnafiz2017/write-up-cryptography-and-pwn-challenges-on-wargames-my-2023-capture-the-flag-ea1b890b070b
- https://zakigeyan.github.io/
- https://github.com/jvdsn/crypto-attacks
- https://book.jorianwoltjer.com/cryptography/pseudo-random-number-generators-prng
- https://exploit-notes.hdks.org/exploit/cryptography/algorithm/aes-ecb-padding-attack/
- https://github.com/isislovecruft/library--/tree/master/cryptography%20%26%20mathematics
- https://github.com/pberba/ctf-solutions/blob/master/20180913_sect/matryoskal/README.md
- https://github.com/Lyutoon/cryptography
- https://github.com/ashutosh1206/Crypton/
- https://github.com/Merricx
- https://github.com/nakov/Practical-Cryptography-for-Developers-Book
- https://merri.cx/adventure-of-aes/
