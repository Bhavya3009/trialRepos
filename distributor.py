import os
from getpass import getpass
from dotenv import load_dotenv

load_dotenv()

password = os.environ.get("pass")
key = getpass("Enter password: ")

if(password == key):
    current_dirct = os.getcwd()
    new_folder = os.path.join(current_dirct,"myfolder")
    for root,dirct,files in os.walk(current_dirct):
            for file_name in files:
                if(file_name == ".env" or file_name == "practice.py" or file_name ==     "usingdict.py"):
                    continue
                src = os.path.join(root,file_name)
                os.rename(src,os.path.join(new_folder,file_name))
             
    for root,dirct,files in os.walk(current_dirct):
           for folders in dirct:
                 if(folders != "myfolder"):
                      os.removedirs(folders)

else:
     print("Wrong password")
     exit()