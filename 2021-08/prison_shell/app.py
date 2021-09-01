#!/usr/bin/python3
import subprocess

whitelist = "prim@cult ."

error = "tinyurl.com/ictf-flag"

def sh(cmd):
	for word in cmd.split(" "):
		if not ((word.startswith("-") and word.replace("-", "").isalnum()) or all(char.lower() in whitelist for char in word)):
			return error

	data = dict(zip(["stdout", "stderr"], [_.decode() for _ in subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()]))

	out = [data[i] for i in data if data[i]]
	return '\n'.join(out)


while True:
	cmd = input("agent@[REDACTED]:~$ ")
	if cmd in ["exit", "quit"]:
		break
	print(sh(cmd))
