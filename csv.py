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
        # print(json.dumps(create_list))
        print(json.dumps({'user_id': create_list[0], 'username': create_list[1],
            'email' : create_list[2], 'level_of_authorization' : create_list[3],
            'date_of_birth' : create_list[4]
            }, sort_keys=True, indent=4))
        

