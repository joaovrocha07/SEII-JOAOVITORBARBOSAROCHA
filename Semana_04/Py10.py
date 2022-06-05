import os
from datetime import datetime

#print(dir(os))
print(os.getcwd()) #get current working directory
os.chdir('/Users/João Vítor/PycharmProjects/pythonProject1/')
print(os.getcwd())
print(os.listdir)

#os.mkdir("OS-Demo-2")
#os.mkdir("OS-Demo-2/Sub-Dir-1")
os.makedirs("OS-Demo-2/Sub-Dir-1")
os.removedirs('OS-Demo-2/Sub-Dir-1')
#os.rename('Sistemas Digitais', 'SD')

#print(os.listdir)
#mod_time = os.stat('CD').st_mtime
#print(datetime.fromtimestamp(mod_time))

#for dirpath, dirnames, filenames in os.walk('/home/divinojr/Desktop'):   #generates a tuple of directory tree
#    print('Current Path:', dirpath)
#    print('Directories: ', dirnames)
#    print('Files: ', filenames)
#    print()

print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'teste01.txt')
print(file_path)

print(os.path.basename('/tmp/teste01.txt'))
print(os.path.dirname('/tmp/teste01.txt'))
print(os.path.split('/tmp/teste01.txt'))
print(os.path.splitext('/tmp/teste01.txt'))
print(os.path.exists('/tmp/teste01.txt'))
print(os.path.isdir('/Users/João Vítor/PycharmProjects/pythonProject1/SD'))

print(dir(os.path))
