import sys
import argparse
import numpy as np
# print(sys.argv)
# print(type(sys.argv))

#argparsing
parser = argparse.ArgumentParser(description = "Calculate the speed of Sound in a Medium ")
parser.add_argument ('-d', '--density', type=float, metavar ="", help = "This is the Denisty of the Medium in kg/m^3", default = '1.225')
parser.add_argument('-r', '--rho', type = float, metavar ="", help = "adiabatic index of the medium", default = '1.4')
parser.add_argument('-p', '--pressure', type = float, metavar ="", help = "Pressure of the Medium in Pa", default = '101325')
#metavar just helps clean thing sout in -h on the terminal
grouper = parser.add_mutually_exclusive_group()
grouper.add_argument('-v', '--verbose', action = 'store_true', help = "Prints the speed of sound in the medium with explanation")
grouper.add_argument('-q', '--quiet', action = 'store_true', help = "Prints the speed of sound in the medium without explanation")
args = parser.parse_args()
 # store_true for boolean values as default
if( __name__ == "__main__"):
    if(args.quiet):
        print(np.sqrt(args.rho * args.pressure / args.density))
    else:
        print("The speed of sound in the medium is: ") 
        print(np.sqrt(args.rho * args.pressure / args.density))

    
    
