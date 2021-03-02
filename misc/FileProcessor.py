# Copied from StackOverflow for learning purposes
import iptcinfo3
import os
import random
import string
import sys


# Random string gennerator
def rnd(length=3):
    return ''.join(random.choices(list(string.ascii_letters), k=length))


# Path to the file, open a IPTCInfo object
path = os.path.join(sys.path[0], 'DSC_7960.jpg')
info = iptcinfo3.IPTCInfo(path)
# Show the keywords
print(info['keywords'])
# Add a keyword and save
info['keywords'] = [rnd()]
info.save()
# Remove the weird ghost file created after saving
os.remove(path + '~')
