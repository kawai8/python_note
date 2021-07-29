import os

##os.walk yields a 3-tuple (dirpath, dirnames, filenames) by walking the directory tree.
path = "/foo/var/"
for root, dirs, files in os.walk(path):
    for file in files:
        print(file)

#python 3.8 and earlier, '__file__' returns the path specified when executing.
#python 3.9 and later, '__file__' always returns an absolute path.
print('[__file__] = ' + __file__)

#Return a string representing the current working directory.
print('[os.getcwd] = ' + os.getcwd())

#Return the base name of pathname path.
print('[os.path.basename] = ' + os.path.basename(__file__))

#Return the directory name of pathname path.
print('[os.path.dirname] = ' + os.path.dirname(__file__))

#Return a normalized absolutized version of the pathname path.
print('[os.path.abspath] = ' + os.path.abspath(__file__))
