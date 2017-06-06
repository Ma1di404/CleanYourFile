import os
def rename_file():
    # the program asked to give the path
    
    path = raw_input("Please enter path: ")
    
    # list the files in the dir

    file_list = os.listdir(path)
    saved_path = os.getcwd()
    print ("Current Working Dir is "+saved_path)
    os.chdir(path)

    # rename the files in this dir

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"123456789")) 
rename_file()

