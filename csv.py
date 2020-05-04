# 9737452,johndoe27,rockstar_data@yahoo.com,id proofed,19540528
# 2941846,young4eva,eva47@aol.com,unconfirmed,19790129

# id,username,email,level of authorization,date of birth

import json
import csv 
# save the csv 
# open file 
with open('test.txt') as csv_file:
    # file_reader = csv.reader(csv_file)

    for each_line in csv_file: 
        create_list = each_line.split(",")
        
        print(create_list[0])


# convert csv file into a dictionary (json format)


# {
    
#     "id": 9737452,
#     "username":
# }

