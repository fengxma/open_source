import csv

potholes_by_zip = {}

f = open('potholes.csv', 'r')
for row in csv.DictReader(f):
    status = row['STATUS']
    zipcode = row['ZIP']
    if status == 'Open':
        if zipcode not in potholes_by_zip:
            potholes_by_zip[zipcode] = 1
        else:
            potholes_by_zip[zipcode] += 1

print('Number of open potholes by zipcode')
for zc in sorted(potholes_by_zip):
    print('%8s %d' % (zc, potholes_by_zip[zc]))
