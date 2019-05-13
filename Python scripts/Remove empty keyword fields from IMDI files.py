# Script author: Richard Griscom (rgriscom@uoregon.edu), February 2019
# Script description: This script is designed for users who are depositing data with the Endangered Languages Archive (ELAR) and have already created topic and keyword fields and finished filling as many keyword fields as they would like to fill. This script will remove any empty keyword fields in IMDI files (labeled "<Key>" in the XML format of the file). It makes new copies of all of the IMDI files in same folder as the script, and puts them in a new folder ("Output"). 

import os, platform, shutil
#Determine the operating system
if platform.system() == 'Windows':
    system_var = 'w'
    print('OS is Windows')
else:
    system_var = 'nw'
        

#Determine the input directory and create the output directory
if system_var == 'w':
    input_dir = os.getcwd() + "\\"
    output_dir = os.getcwd() + "\\Output\\"
    print('Input dir: ' + input_dir)
    print('Output dir: ' + output_dir) 
else:
	input_dir = os.getcwd() + "/"
	output_dir = os.getcwd() + "/Output/"
	print('Input dir: ' + input_dir)
	print('Output dir: ' + output_dir)

#For each .IMDI file in the same folder as the script, remove any empty keyword lines.
dir_list = os.listdir(input_dir)
for d in dir_list:
    if ".imdi" in d:
        oldname = input_dir + d
        newname = output_dir + d
        with open(oldname) as f_old, open(newname, "w") as f_new:
           
            for line in f_old:
                if  "<Key Name=\"Keyword\"/>" in line:
                    check = 0
                else:
                    f_new.write(line)
            print(d)

 
                    
