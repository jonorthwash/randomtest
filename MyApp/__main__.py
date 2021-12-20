#!/usr/bin/env python3

from . import modules
from . import util

def main():
	print("testing modules")
	modules.base.Base()
	print("testing util")
	util.tools.Tool()

if __name__ =='__main__':
	main()
