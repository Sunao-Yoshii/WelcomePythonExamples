#!/usr/local/bin/python3
import subprocess

p1 = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "py"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()

result = p2.communicate()[0]
print(result.decode())
