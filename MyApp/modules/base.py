from .. import util

class Base():
	def __init__(self):
		print("running module")
		print("running util.tools.Tool from within module")
		util.tools.Tool()
