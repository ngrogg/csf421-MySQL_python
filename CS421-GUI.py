#!/usr/bin/python2.7

import mysql.connector
import tkMessageBox
from Tkinter import *

class Application(Frame):

    ######################
    ### MAIN FUNCTIONS ###
    ######################
    
    #######################
    ### QUERY FUNCTIONS ###
    #######################
    
    ########################
    ### INSERT FUNCTIONS ###
    ########################
    
    #########################
    ### REMOVAL FUNCTIONS ###
    #########################
    
    ######################
    ## EXPORT TABLE FUNCTIONS ##
    ######################

    # Export bodytype
    def BODYTYPE(self):
         # Open MySQL connection
        self.cnx = mysql.connector.connect(user='', password='', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM body_type INTO OUTFILE '/home/oddone9139/ProjectExports/bodytype.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()
   
    # Export brand
    def BRAND(self):
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='Oddone9139', password='Mast0don!', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM brand INTO OUTFILE '/home/oddone9139/ProjectExports/brand.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()

    # Export car
    def CAR(self):
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='Oddone9139', password='Mast0don!', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM car INTO OUTFILE '/home/oddone9139/ProjectExports/car.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()

    # Export costofownership
    def COSTOFOWNERSHIP(self):
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='Oddone9139', password='Mast0don!', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM costofownership INTO OUTFILE '/home/oddone9139/ProjectExports/cow.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()

    # Export engine
    def ENGINE(self):
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='Oddone9139', password='Mast0don!', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM engine INTO OUTFILE '/home/oddone9139/ProjectExports/engine.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()

    # Export jointproject
    def JOINTPROJECT(self):
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='Oddone9139', password='Mast0don!', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM jointproject INTO OUTFILE '/home/oddone9139/ProjectExports/jointproject.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()

    # Export review
    def REVIEW(self):
         # Open MySQL connection
        self.cnx = mysql.connector.connect(user='Oddone9139', password='Mast0don!', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM review INTO OUTFILE '/home/oddone9139/ProjectExports/review.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()
   
    # Export tech
    def TECH(self):
         # Open MySQL connection
        self.cnx = mysql.connector.connect(user='Oddone9139', password='Mast0don!', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM tech INTO OUTFILE '/home/oddone9139/ProjectExports/tech.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()
   
    # Export usesengine
    def USESENGINE(self):
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='Oddone9139', password='Mast0don!', database='CS421',host='localhost')
        self.cur = self.cnx.cursor()
        self.command=("""SELECT * FROM usesengine INTO OUTFILE '/home/oddone9139/ProjectExports/usesengine.csv';""")
        self.cur.execute(self.command)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()
        
    ##############################
    ### EXPORT QUERY FUNCTIONS ###
    ##############################

    #########################
    ### GO BACK FUNCTIONS ###
    #########################

    # When go back button is hit on query screen
    def back_query(self):
        # Remove created buttons and title
        self.buttona.pack_forget()
        self.TITLEA.pack_forget()

        # Create Home buttons
        self.createWidgets()

    # When go back button is hit on insertion screen
    def back_insertion(self):
        # Remove created buttons and title 
        self.buttonb.pack_forget()
        self.TITLEB.pack_forget()
       
        # Create Home buttons
        self.createWidgets()

    # When go back button is hit on removal screen
    def back_removal(self):
        # Remove created buttons and title
        self.buttonc.pack_forget()
        self.TITLEC.pack_forget()

        # Create Home buttons
        self.createWidgets()

    # When go back button is hit on export table screen
    def back_exportTable(self):
        # Remove created buttons and title
        self.buttond.pack_forget()
        self.TITLED.pack_forget()
        self.buttond1.pack_forget()
        self.buttond2.pack_forget()
        self.buttond3.pack_forget()
        self.buttond4.pack_forget()
        self.buttond5.pack_forget()
        self.buttond6.pack_forget()
        self.buttond7.pack_forget()
        self.buttond8.pack_forget()
        self.buttond9.pack_forget()

        # Create Home buttons
        self.createWidgets()

    # When go back button is hit on export query screen
    def back_exportQuery(self):
        # Remove created buttons and title
        self.buttone.pack_forget()
        self.TITLEE.pack_forget()

        # Create Home buttons
        self.createWidgets()

    ######################
    ### HOME FUNCTIONS ###
    ######################

    # Button to run query
    def query(self):
       # Insert title text
        self.TITLE.pack_forget()
        self.TITLEA= Label(self, text="Enter query to run")
        self.TITLEA.pack()

        # Remove other buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # create Go Back button
        self.buttona = Button(self)
        self.buttona["text"] = "Back"
        self.buttona["command"] = self.back_query
        self.buttona.pack({"side" : "left"})


    # Button to insert data
    def insertion(self):
        # Insert title text
        self.TITLE.pack_forget() 
        self.TITLEB= Label(self, text="Fill form to insert")
        self.TITLEB.pack()

        # Remove other buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # Create Go Back button
        self.buttonb = Button(self)
        self.buttonb["text"] = "Back"
        self.buttonb["command"] = self.back_insertion
        self.buttonb.pack({"side" : "left"})

    # Button to remove data
    def removal(self):
        # Insert title text
        self.TITLE.pack_forget() 
        self.TITLEC= Label(self, text="Enter values to export")
        self.TITLEC.pack()

        # Remove Home buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # Create Go Back button
        self.buttonc = Button(self)
        self.buttonc["text"] = "Back"
        self.buttonc["command"] = self.back_removal
        self.buttonc.pack({"side" : "left"})


    # Button to export table
    def exportTable(self):
        # Insert title text
        self.TITLE.pack_forget() 
        self.TITLED= Label(self, text="Select table export")
        self.TITLED.pack()

        # Remove Home buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # Create Go Back button
        self.buttond = Button(self)
        self.buttond["text"] = "Back"
        self.buttond["command"] = self.back_exportTable
        self.buttond.pack({"side" : "left"})

        # Buttons for table export

        # Export bodytype button
        self.buttond1 = Button(self)
        self.buttond1["text"] = "Body Type"
        self.buttond1["command"] = self.BODYTYPE
        self.buttond1.pack({"side":"left"})

        # Export brand
        self.buttond2 = Button(self)
        self.buttond2["text"] = "Brand"
        self.buttond2["command"] = self.BRAND
        self.buttond2.pack({"side":"left"})

        # Export car
        self.buttond3 = Button(self)
        self.buttond3["text"] = "Car"
        self.buttond3["command"] = self.CAR
        self.buttond3.pack({"side":"left"})

        # Export costofownership
        self.buttond4 = Button(self)
        self.buttond4["text"] = "Cost of Ownership"
        self.buttond4["command"] = self.COSTOFOWNERSHIP
        self.buttond4.pack({"side":"left"})
       
        # Export engine
        self.buttond5 = Button(self)
        self.buttond5["text"] = "Engine"
        self.buttond5["command"] = self.ENGINE
        self.buttond5.pack({"side":"left"})
      
        # Export jointproject
        self.buttond6 = Button(self)
        self.buttond6["text"] = "Joint Project"
        self.buttond6["command"] = self.JOINTPROJECT
        self.buttond6.pack({"side":"left"})
     
        # Export review
        self.buttond7 = Button(self)
        self.buttond7["text"] = "Review"
        self.buttond7["command"] = self.REVIEW
        self.buttond7.pack({"side":"left"})
    
        # Export tech
        self.buttond8 = Button(self)
        self.buttond8["text"] = "Tech"
        self.buttond8["command"] = self.TECH
        self.buttond8.pack({"side":"left"})
   
        # Export usesengine
        self.buttond9 = Button(self)
        self.buttond9["text"] = "Uses Engine"
        self.buttond9["command"] = self.USESENGINE
        self.buttond9.pack({"side":"left"})


    # Button to export query
    def exportQuery(self):
        # Delete old title text and Insert title text
        self.TITLE.pack_forget() 
        self.TITLEE= Label(self, text="Enter query to run and export")
        self.TITLEE.pack()

        # Remove Home buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # Create Go Back button
        self.buttone = Button(self)
        self.buttone["text"] = "Back"
        self.buttone["command"] = self.back_exportQuery
        self.buttone.pack({"side" : "left"})


    # Home page 
    def createWidgets(self):
        # Title
        self.TITLE = Label(self, text="Car Database")
        self.TITLE.pack()

        # Button Parameters
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        # Create Button
        self.QUIT.pack({"side": "left"})

        # Button parameters for Query button
        self.QUERY = Button(self)
        self.QUERY["text"] = "Query"
        self.QUERY["command"] = self.query

        # Add Query Button to GUI
        self.QUERY.pack({"side": "left"})

        # Button Parameters for Insertion button
        self.INSERTION = Button(self)
        self.INSERTION["text"] = "Insertion"
        self.INSERTION["command"] = self.insertion

        # Create Button
        self.INSERTION.pack({"side": "left"})

        # Button for Removal
        self.REMOVAL = Button(self)
        self.REMOVAL["text"] = "Removal"
        self.REMOVAL["command"] = self.removal
        self.REMOVAL.pack({"side": "left"})

        # Button for Exporting table
        self.EXPORTTABLE = Button(self)
        self.EXPORTTABLE["text"] = "ExportTable"
        self.EXPORTTABLE["command"] = self.exportTable
        self.EXPORTTABLE.pack({"side": "left"})

        # Button for Exporting Query
        self.EXPORTQUERY = Button(self)
        self.EXPORTQUERY["text"] = "ExportQuery"
        self.EXPORTQUERY["command"] = self.exportQuery
        self.EXPORTQUERY.pack({"side":"left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
