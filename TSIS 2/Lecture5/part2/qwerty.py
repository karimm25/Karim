import os

class work_with_files:
    def del_f(self,target): #delete file
        os.remove(target)
    def rename_f(self,target): #check this function # reaname file
        new_name = input()
        os.rename(target,new_name) 
    def add_cont_f(self,target): # add content
        cont = input()
        with open(target,'a') as f:
            f.write(cont)
    def rewrite_f(self,target): # rewrite all file
        with open(target,'w') as f:
            f.write(input())
    def parent_dir(self, target): # view parent directory path
        NEW_ULR = os.path.abspath(os.path.join(target,os.pardir))
        print(NEW_ULR)

class work_with_dir:
    def rename_dir(self,target): # renamedirectory
        os.rename(target,input())
    def num_of_files(self,target): # number of files
        num = [file for file in target if os.path.isfile(file)]
        print(len(num))
    def num_of_dir(self,target): # number of directorys
        num = [dir for dir in target if os.path.isdir(dir)]
        print(len(num))
    def list_cont(self,target): # list content of directory
        for content in os.listdir(target):
            content_name = os.path.join(target,content)
            if os.path.isdir(content_name):
                print(f"DIR -> {content_name}")
            if os.path.isfile(content_name):
                print(f"FILE -> {content_name}")
    def add_file(self, target): # add file
        tst = input()
        with open(os.path.join(target,tst),'x') as file:
            file.write('')
    def add_dir(self, target): # add directory
        new_dir = input()
        os.mkdir(new_dir)

UL = 'C:\\'

for target in os.listdir(UL):
    f = work_with_files()
    d = work_with_dir()
    target_name = os.path.join(UL,target)
    if os.path.isdir(target_name):
        next = input(target + " dir: ")
        if next == "add dir":
            d.add_dir(target_name)
        if next == "add file":
            d.add_file(target_name)
        if next == "list":
            d.list_cont(target_name)
            print('\n')
        if next == "num of dir":
            d.num_of_dir(target_name)
            print('\n')
        if next == "num of files":
            d.num_of_files(target_name)
            print('\n')
        if next == "rename":
            d.rename_dir(target_name)
    if os.path.isfile(target_name):
        next = input(target_name + " file: ")
        if next == "del":
            f.del_f(target_name)
        if next == "add cont":
            f.add_cont_f(target_name)
        if next == "rewrite":
            f.rewrite_f(target_name)
        if next == "rename":
            f.rename_f(target_name)
        if next == "par":
            f.parent_dir(target_name)