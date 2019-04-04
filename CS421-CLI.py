#!/usr/bin/python2.7

import argparse
import mysql.connector

parser = argparse.ArgumentParser()
parser.add_argument("-a", action='store', dest='table',    help="Add to table A")
parser.add_argument("-t", action='store', dest='textfile', help="Use text file T")
args = parser.parse_args()

# the name of the file
fileName = args.textfile
Table    = args.table

# MySQL connection information
#mysql.connector.connect(host='localhost',database='l',user='',password='')

f = open(fileName)
#f = open('sample.txt')
line = f.readline()

# If table flag is C for car table

# If table flag is B for brand table
while line:
    #print(line)
    line.split()
    a,b,c=line.split()
    print(a)
    print(b)
    print(c)
    # MySQL stuff goes here
    line = f.readline()
f.close()

# If table flag is E for Engine table

# If table flag is BT for Body Type table

# If table flag is T for Tech table

# If table flag is R for Review table

# If table flag is CO for Cost of Ownership table

# If table flag is UE for Uses Engine table

# If table flag is JP for Joint Project table

# Close MySQL connection
