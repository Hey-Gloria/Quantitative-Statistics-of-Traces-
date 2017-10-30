# -*- coding:UTF-8 -*-
import sys, re
reload(sys)
sys.setdefaultencoding('utf-8')

class Addressing():
	@staticmethod
	def checkMode(op):
		""" 
			ModeCode	Description
			   1		Immediate
			   2		Register
			   3		Displacement (absolute/static address)
			   4		Base
			   5		Base + Displacement -- Can this Displacement be None?
			   6		(Index * Scale) + Displacement
			   7		Base + Index + Displacement
			   8		Base + (Index * Scale) + Displacement
		"""
		if re.match(r'\$0x\w+$', op, re.I):
			return 1
		elif re.match(r'%\w+$', op, re.I):
			return 2
		elif re.match(r'0x\w+$', op, re.I):
			return 3
		elif re.match(r'\(%\w+\)$', op, re.I):
			return 4
		elif re.match(r'-?0x\w+\(%\w+\)$', op, re.I):
			return 5
		elif re.match(r'(-?0x\w+)?\(,%\w+,\w+\)$', op, re.I):
			return 6
		elif re.match(r'(-?0x\w+)?\(%\w+,%\w+\)$', op, re.I):
			return 7
		elif re.match(r'(-?0x\w+)?\(%\w+,%\w+,\w+\)$', op, re.I):
			return 8
		return
	
	@staticmethod
	def checkAddrLen(op):
		return
