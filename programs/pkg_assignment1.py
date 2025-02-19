'''
Write a script that lists all files and directories in the current working directory line by line.
###################################################################################################
Create a new directory called "test_directory". After creating it, remove the directory.
###################################################################################################
write a script to create 10 directories in the current directory as below.

dir1
dir2
dir3
dir4
..
..
dir10
###################################################################################################

'''

import os
# print("Current directory is: ",os.getcwd())

# print("Contents of current dir:")
# print("---------------------------")
# files_dir = os.listdir()
# for item in files_dir:
#     print(item)


# dir_name = "test_directory"
# os.mkdir(dir_name)

# if os.path.exists("test_directory"):
#     print(f"directory {dir_name} exists")
#     os.removedirs("test_directory")
#     print(f"{dir_name} is removed")
# else:
#     print(f"{dir_name} is not exists")

dir_names = "dir{}"
for i in range(1,11):
    dir_name = f"dir,{i}"
    # os.mkdir(dir_name)
    os.removedirs(dir_name)

print(os.listdir())
