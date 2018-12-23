# Script author: Richard Griscom (rgriscom@uoregon.edu), December 2018
# Script description: This script is designed to make it easier to enter multiple keys into IMDI files for the purpose of preparing metadata for deposit in the Endangered Languages Archive. It makes new copies of all of the IMDI files in the first specified folder ("FOLDER FOR ORIGINAL FILES"), puts them in a new folder ("FOLDER FOR NEW FILES"), and adds six empty Key fields to each file: one called "Topic", and five called "Keyword". In order to make this script work correctly, you need to replace "FOLDER FOR ORIGINAL FILES" (two instances) and "FOLDER FOR NEW FILES" (one instance) in the script below with the corresponding directories on your machine. After completing your metadata, you can use another script to remove any remaining empty "Keyword" fields. 


import os
dir_list = os.listdir('/FOLDER FOR ORIGINAL FILES/')
for d in dir_list:
    if ".imdi" in d:
        oldname = "/FOLDER FOR ORIGINAL FILES/" + d
        newname = "/FOLDER FOR NEW FILES/" + d
        with open(oldname) as f_old, open(newname, "w") as f_new:
            check = 0
            for line in f_old:
                if check == 1 and "Keys" in line:
                    check =0
                else:
                    f_new.write(line)
                    if "</Project>" in line:
                        f_new.write('\t<Keys>\n\t\t<Key Name=\"Topic\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t</Keys>\n')
                        check = 1
            print(d)
 
                    
