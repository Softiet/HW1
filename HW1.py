# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061216.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================


cropped = []
for i in data:
    if not(float(i['PRES']) == -999.0 or float(i['PRES']) == -99.0):
        cropped.append(i)


target = ["C0A880","C0F9A0","C0G640","C0R190","C0X260"]

def find_mean(target,list_dict):
    counts = 0
    acc = 0
    for i in list_dict:
        if i["station_id"] == target:
            counts = counts + 1
            acc = acc + float(i['PRES'])
    if counts == 0:
        return 'None'
    else:
        return acc/counts

answer = []
for i in target:
    answer.append([i,find_mean(i,cropped)])

print(answer)