import os

from sys import argv


try: name = (argv[1])
except:
    try: name = (input ("Ведите путь и название файла"))
    except FileNotFoundError:
         name = (input ("Ведите путь и название файла"))

for root, dirs, files in os.walk("."):
    if name in files:
        print(os.path.join(root, name), os.getcwd())
    if name in dirs:
        print(os.path.join(root, name), os.getcwd())
__all__ = (name)