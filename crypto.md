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
m = 1337
x = 123456789
p=254054958823884061261040682676038626423
q=226266850984917201238064347151994984571
# p = getPrime(128)
# q = getPrime(128)
n = p*q
c1 = m*(x**14) % n
c2 = m*(x**22) % n

_x = (inverse(c1, n) * c2) % n
assert x**8 == _x

leaked_x = gmpy2.iroot(_x, 8)[0]
leaked_m = (inverse(leaked_x**14, n) * c1) % n
assert leaked_x == x
assert leaked_m == m
```

```
P.<x> = PolynomialRing(Zmod(n))
equation = persamaan
```

```
from z3 import *
a1 = [BitVec(f'a1_{i}', 8) for i in range(66)]
s = Solver()

for i in range(66-2):
     if i%3 == 0:
            v4 = a1[i]
            if i > 62:
                v4 = a1[i + 1] + a1[i] + a1[i + 2]
                s.add(v4 == secrets[i])
     elif i%3 == 1:
            sum1 = a1[i] + a1[i - 1]
            sum2 = a1[i] + a1[i + 1]
            s.add(sum1 == secretf[i])
            s.add(sum2 == secrets[i])
     else:
            sum1 = a1[i - 1] + a1[i] + a1[i - 2]
            sum2 = a1[i + 1] + a1[i] + a1[i + 2]
            s.add(sum1 == secretf[i])
            s.add(sum2 == secrets[i])
if s.check() == sat:
            model = s.model()
            print(bytearray([model[a1[i]].as_long() for i in range(66)]))
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
- https://github.com/prajnapras19/some-kripto-tool
- https://github.com/keeganryan/flatter
