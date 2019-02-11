# Script author: Richard Griscom (rgriscom@uoregon.edu), February 2019
# Script description: This script is designed to remove any empty Keyword fields in IMDI files. It makes new copies of all of the IMDI files in same folder as the script, and puts them in a new folder ("Output"). 

import os, platform, shutil
if platform.system() == 'Windows':
    system_var = 'w'
    print('OS is Windows')
else:
    system_var = 'nw'
        

#!!!Input and output directories!!!
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

 
                    
