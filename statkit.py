# -*- coding:UTF-8 -*-
import sys
from toolkit import Toolkit
from addressing import Addressing
reload(sys)
sys.setdefaultencoding('utf-8')

class Statkit():
	@staticmethod
	def genListFromTrace(ftrace, fdict=""):
		stats = []; stat = {}; count = 0
		with open(ftrace) as f:
			for line in f:
				if "--" in line:
					""" to process the additional information """
					if "addr" in line:
						stat['addr'] = line.split()[2]

					elif "not taken" in line:
						stat['taken'] = 0
					elif "taken" in line:
						stat['taken'] = 1

					elif "not executed" in line:
						stat['executed'] = 0
					elif "executed" in line:
						stat['executed'] = 1

					else:
						print "Error:", line

				else:
					""" else, it's the begin for a new instruction """
					if stat.has_key('id'):
						stats.append(stat)
					stat = {'lock': 0, 'rep': 0, 'op1': "", 'op2': "", 'op3': "", 'op1_mode': "", 'op2_mode': "", 'op3_mode': ""}

					""" split the string line into 3 parts """
					stat['id'] = line[0:16]
					instrList = line[17:60].split()
					addrList = line[60:-1].split()

					""" for the instruction part """
					if instrList[0] == "lock":
						stat['lock'] = 1
					if instrList[0] == "rep":
						stat['rep'] = 1
					""" Any Other Prefix? REPE, REPNE, REPZ, REPNZ ??? """
					stat['instr'] = instrList[0+stat['lock']+stat['rep']]
					stat['nOPs'] = len(instrList) - 1 - stat['lock'] - stat['rep']
					if stat['nOPs'] == 1:
						stat['op1'] = instrList[1+stat['lock']+stat['rep']]
					elif stat['nOPs'] == 2:
						stat['op1'] = instrList[1+stat['lock']+stat['rep']][0:-1]
						stat['op2'] = instrList[2+stat['lock']+stat['rep']]
					elif stat['nOPs'] == 3:
						stat['op1'] = instrList[1+stat['lock']+stat['rep']][0:-1]
						stat['op2'] = instrList[2+stat['lock']+stat['rep']][0:-1]
						stat['op3'] = instrList[3+stat['lock']+stat['rep']]
					elif stat['nOPs'] > 3:
						print line

					""" for the binary representation part"""
					stat['nbytes'] = len(addrList)
					for i in range(0, len(addrList)):
						stat['byte'+str(i)] = addrList[i]

			if stat.has_key('id'):
				stats.append(stat)
			f.close()
			
		if len(fdict) > 0:
			Toolkit.writeJsonFile(fdict, stats)
		return stats

	@staticmethod
	def statAndShowLength(stats, flength="", picName="", picTitle=""):
		lenDict = {}
		for stat in stats:
			if not stat.has_key('nbytes'):
				print stat
			tlen = stat['nbytes']
			if lenDict.has_key(tlen):
				lenDict[tlen] += 1
			else:
				lenDict[tlen] = 1
		Toolkit.showProportion(lenDict, picName, picTitle)
		if len(flength) > 0:
			Toolkit.writeJsonFile(flength, lenDict)
		return lenDict

	@staticmethod
	def statAndShowAddrMode(stats, fmode="", picName="", picTitle=""):
		modeDict = {}
		for stat in stats:
			for i in range(0, stat['nOPs']):
				mode = Addressing.checkMode(stat['op'+str(i+1)])
				stat['op'+str(i+1)+'_mode'] = mode
				modeDict[mode] += 1
		Toolkit.showProportion(modeDict, picName, picTitle)
		if len(fmode) > 0:
			Toolkit.writeJsonFile(fmode, modeDict)
		return modeDict
	
	@staticmethod
	def statAndShowImmediateLength(stats, fimmediate="", picName="", picTitle=""):
		lenDict = {}
		for stat in stats:
			for i in range(0, stat['nOPs']):
				op = 'op'+str(i+1)
				mode = stat[op+'_mode']
				if len(mode) <= 0:
					mode = Addressing.checkMode(stat[op])
					stat[op+'_mode'] = mode
				if mode == 1:
					length = Addressing.checkAddrLen(stat[op])
					if lenDict.has_key(length):
						lenDict[length] += 1
					else:
						lenDict[length] = 1
		Toolkit.showProportion(lenDict, picName, picTitle)
		if len(fimmediate) > 0:
			Toolkit.writeJsonFile(fimmediate, lenDict)
		return lenDict
