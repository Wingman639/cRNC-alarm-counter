# -*- coding: utf-8 -*-
import re

SOURCE_FILE_NAME = 'alarm_log.txt'
REPORT_FILE_NAME = 'count_report.txt'


def alarmTextListWithText(text):
	return text.split(') IPA2800          ')

def alarmNumFromText(text):
	iAlarm = text.find(' ALARM ')
	if iAlarm < 1: 
		return None
	alarmStr = text[iAlarm: iAlarm + 130]
	iAlarmNumPrefix = alarmStr.find('\n    ')
	alarmNumStr = alarmStr[iAlarmNumPrefix+5: iAlarmNumPrefix + 10]
	return alarmNumStr

def alarmNumReSearchFromText(text):
	patternStr = r' ALARM .*? ([0-9]+)'
	pattern = re.compile(patternStr, re.S)
	match = pattern.search(text)
	if match:
		return match.group(1)

def collectAlarms(alarmTextList):
	alarms = {}
	for alarmText in alarmTextList:
		alarmNum =  alarmNumReSearchFromText(alarmText) #alarmNumFromText(alarmText)
		if alarmNum is None:
			continue
		
		if alarmNum in alarms:
			alarms[alarmNum] += 1
		else:
			alarms[alarmNum] = 1
	return alarms


def readTextFile(fileName):
	f = open(fileName, 'r')
	text = f.read()
	f.close()
	return text

def writeReport(text):
	f = open(REPORT_FILE_NAME, 'w')
	f.write(text)
	f.close()

def dictToStr(dict):
	text = ''
	for key, value in dict.iteritems():
		text += '\n' + str(key) + ' : ' + str(value)
	return text


def counting(text):
	alarmTextList = alarmTextListWithText(text)
	alarms = collectAlarms(alarmTextList)
	print alarms
	report = dictToStr(alarms)
	return report

def main():
	text = readTextFile(SOURCE_FILE_NAME)
	report = counting(text)
	writeReport(report)

if __name__ == '__main__':
	main()