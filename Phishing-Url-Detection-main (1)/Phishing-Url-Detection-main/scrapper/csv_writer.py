import csv
def writer(row):
    f= open('beningn.csv','a',newline="",encoding='utf-8-sig')
    writer = csv.writer(f)
    writer.writerow(row)
