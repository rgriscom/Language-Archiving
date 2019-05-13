# Script author: Richard Griscom (rgriscom@uoregon.edu), February 2019
# Script description: This script is designed for users who are depositing data with the Endangered Languages Archive (ELAR) and need to create topic and keyword fields for their IMDI files. It makes new copies of all of the IMDI files in the same folder as the script, puts them in a new folder called 'Output,' and adds six empty Key fields to each file: one called "Topic", and five called "Keyword". You can then easily fill the fields with metadata using software such as Arbil. After completing your metadata, you can use another script to remove any remaining empty "Keyword" fields. 


import os, platform, shutil
#Determine which OS is being used
if platform.system() == 'Windows':
    system_var = 'w'
    print('OS is Windows')
else:
    system_var = 'nw'
        

# Determines the input directiony and creates the output directory
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
if "Output" in dir_list:
    try:
        shutil.rmtree(output_dir)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
os.mkdir(output_dir)

#For each .IMDI file in the same location as the script, it inserts the topic and keyword fields (called "keys") in the "<Content>" section of the file.
for d in dir_list:
    if ".imdi" in d:
        oldname = input_dir + d
        newname = output_dir + d
        with open(oldname) as f_old, open(newname, "w") as f_new:
            check = 0
            for line in f_old:
                if "<Content>" in line:
                    check = 1
                if "</Content>" in line:
                    check = 2
                if check == 1 and "<Keys/>" in line:
                    f_new.write('\t<Keys>\n\t\t<Key Name=\"Topic\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t\t<Key Name=\"Keyword\"></Key>\n\t</Keys>\n')
                else:
                    f_new.write(line)
                    
            print('Completed processing of: ' + d)
 
                    
