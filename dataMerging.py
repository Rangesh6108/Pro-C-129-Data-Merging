import csv

data_1=[]
data_2=[]

with open("dwaft_stars.csv","r") as f:
    dataframe=csv.reader(f)
    for i in dataframe:
        data_1.append(i)

with open("brightest_stars.csv","r") as f:
    dataframe=csv.reader(f)
    for i in dataframe:
        data_2.append(i)

header_1=data_1[0]
planetdata_1=data_1[1:]

header_2=data_2[0]
planetdata_2=data_2[1:]

header=header_1+header_2
planetdata=[]

for i in planetdata_1:
    planetdata.append(i)

for i in planetdata_2:
    planetdata.append(i)

with open("final_output.csv","a+") as f:
    write=csv.writer(f)
    write.writerow(planetdata)
    write.writerows(header)