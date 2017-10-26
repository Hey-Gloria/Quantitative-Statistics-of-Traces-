# -*- coding:UTF-8 -*-
import sys, os, json
from toolkit import Toolkit
reload(sys)
sys.setdefaultencoding('utf-8')

class Statkit():
	@staticmethod
	def genListFromTrace(ftrace, fdict=""):
		stats = []
		preID = 0; stat = {}
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
					stat = {}
					parts = line.split()
					stat['id'] = parts[0]
					stat['instr'] = parts[1]
					stat['nOPs'] = 0; stat['naddr'] = 0
					n = len(parts)
					for i in range(2, n):
						if(len(parts[i]) > 2):
							parts[i] = parts[i].split(',')[0]
							stat['nOPs'] += 1
							index = "op"+str(stat['nOPs'])
							stat[index] = parts[i]
						else:
							stat['naddr'] += 1
							index = "addr"+str(stat['naddr'])
							stat[index] = parts[i]
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


