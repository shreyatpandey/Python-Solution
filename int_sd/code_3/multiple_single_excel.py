import os
import glob
import csv
import xlwt

wb = xlwt.Workbook()
for csvfile in glob.glob(os.path.join('.', '*.csv')):
    print("csvfile:",csvfile)
    fpath = csvfile.split("\\", 1)
    print("fpath:",fpath)
    #fname = fpath[1].split(".", 1) ## fname[0] should be our worksheet name

    ws = wb.add_sheet(fpath[1])
    with open(csvfile, 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                ws.write(r, c, col)
    wb.save('output.xls')
    os.remove(csvfile)
