import os
import django
import sys

os.chdir(".")
print("Current dir=" ,  end= ""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath))
print(BASE_DIR="")