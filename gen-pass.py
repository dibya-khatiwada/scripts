import subprocess
import sys
import argparse
codeword = []
parser = argparse.ArgumentParser(usage="python gen-password.py -l <length of the password>")
parser.add_argument( '-l', '--length', type=int, help='Length of the password', required=True)
parser.add_argument( '-s', '--steps', type=int, default=1, help='Steps to repeat for password generation', required=True)

args = parser.parse_args()

def get_random_string(length):
    cmd = 'LC_CTYPE=C tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)\[\]-+= < /dev/urandom | head -c '+str(length)+' | xargs'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    return (output[0].strip().decode())

if args.length and args.steps:
    for x in range(args.steps):
        codeword.append(get_random_string(args.length))

print("-".join(codeword))

