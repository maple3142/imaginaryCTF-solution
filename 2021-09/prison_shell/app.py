#!/usr/bin/env python3
import subprocess

fullflag = open("flag.txt").read().strip()

partial_flags = [
	fullflag[:13],
	fullflag[13:39],
	fullflag[39:60],
	fullflag[60:64],
	fullflag[64:],
]

error = "jctf{f4k3_f1@g}"

def sh(cmd):
	if len(cmd) != 50 or "cat" in cmd or not all(c.isalpha() or c == " " for c in cmd):
		return error

	data = dict(zip(["stdout", "stderr"], [_.decode() for _ in subprocess.Popen(cmd + " flag.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()]))

	if "ictf" in data["stdout"] or "ftci" in data["stdout"]:
		i = len(cmd.split(" ")[0])
		if i in range(2, 7) and cmd.count(" ") in range(1, 3):
			return partial_flags[i - 2]
		return error

	out = [data[i] for i in data if data[i]]
	return '\n'.join(out)


while True:
	cmd = input("hacker@ictf:~$ ")
	if cmd in ["exit", "quit"]:
		break
	print(sh(cmd))
