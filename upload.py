from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from os import listdir
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

dir1= r"C:/Users/sachi/Desktop/appzui"
os.chdir(dir1)

def DriveFileUpload(dir1,id):
    if id != None:
        print("id inside if",id)
        upload_pics(id)
    else:
        new_folder = drive.CreateFile({'title':'{}'.format('appzui'),'mimeType':'application/vnd.google-apps.folder'})
        new_folder.Upload()
        print("new folder",new_folder['id'])
        upload_pics( new_folder['id'])
        return new_folder['id']

def ListFiles():
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
        if file1['title']== "appzui":
            return file1['id']

def upload_pics(id):
    fnames = listdir(dir1)
    lst222=[]
    for fname in fnames:
        if (fname.endswith(".jpg") or fname.endswith(".png")):
            list1 = drive.ListFile({'q': "'%s' in parents and trashed=false" % id}).GetList()
            for lst in list1:
                lst222.append(lst['title'])
            if fname in lst222:
                print("fname exists",fname)
            else:
                nfile = drive.CreateFile({'title': os.path.basename(fname), 'parents': [{u'id': id}]})
                nfile.SetContentFile(fname)
                nfile.Upload()


id= ListFiles()
id= DriveFileUpload(dir1,id)





