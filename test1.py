import csv

errorList = dir(locals()['__builtins__'])

filteredList = []

def filterAll(errorList):
	for substring in errorList:
		if 'Error' in substring:
			filteredList.append(substring)
	return filteredList

csv_data = open('filteredError.csv',mode='w',newline='')
csv_writer = csv.writer(csv_data,delimiter='\t')
csv_writer = csv_writer.writerows(filterAll(errorList))
csv_data.close()

