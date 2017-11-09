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
			   9		%fs:Displacement
			  10		%fs:Base
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
		elif re.match(r'%fs:0x\w+$', op, re.I):
			return 9
		elif re.match(r'%fs:\(%\w+\)$', op, re.I):
			return 10
		return
	
	@staticmethod
	def checkAddrLen(op, mode):
		if mode == 1:
			num = op[1:]
		elif mode == 3:
			num = op
		elif mode in [5, 6, 7, 8]:
			nums = re.findall(r'(0x\w+)\(', op, re.I);
			if len(nums) == 0:
				num = 0x0
			else:
				num = nums[0]
		else:
			return
		
		"""
			if num is a negative number, (ignore the sign bit)
			checkAddrLen for -num instead
		"""
		if len(num) == 18 and int(num[0:3], 16) >= 8:
			num = hex((int(num, 16) - 1) ^ (2**64 - 1))[:-1]

		"""
			the addrLen is in unit of "bits"
		"""
		addrLen = (len(num) - 3) * 4
		head = int(num[0:3], 16)
		if head >= 8:
			addrLen += 4
		elif head >= 4:
			addrLen += 3
		elif head >= 2:
			addrLen += 2
		elif head >= 1:
			addrLen += 1
		return addrLen
