"""This module is a Intrusion Detection System"""
import os
import hashlib

def change_string_slash(string):
    """Take away (//, \\) and set it as (/) in sent in string"""
    string = string.replace("//", "/")
    string = string.replace("\\", "/")
    return string

def find_files(directory):
    """Make a list of all files under sent in directory"""
    file_list = []
    path_list = os.listdir(directory)

    for path in path_list:
        fullpath = os.path.join(directory, path)
        fullpath = change_string_slash(fullpath)

        if os.path.isfile(fullpath):
            file_list.append(fullpath)
        elif os.path.isdir(fullpath):
            file_list += find_files(fullpath)
    return file_list

def hash_file(file_path):
    """Hash the file that is sent in"""
    open_file = open(file_path, "rb")
    sha = hashlib.sha1()
    for line in open_file.readlines():
        sha.update(line)
    open_file.close()
    return sha.hexdigest()

def create_logg(path, f_list, h_list):
    """Create a logg with path_list and hash_list"""
    open_file = open(path, "w+")
    for count,ele in enumerate(f_list):
        open_file.write(ele + " " + h_list[count] + "\n")
    open_file.close()

def create_old_logg_lists(path):
    """Create two list (file, hash) from the old logg that already exist"""
    old_hash_logg = []
    old_file_logg = []
    op_file = open(path, "r")
    lines = op_file.readlines()

    for line in lines:
        count = 0
        for word in line.split():
            if count == 0:
                old_file_logg.append(word)
            else:
                old_hash_logg.append(word)
            count += 1
    op_file.close()
    return old_file_logg, old_hash_logg

def check_changed_files(old_file, old_hash, new_file, new_hash):
    """Check if files have changed"""
    changed_list = []
    for count,ele in enumerate(old_file):
        for index, path in enumerate(new_file):
            if ele.lower() == path.lower():
                if old_hash[count] != new_hash[index]:
                    changed_list.append(ele)
    return changed_list

def check_new_files(old_file, new_file):
    """Check if there are new files"""
    new_list = []
    for ele in new_file:
        count = 0
        for path in old_file:
            if ele.lower() == path.lower():
                count += 1
        if count == 0:
            new_list.append(ele)
    return new_list

def check_removed_files(old_file, new_file):
    """Check if files got removed"""
    removed_list = []
    for ele in old_file:
        count = 0
        for path in new_file:
            if ele.lower() == path.lower():
                count += 1
        if count == 0:
            removed_list.append(ele)
    return removed_list

def main():
    print("Welcome to Intrusion Detection Check")
    print("-------------------------------------")
    loop = True
    while loop:
        path_folder = input("What folder (path full or relative) do you want to protect? ")
        try:
            files_list = find_files(path_folder) #Create list of paths to files
            loop = False
        except FileNotFoundError:
            print("File not found")
        except NotADirectoryError:
            print("This is not a directory")
    print()
    print("Report")
    print("------")

    path_folder = change_string_slash(path_folder)
    check_file = path_folder + "/" + "ids_logg.txt"

    hash_list = []
    for file in files_list: #Create list of hash signature to files
        hash_list.append(hash_file(file))

    if check_file in files_list:
        files_list.remove(check_file) #Remove ids_logg
        hash_list.remove(hash_file(check_file))
        create_logg("new_ids_logg.txt", files_list, hash_list)

        old_files_list, old_hash_list = create_old_logg_lists(check_file)
        changed_file_list = check_changed_files(old_files_list, old_hash_list, files_list, hash_list)
        new_file_list = check_new_files(old_files_list, files_list)
        removed_file_list = check_removed_files(old_files_list, files_list)

        if changed_file_list or new_file_list or removed_file_list:
            print("WARNING!\n")
            if new_file_list:
                print("NEW FILES")
                print("---------")
                for ele1 in new_file_list:
                    print(ele1)
                print()
            if changed_file_list:
                print("CHANGED FILES")
                print("---------")
                for ele2 in changed_file_list:
                    print(ele2)
                print()
            if removed_file_list:
                print("REMOVED FILES")
                print("---------")
                for ele3 in removed_file_list:
                    print(ele3)
                print()
            create_logg(check_file, files_list, hash_list)
        else:
            print("There where no changes in the folder")
        create_logg(check_file, files_list, hash_list)

    else: #If it is the first time to logg the map
        create_logg(check_file, files_list, hash_list)
        print("Creating new logg...\n")

if __name__ == "__main__":
    main()