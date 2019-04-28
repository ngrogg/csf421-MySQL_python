import Tkinter as tk
import sys
import ttk
import tkMessageBox
import mysql.connector



#each class is a page in this set up
#mainapp creates the initialization of the app's baseline
#the for loop  holds a list that holds the names of all of the
#other page classes to be passed into self.frames and loaded when their buttons are clicked.
class mainapp(tk.Tk):
	
	def __init__(self, *args, **kwargs ):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side="top",fill="both",expand=True )

		container.grid_rowconfigure(0,weight=1)
		container.grid_rowconfigure(0,weight=1)

		self.frames = {}
		#Don't forget to add new page classes to this list
		for F in (StartPage,QueryPage,InsertPage,QEPage,RemovePage,TEPage):		
			frame = F(container,self)
			self.frames[F] = frame
			frame.grid(row=0,column=0,sticky="nsew")
		
	#Use controller.show_frame(Page'sClassName) on button command to load each page 
		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

############################
## EXPORT TABLE FUNCTIONS ##
############################
	# Export bodytype
    	def BODYTYPE(self):
		# Open MySQL connection
		self.cnx = mysql.connector.connect(user='george', password='LabPass123', database='CS421',host='localhost')
		self.cur = self.cnx.cursor()
		self.command=("""SELECT * FROM body_type INTO OUTFILE '/home/oddone9139/ProjectExports/bodytype.csv';""")			
		self.cur.execute(self.command)
		self.cnx.commit()
		self.cur.close()
		self.cnx.close()
		   
	# Export brand
	def BRAND(self):
		# Open MySQL connection
		self.cnx = mysql.connector.connect(user='george', password='LabPass123', database='CS421',host='localhost')
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

############
#Start Page#
############
#Start Page is the first page you see in the application
class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.style = ttk.Style()
		label = tk.Label(self,text="Start page")
		label.pack()

	#begin buttons
		quitbutton = tk.Button(self, text="QUIT",command = lambda: controller.quit())
		quitbutton.pack(anchor = "nw", side = "left")
		
		querybutton = tk.Button(self, text="Query",command = lambda: controller.show_frame(QueryPage))
		querybutton.pack()
		
		insertbutton = tk.Button(self, text="Insert",command = lambda: controller.show_frame(InsertPage))                 
		insertbutton.pack()
		
		removebutton = tk.Button(self, text="Remove",command = lambda: controller.show_frame(RemovePage))
		removebutton.pack()

		tableExbutton = tk.Button(self, text="Export Table",command = lambda: controller.show_frame(TEPage))
		tableExbutton.pack()
		
		queryExbutton = tk.Button(self, text="Export Query",command = lambda: controller.show_frame(QEPage))
		queryExbutton.pack()
	#end buttons


###########
#QueryPage#
###########
class QueryPage(tk.Frame):
         def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.style = ttk.Style()
		label = tk.Label(self,text="Please fill out the form below to Query the database")
		label.pack()

		backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
		backbutton.pack(anchor = "sw", side = "left")
	#begin Query form code
		
        	self.Label1 = tk.Label(self)
       		self.Label1.place(relx=0.183, rely=0.089, height=28, width=46)
        	self.Label1.configure(activebackground="#f9f9f9")
        	self.Label1.configure(text='''SELECT''')

        	self.Label2 = tk.Label(self)
        	self.Label2.place(relx=0.183, rely=0.2, height=18, width=46)
        	self.Label2.configure(activebackground="#f9f9f9")
        	self.Label2.configure(text='''FROM''')

        	self.Label3 = tk.Label(self)
        	self.Label3.place(relx=0.183, rely=0.311, height=18, width=46)
        	self.Label3.configure(activebackground="#f9f9f9")
        	self.Label3.configure(text='''WHERE''')
		
	# Select input box
	        self.Entry1 = tk.Entry(self)
	        self.Entry1.place(relx=0.317, rely=0.089,height=20, relwidth=0.243)
	        self.Entry1.configure(background="white")
	        self.Entry1.configure(font="TkFixedFont")
	        self.Entry1.configure(selectbackground="#c4c4c4")
	# FROM input box
	        self.Entry2 = tk.Entry(self)
	        self.Entry2.place(relx=0.317, rely=0.2,height=20, relwidth=0.243)
	        self.Entry2.configure(background="white")
	        self.Entry2.configure(font="TkFixedFont")
	        self.Entry2.configure(selectbackground="#c4c4c4")
	#WHERE STATEMENT
	    # WHERE input box1
	        self.Entry3 = tk.Entry(self)
	        self.Entry3.place(relx=0.317, rely=0.311,height=20, relwidth=0.243)
	        self.Entry3.configure(background="white")
	        self.Entry3.configure(font="TkFixedFont")
	        self.Entry3.configure(selectbackground="#c4c4c4")
	    # WHERE Input box2
	        self.Entry4 = tk.Entry(self)
	        self.Entry4.place(relx=0.633, rely=0.311,height=20, relwidth=0.243)
	        self.Entry4.configure(background="white")
	        self.Entry4.configure(font="TkFixedFont")
	    # Radio button for WHERE
	        #self.RadioWHERE = tk.Radiobutton(self)
	        self.RadioWHERE = tk.Checkbutton(self)
	        self.RadioWHERE.place(relx=0.017, rely=0.311, relheight=0.044
                , relwidth=0.132)
	        self.RadioWHERE.configure(activebackground="#f9f9f9")
	        self.RadioWHERE.configure(justify='left')
	        self.RadioWHERE.configure(text='''WHERE?''')
	    # Drop down menu for WHERE statement logicals
	        self.TCombobox1 = ttk.Combobox(self)
	        self.TCombobox1.place(relx=0.567, rely=0.311, relheight=0.04
                , relwidth=0.062)
	        self.value_list = ['AND','OR','>','<','=','!=']
	        self.TCombobox1.configure(values=self.value_list)
	        self.TCombobox1.configure(takefocus="")
	# Query OutPut box
	        #self.Scrolledtext1 = tk.scrolledtext.ScrolledText(self)
	        #self.Scrolledtext1.place(relx=0.0, rely=0.667, relheight=0.262
                #, relwidth=0.98)
	        #self.Scrolledtext1.configure(background="white")
	        #self.Scrolledtext1.configure(font="TkTextFont")
	        #self.Scrolledtext1.configure(insertborderwidth="3")
	        #self.Scrolledtext1.configure(selectbackground="#c4c4c4")
	        #self.Scrolledtext1.configure(width=10)
	        #self.Scrolledtext1.configure(wrap="none")
	# Run Query button
	        self.Button1 = tk.Button(self)
	        self.Button1.place(relx=0.017, rely=0.578, height=28, width=92)
	        self.Button1.configure(text='''Run Query''')
		

#############
#Insert Page#
#############
class InsertPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.style = ttk.Style()

		label = tk.Label(self,text="Please fill out the form to insert a car into the database. No box may be left empty.")
		label.pack()

		backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
		backbutton.pack(anchor = "sw", side = "left")

###################		
#Export Query Page#
###################
class QEPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
	        self.style = ttk.Style()

		label = tk.Label(self,text="Please fill out the form to query the database. No box may be left empty.")
		label.pack()
		backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
		backbutton.pack(anchor = "sw", side = "left")

	#begin Query form code
		
        	self.Label1 = tk.Label(self)
       		self.Label1.place(relx=0.183, rely=0.089, height=28, width=46)
        	self.Label1.configure(activebackground="#f9f9f9")
        	self.Label1.configure(text='''SELECT''')

        	self.Label2 = tk.Label(self)
        	self.Label2.place(relx=0.183, rely=0.2, height=18, width=46)
        	self.Label2.configure(activebackground="#f9f9f9")
        	self.Label2.configure(text='''FROM''')

        	self.Label3 = tk.Label(self)
        	self.Label3.place(relx=0.183, rely=0.311, height=18, width=46)
        	self.Label3.configure(activebackground="#f9f9f9")
        	self.Label3.configure(text='''WHERE''')
		
	# Select input box
	        self.Entry1 = tk.Entry(self)
	        self.Entry1.place(relx=0.317, rely=0.089,height=20, relwidth=0.243)
	        self.Entry1.configure(background="white")
	        self.Entry1.configure(font="TkFixedFont")
	        self.Entry1.configure(selectbackground="#c4c4c4")
	# FROM input box
	        self.Entry2 = tk.Entry(self)
	        self.Entry2.place(relx=0.317, rely=0.2,height=20, relwidth=0.243)
	        self.Entry2.configure(background="white")
	        self.Entry2.configure(font="TkFixedFont")
	        self.Entry2.configure(selectbackground="#c4c4c4")
	#WHERE STATEMENT
	    # WHERE input box1
	        self.Entry3 = tk.Entry(self)
	        self.Entry3.place(relx=0.317, rely=0.311,height=20, relwidth=0.243)
	        self.Entry3.configure(background="white")
	        self.Entry3.configure(font="TkFixedFont")
	        self.Entry3.configure(selectbackground="#c4c4c4")
	    # WHERE Input box2
	        self.Entry4 = tk.Entry(self)
	        self.Entry4.place(relx=0.633, rely=0.311,height=20, relwidth=0.243)
	        self.Entry4.configure(background="white")
	        self.Entry4.configure(font="TkFixedFont")
	    # Radio button for WHERE
	        #self.RadioWHERE = tk.Radiobutton(self)
	        self.RadioWHERE = tk.Checkbutton(self)
	        self.RadioWHERE.place(relx=0.017, rely=0.311, relheight=0.044
                , relwidth=0.132)
	        self.RadioWHERE.configure(activebackground="#f9f9f9")
	        self.RadioWHERE.configure(justify='left')
	        self.RadioWHERE.configure(text='''WHERE?''')
	    # Drop down menu for WHERE statement logicals
	        self.TCombobox1 = ttk.Combobox(self)
	        self.TCombobox1.place(relx=0.567, rely=0.311, relheight=0.04
                , relwidth=0.062)
	        self.value_list = ['AND','OR','>','<','=','!=']
	        self.TCombobox1.configure(values=self.value_list)
	        self.TCombobox1.configure(takefocus="")
	# Query OutPut box
	        #self.Scrolledtext1 = tk.scrolledtext.ScrolledText(self)
	        #self.Scrolledtext1.place(relx=0.0, rely=0.667, relheight=0.262
                #, relwidth=0.98)
	        #self.Scrolledtext1.configure(background="white")
	        #self.Scrolledtext1.configure(font="TkTextFont")
	        #self.Scrolledtext1.configure(insertborderwidth="3")
	        #self.Scrolledtext1.configure(selectbackground="#c4c4c4")
	        #self.Scrolledtext1.configure(width=10)
	        #self.Scrolledtext1.configure(wrap="none")
	# Export button
	        self.ExportQuery = tk.Button(self)
	        self.ExportQuery.place(relx=0.35, rely=0.933, height=28, width=149)
	        self.ExportQuery.configure(activebackground="#f9f9f9")
	        self.ExportQuery.configure(text='''Export''')
	# Run Query button
	        self.Button1 = tk.Button(self)
	        self.Button1.place(relx=0.017, rely=0.578, height=28, width=92)
	        self.Button1.configure(text='''Run Query''')
		

#############		
#Remove Page#
#############
class RemovePage(tk.Frame):
         def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.style = ttk.Style()
		label = tk.Label(self,text="Please fill out the form below to remove a car from the database")
		label.pack()

		backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
		backbutton.pack(anchor = "sw", side = "left")

###################		
#Export Table Page#
###################
class TEPage(tk.Frame):
         def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.style = ttk.Style()
		label = tk.Label(self,text="Please choose a table below to export")
		label.pack(anchor = "n",side = "top")

		backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
		backbutton.pack(anchor = "sw", side = "left")
		BodyType = tk.Button(self, text="BodyType",command = lambda: controller.BODYTYPE())
		BodyType.pack()
		Brand = tk.Button(self, text="Brand",command = lambda: controller.BRAND())
		Brand.pack()
		Car = tk.Button(self, text="Car",command = lambda: controller.CAR())
		Car.pack()
		CostofOwnership = tk.Button(self, text="Cost of Ownership",command = lambda: controller.COSTOFOWNERSHIP())
		CostofOwnership.pack()
		Engine = tk.Button(self, text="Engine",command = lambda: controller.ENGINE)
		Engine.pack()
		JointProject = tk.Button(self, text="Join Project",command = lambda: controller.JOINTPROJECT)
		JointProject.pack()
		Review = tk.Button(self, text="Review",command = lambda: controller.REVIEW())
		Review.pack()
		Tech = tk.Button(self, text="Tech",command = lambda: controller.TECH())
		Tech.pack()
		UsesEngine = tk.Button(self, text="Alternate Engine",command = lambda: controller.USESENGINE())
		UsesEngine.pack()



app = mainapp()
app.mainloop()
