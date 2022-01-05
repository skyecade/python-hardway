from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# we could do these two on one line

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")

print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

open(to_file, 'a').write(indata)

print("Alright, all done.")
