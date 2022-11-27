# Easy Peasy
one-time pad
## Solution
force a second pass in which the flag will be encrypted twice  
the server uses XOR encryption: in the second pass the flag will decrypted
enc = encrypted Flag
```
flag ^ key = enc                    # first pass
enc ^ key = flag ^ key ^ key = flag # second pass
```
##  Encrypted Flag
the servers gives us the Flag, encrypted used the first bytes of the key
```bash
nc mercury.picoctf.net 41934
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d
```
we'll need this in raw form
```bash
echo -n '0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d' | \
  xxd -p -r > encrypted_flag.raw
xxd encrypted_flag.raw
00000000: 0345 376e 1e54 0669 1d5c 076c 4050 046e  .E7n.T.i.\.l@P.n
00000010: 4000 036a 1a00 5c6b 1904 531d 3941 055d  @..j..\k..S.9A.]
```
### Flag length
```python
len('0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d')
# 64
```
## forcing a second pass
we need a file with `KEY_LEN` - `FLAG_LEN` data to encrypt in order to exaust the
key and force a send pass  
this should be followed by the encrypted key (second pass)
### Key length
from _otp.py_: `KEY_LEN = 50000`
### file generation
```bash
dd if=/dev/zero bs=1 count=$((50000-32)) of=exaust_first_pass.raw
echo "" > /tmp/newline
cat exaust_first_pass.raw /tmp/newline \
  encrypted_flag.raw /tmp/newline \
      > second_pass.raw
```
...or using vi `:set binary` and `:r ++bin key.raw`
## obtaining the Flag
```bash
nc mercury.picoctf.net 41934 < second_pass.raw

******************Welcome to our OTP implementation!******************
This is the encrypted flag!
0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d

What data would you like to encrypt? Here ya go!
5c7864315c7839 ...and alot more... 5322b3a255c7865325c7830345c78

What data would you like to encrypt? Here ya go!
6162663266376435656466303832303238303736626664376134636665396139

What data would you like to encrypt?
```

### deconding
```python
flag = '6162663266376435656466303832303238303736626664376134636665396139'
print(bytes.fromhex(flag))
# b'abf2f7d5edf082028076bfd7a4cfe9a9'
```
which gives us the flag `abf2f7d5edf082028076bfd7a4cfe9a9`, wrapped in the picoCTF format:  
**picoCTF{abf2f7d5edf082028076bfd7a4cfe9a9}**

