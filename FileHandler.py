import os
import shutil

def create_folder():
    print("Enter Folder name:")
    name = input()
    folder = os.getcwd() + "/" + name  
    if not os.path.exists(folder):
        os.makedirs(folder, 0o777)
        print("Folder Created")
    else:
        print("Folder already exists")


def change_extension():
    print("Enter old Extension:")
    old_extension = input()
    print("Enter new Extension:")
    new_extension = input()
    print("Press 1 for all files and 2 for a specific file")
    option = input()
    if option == "1":
        folder = os.getcwd()                    
        for filename in os.listdir(folder):
            in_file_name = os.path.join(folder, filename)
            if not os.path.isfile(in_file_name):
                continue
            os.path.splitext(filename)
            new_name = in_file_name.replace(old_extension, new_extension)
            os.rename(in_file_name, new_name)
        print("Modifying Extension Complete")
    elif option == "2":
        folder = os.getcwd()
        print("Enter file name:")
        filename = input()
        newfile = filename+"."+old_extension
        in_file_name = os.path.join(folder, newfile)
        os.path.splitext(newfile)
        new_name = in_file_name.replace(old_extension, new_extension)
        os.rename(in_file_name,new_name)
        print("Modifying Extension Complete")
        filename = new_name
        file_open(filename)


def create_copy():
    print("Enter file Name with Extension")
    file_name = input()
    if os.path.isfile(file_name):
        shutil.copy2(file_name, '(copy)' + file_name)
        print("Copy Created")
    else:
        print("No such file")


def delete_file():
    print("Enter file Name with Extension")
    file_name = input()
    if os.path.isfile(file_name):
        os.remove(file_name)
        print("File Removed!")
    else:
        print("No such File")


def delete_folder():
    print("Enter folder")
    filename = input()
    if os.path.exists(filename):
        shutil.rmtree(filename, ignore_errors=True)  
        print("Folder Deleted")
    else:
        print("No Such Folder")


def move_file():
    print("Enter filename:")
    filename = input()
    if os.path.exists(filename):
        print("Enter sub folder:")
        folder = input()
        if os.path.exists(folder):
            os.rename(filename, folder + '/' + filename)
            print("File moved")
        else:
            print("Folder doesnt exist. Would you like to create folder (yes/no)")
            f = input()
            if f == 'yes':
                os.makedirs(folder, 0o777)
                os.rename(filename, folder + '/' + filename)
                print("File moved")
            elif f == 'no':
                print("Folder not created")
            else:
                print("invalid input")
    else:
        print("No such file")


def move_ext():
    print("Enter Extension:")
    ext = input()
    print("Enter sub folder:")
    folder = input()
    flag = 0
    if not os.path.exists(folder):
        print("Folder doesnt exist. Would you like to create folder (yes/no)")
        f = input()
        if f == 'yes':
            os.makedirs(folder, 0o777)
        elif f == 'no':
            print("Folder not created")
        else:
            print("invalid input")
    if os.path.exists(folder):
        for filename in os.listdir(os.getcwd()):
            if ext in filename:
                os.rename(filename, folder + '/' + filename)
                flag = 1
    if flag == 0:
        print("No files moved")
    else:
        print("Moving of files complete")
def file_open(filename):
    print("Do you wish to open the file ?")
    ans = input()
    if ans=="yes" or ans=="Yes" or ans=="YES" or ans=="Y" or ans=="y" :
        os.startfile(filename)
    elif ans=="NO" or ans=="no" or ans=="No" or ans=="N" or ans=="n" :
        print("OK")
    else:
        print("Invalid Input type Y/N")
        file_open(filename)

print("\n         EASY  FILE  HANDLER           ")
print("          By Divyansh Bhasin            ")
print(" ------------------------------------")
while True:
    
    print("\n1.Create a folder")
    print("2.Create copy of a file")
    print("3.Delete file")
    print("4.Delete folder")
    print("5.Move specific file to sub folder")
    print("6.Move according to extension")
    print("7.Change Extension")
    print("0.Exit")
    cmd = input()
    if cmd == '1':
        create_folder()
    elif cmd == '2':
        create_copy()
    elif cmd == '3':
        delete_file()
    elif cmd == '4':
        delete_folder()
    elif cmd == '5':
        move_file()
    elif cmd == '6':
        move_ext()
    elif cmd == '7':
        change_extension()
    elif cmd == '0':
        break
    else:
        print("Invalid command.")

