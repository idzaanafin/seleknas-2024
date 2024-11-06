import pwn
from Crypto.Cipher import AES
BLOCK_SIZE = 16

io = pwn.process("python3 binus.py", shell=True)
io.recv()
io.recvuntil(b': ')
data = bytes.fromhex(io.recvuntil(b'\n').strip().decode())
print(data)

def is_padding_ok(cipher):
        io.sendline(b'1')
        #io.recv()
        io.sendline(cipher.hex())
        io.recvuntil(b': ')
        data = io.recvuntil(b'\n').strip()
        if data == b'Something went wrong':
                return False
        else:
                return True
        #io.interactive()
#print(is_padding_ok(data))

def attack( ciphertext ):
        guessed_clear = b''

        split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
        blocks = split_string( ciphertext, BLOCK_SIZE )

        for block_n in range( len( blocks ) - 1, 0, -1 ): #build pair of blocks starting from end of message
                spliced_ciphertext = blocks[block_n - 1] + blocks[block_n]

                decoded_bytes = b'?' * BLOCK_SIZE #output of block cipher decoding values

                ##GET VALUE OF SECRET BYTE byte
                for byte in range( BLOCK_SIZE - 1, -1, -1 ):
                        new_pad_len = BLOCK_SIZE - byte

                        #Build hacked ciphertext tail with values to obtain desired padding
                        hacked_ciphertext_tail = b''
                        for padder_index in range( 1, new_pad_len ):
                                hacked_ciphertext_tail += bytearray.fromhex('{:02x}'.format( new_pad_len ^ decoded_bytes[byte + padder_index] ) )

                        for i in range( 0, 256 ):
                                attack_str = bytearray.fromhex( '{:02x}'.format( ( i ^ spliced_ciphertext[byte] ) ) )
                                hacked_ciphertext = spliced_ciphertext[:byte] + attack_str + hacked_ciphertext_tail + spliced_ciphertext[byte + 1 + new_pad_len - 1:]

                                if( is_padding_ok( hacked_ciphertext ) ):

                                        test_correctness = hacked_ciphertext[:byte - 1] + bytearray.fromhex( '{:02x}'.format( ( 1 ^  hacked_ciphertext[byte] ) ) )  + hacked_ciphertext[byte:]
                                        if( not is_padding_ok( test_correctness ) ):
                                                continue

                                        decoded_bytes = decoded_bytes[:byte] + bytearray.fromhex('{:02x}'.format( hacked_ciphertext[byte] ^ new_pad_len ) ) + decoded_bytes[byte + 1:]
                                        guessed_clear = bytearray.fromhex('{:02x}'.format( i ^ new_pad_len ) ) + guessed_clear
                                        break

        return guessed_clear[:-guessed_clear[-1]] #remove padding!

#print(attack(bytes.fromhex('71776572747975696f7061736466676863d8ac79783a5473c14a988a6cb77276633e4dedc34f00a4c8f1b424da386d1f')))
#print(attack(bytes.fromhex('704a6b47e4de5b929bb24bda24c2de05254a1236e7fe46a87e15d0203637bc7385c4cc2c46feb6b09f781666bb097bea')))
print(attack(data))
