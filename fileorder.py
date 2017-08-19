import datetime
import os.path
import shutil


while True:
    filetype = input("Enter the file type you want to move\nType EXIT to end the program:\n")
    if filetype == "EXIT":
        break
    for filename in os.listdir():
        if os.path.isfile(filename):
         if filetype in filename:
            mtime = os.path.getmtime(filename)
            lastmd = datetime.datetime.fromtimestamp(mtime)
            lastdate = str(lastmd)
            month = lastdate.split("-")
            try:
                os.mkdir(month[1]+" "+month[0])
            except FileExistsError:
                pass
            shutil.move(filename,month[1]+" "+month[0] +"//"+ filename)

