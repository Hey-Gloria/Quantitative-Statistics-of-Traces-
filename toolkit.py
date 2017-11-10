# -*- coding:UTF-8 -*-
import sys, os, json
import numpy as np
import matplotlib.pyplot as plt 
reload(sys)
sys.setdefaultencoding('utf-8')

class Toolkit():
	@staticmethod
	# 把content写入Json文件filename, add表示是否追加
	def writeJsonFile(filename, content, add=False):
		ori = os.path.exists(filename)
		if ori and add:
			print "File %s has already existed, now add to the end..." % filename
			with open(filename, "r") as load_f:
				pre = json.load(load_f)
				load_f.close()
				pre.extend(content)
				content = pre
		with open(filename, "w") as dump_f:
			json.dump(content, dump_f)
			dump_f.close()
		return
	
	@staticmethod
	def readJsonFile(filename):
		with open(filename, "r") as load_f:
			return json.load(load_f)

	@staticmethod
	def showProportion(dataDict, picName="", picTitle=""):
		labels = dataDict.keys()
		counts = dataDict.values()
		plt.figure(1, figsize=(6,6))
		plt.pie(counts, labels=labels, autopct='%1.1f%%')
		plt.title(picTitle)
		plt.show()
		plt.close()
		return
	
	@staticmethod
	def showHistogram(dataDict, picName="", picTitle="", xlabel="", ylabel="", labelDict={}):
		labels = dataDict.keys()
		counts = dataDict.values()
		pct = []
		total = float(sum(counts))
		for i in range(0, len(labels)):
			key = labels[i]
			if labelDict.has_key(key):
				labels[i] = labelDict[key]
			pct.append(100 * counts[i] / total)
		idx = np.arange(len(counts))

		plt.figure(figsize=(10, 6))
		plt.barh(idx, counts, alpha=0.6)
		for x, y, z in zip(counts, idx, pct):
			plt.text(x+0.05, y-0.1, '%.3f%%' % z)
		plt.yticks(idx, labels)
		plt.grid(axis='x')
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(picTitle)
		plt.show()
		return
