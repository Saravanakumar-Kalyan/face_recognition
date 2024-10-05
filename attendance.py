import csv
import datetime

# creating the csv file if it doesn't exits
try:
    with open("attendance/file.csv") as f:
        pass
except:
    with open("attendance/file.csv", mode="w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["name"])
        writer.writerow(['saravana'])
        writer.writerow(['akhil'])
        writer.writerow(['amandeep'])

def takeAttendance(names):
    with open("attendance/file.csv", mode='r') as f:
        read = csv.reader(f)
        read = list(read)
        field_names = read[0]
        read = read[1:]
        d = datetime.datetime.today()
        d = d.strftime("%d-%m-%Y %H:%M:%S")
        if not field_names[-1] == d:
            field_names.append(d)
            for line in read:
                if line[0] in names:
                    line.append(str(1))
                else:
                    line.append(str(0))
        else:
            for line in read:
                if line[0] in names:
                    line[-1] = str(1)
                    

    with open("attendance/file.csv",mode='w') as f:
        write = csv.writer(f,lineterminator='\n')
        write.writerow(field_names)
        write.writerows(read)
