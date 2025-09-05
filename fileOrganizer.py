import os
from dotenv import load_dotenv
from getpass import getpass

load_dotenv()
password = os.environ.get("pass")
key = getpass("Enter your password: ")
this_script = os.path.basename(__file__)
if(password == key):
    current_dirt = os.getcwd()
    # new_folder = os.path.join(current_dirt,"myfolder")
    images_folder = os.path.join(current_dirt,"image files")
    html_folder = os.path.join(current_dirt,"html files")
    text_folder = os.path.join(current_dirt,"text_folder")
    python_folder = os.path.join(current_dirt,"python files")
    other = os.path.join(current_dirt,"other files")

    os.makedirs(images_folder,exist_ok=True)
    os.makedirs(python_folder,exist_ok=True)
    os.makedirs(html_folder,exist_ok=True)
    os.makedirs(other,exist_ok=True)
    os.makedirs(text_folder,exist_ok=True)

    dict = {
        "images" : ["jpeg","jpg","png"],
        "text" : ["txt"],
        "html" : ["html","htm"],
        "python" : ["py"]
    }

    for root,dicrt,files in os.walk(current_dirt):
        for file_name in files:
            moved = False
            src = os.path.join(root,file_name)
            ext = os.path.splitext(file_name)[1].lower().lstrip(".")
            if file_name in [".env","practice.py", this_script]:   # ignore .env aur apna script
                continue
            for keys,values in dict.items():
                
                if ext in values:
                    if keys == "images":
                        os.rename(src,os.path.join(images_folder,file_name))
                        moved = True
                        break
                    elif keys == "text":
                        os.rename(src,os.path.join(text_folder,file_name))
                        moved = True
                        break
                    elif keys == "html":
                        os.rename(src,os.path.join(html_folder,file_name))
                        moved = True
                        break
                    elif keys == "python":
                        os.rename(src,os.path.join(python_folder,file_name))
                        moved = True
                        break
            if not moved:  
               os.rename(src, os.path.join(other, file_name))
                        

else:
    print("password is wrong")
    