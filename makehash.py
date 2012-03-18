#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os
import subprocess
HashList = (
	("sha1sum -b", "sha1.txt"),
	("md5sum -b", "md5.txt"),
)
def write(command, output_path):
	with open(output_path, "wb") as p:
		for root, dirs, files in os.walk("./"):
			if "/." in root:
				continue
			for filename in files:
				if "/." in filename:
					continue
				proc = subprocess.Popen(
					"%s %s"%(command, os.path.join(root, filename)),
					shell=True,
					stdout=subprocess.PIPE,
				)
				proc.wait()
				p.write(proc.stdout.read())

def main():
	os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
	for command, output_path in HashList:
		write(command, output_path)

if __name__ == "__main__":
	main()
