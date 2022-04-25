from pwn import *

judge = process(['python3', './test.py'])
me = process(['python3', './c.py'])
#context.log_level = 'debug'

for _ in range(350):
    msg = judge.recvline()
    me.send(msg)
    if msg == b'0\n': break
    reply = me.recvline()
    judge.send(reply)
print("done in {} rounds".format(_))
