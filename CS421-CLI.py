#!/usr/bin/python2.7

import argparse
import mysql.connector

parser = argparse.ArgumentParser()
parser.add_argument("-a", action='store', dest='table', required=True, help="Add to table A")
parser.add_argument("-t", action='store', dest='textfile', required=True, help="Use text file T")
args = parser.parse_args()

# the name of the file
fileName = args.textfile
Table    = args.table

# MySQL connection information
cnx = mysql.connector.connect(user='',password='',database='CS421',host='localhost')
cur = cnx.cursor()

f = open(fileName)
line = f.readline()

# If table flag is C for car table
if Table == 'C':
    while line:
        line.split()
        a,b,c,d,e,f,g=line.split()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        # MySQL code to insert the value into the Database
        line = f.readline()
    f.close(_fetch_row)

# If table flag is B for brand table
elif Table == 'B':
    while line:
        line.split()
        a,b,c=line.split()
        print(a)
        print(b)
        print(c)
        # MySQL stuff goes here
        insert = ("""INSERT INTO brand(make,brand_worth,public) VALUES(%s,%s,%s)""")
        data_value = (a,b,c)
        cur.execute(insert,data_value)
        cnx.commit()
        line = f.readline()
    f.close()

# If table flag is E for Engine table
elif Table == 'E':
    while line:
        line.split()
        a,b,c,d,e,f,g=line.split()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        #MySQL stuff goes here
        line = f.readline()
    f.close()

# If table flag is BT for Body Type table
elif Table == 'BT':
    while line:
        line.split()
        a,b,c,d,e=line.split()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        #MySQL stuff goes here
        line = f.readline()
    f.close()

# If table flag is T for Tech table
elif Table == 'T':
    while line:
        line.split()
        a,b,c,d,e,f=line.split()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        #MySQL stuff goes here
        line = f.readline()
    f.close()

# If table flag is R for Review table
elif Table == 'R':
    while line:
        line.split()
        a,b,c=line.split()
        print(a)
        print(b)
        print(c)
        #MySQL stuff goes here
        line = f.readline()
    f.close()

# If table flag is CO for Cost of Ownership table
elif Table == 'CO':
    while line:
        line.split()
        a,b,c,d,e=line.split()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        #MySQL stuff goes here
        line = f.readline()
    f.close()

# If table flag is UE for Uses Engine table
elif Table == 'UE':
    while line:
        line.split()
        a,b=line.split()
        print(a)
        print(b)
        #MySQL stuff goes here
        line = f.readline()
    f.close()

# If table flag is JP for Joint Project table
elif Table == 'JP':
    while line:
        line.split()
        a,b,c,d,e,f,g,h,i=line.split()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
        print(i)
        #MySQL stuff goes here
        #cur.execute()
        #con.commit()
        line = f.readline()
    f.close()

# Fail state for invalid options
else:
    print "Invalid parameter"

# Close MySQL connection
cur.close()
cnx.close()
