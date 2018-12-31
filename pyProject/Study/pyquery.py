#csv
import csv
with open('data.csv','w') as csvfile:
    write = csv.writer(csvfile)
    write.writerow(['id','name','age'])
    write.writerow(['10001', 'zs', '12'])
    write.writerow(['10002', 'ls', '13'])
    write.writerow(['10003', 'ww', '14'])