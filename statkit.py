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
					if stat.has_key('id'):
						stats.append(stat)
					stat = {'op1': "", 'op2': "", 'op1_mode': "", 'op2_mode': "",}
					stat['id'] = line[0:16]
					instrList = line[17:60].split()
					addrList = line[60:-1].split()
					stat['instr'] = instrList[0]
					stat['nOPs'] = len(instrList) - 1
					if len(instrList) == 2:
						stat['op1'] = instrList[1]
					elif len(instrList) == 3:
						stat['op1'] = instrList[1][0:-2]
						stat['op2'] = instrList[2]
					stat['naddr'] = len(addrList)
					for i in range(0, len(addrList)):
						stat['addr'+str(i)] = addrList[i]
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
			if not stat.has_key('naddr'):
				print stat
			tlen = stat['naddr']
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
			for i in range(0, stat[nOPs]):
				mode = Addressing.checkMode(stat['op'+str(i+1)])
				stat['op'+str(i+1)+'_mode'] = mode
				modeDict[mode] += 1
		Toolkit.showProportion(modeDict, picName, picTitle)
		if len(fmode) > 0:
			Toolkit.writeJsonFile(fmode, modeDict)
		return modeDict
	
	@statimethod
	def statAndShowImmediateLength(stats, fimmediate="", picName="", picTitle=""):
		lenDict = {}
		for stat in stats:
			for i in range(0, stat[nOPs]):
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
