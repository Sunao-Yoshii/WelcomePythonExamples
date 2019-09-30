#!/usr/local/bin/python3
import subprocess

res = subprocess.check_output(
    "ls | grep si",
    shell=True,
    stderr=subprocess.STDOUT)

print(res.decode())