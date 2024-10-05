import argparse
import adduser
import real_time

parser = argparse.ArgumentParser(prog='run')

parser.add_argument('-r', '--run', action = 'store_true')
parser.add_argument('-a', '--add', help="adds new user to the list of known faces")
args = parser.parse_args()

if(args.run):
    real_time.main()
if(args.add):
    adduser.main(args.add)