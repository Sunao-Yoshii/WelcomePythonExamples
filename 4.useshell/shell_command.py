#!/usr/local/bin/python3
import subprocess
proc = subprocess.run(["ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(proc.stdout.decode("utf8"))
