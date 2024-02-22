#import glob
import os
import glob2

        
for filepath in glob2.iglob('./**/*.css', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('#666666', '#417690')
    with open(filepath, "w") as file:
        file.write(s)

        print(str(filepath))
        
'''
for filepath in glob2.iglob('./**/*.js', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('2a2a2a', '434319')
    with open(filepath, "w") as file:
        file.write(s)
for filepath in glob2.iglob('./**/*.css', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('2a2a2a', '434319')
    with open(filepath, "w") as file:
        file.write(s)
'''
