import csv
#https://www.youtube.com/watch?v=q5uM4VKywbA
with open('bizimdosya.csv','r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)
    #next(csv_reader) #başlığı alma

    for line in csv_reader:
        print(line)

    # with open("yeni_dosya.csv",'w') as new_file:
    #     csv_writer = csv.writer(new_file,delimiter='\t')
    #
    #     for line in csv_reader:
    #         csv_writer.writerow(line)
        #print(line[1])
