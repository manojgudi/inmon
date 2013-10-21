#!/usr/bin/env python

import sys
import subprocess as sp


try:
	import pygtk
	pygtk.require("2.0")
except:
	print "check pygtk deps"
	sys.exit()
	
try:
	import gtk
	import gtk.glade 
except:
	print "check gtk deps"
	sys.exit(1)

class front_end:
	""" This is front handler for appsearch feature"""
	def __init__(self):
		
		# Set environment path
		#import os
		#path="/opt/py_finder/"
		#os.chdir(path)
		
		#Set glade file
		self.gladefile = "./UI.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		
		self.window=self.glade.get_object("inmon_window")
		self.window.show_all()
		self.window.connect("destroy",self.main_quit)
		
		'''
		## dic start
		self.dic = {
		"on_apps_searchbox_activate" : self.on_apps_searchbox_activate,
		"gtk_main_quit" : self.main_quit, 
		"on_apps_search_button_clicked" : self.on_apps_searchbox_activate,
		"on_file_searchbox_activate" : self.on_file_searchbox_activate,
		"on_file_search_button_clicked" : self.on_file_searchbox_activate,
		"on_notebook_switch_page" : self.on_notebook_focus_tab,
		"on_quit_button_clicked" : self.on_quit_button_clicked,
		"on_quit_wo_onboard_clicked" : self.on_quit_wo_onboard_clicked
		}
		## End of dic
		self.glade.connect_signals(self.dic)
		'''

	def main_quit(self,widget):
		"""
			Predefined callback.
			Equivalent to self.quit()
			I want my ram free of any infections after fucking with GTK....;)
		"""                    
		
		print "Exiting..."

		gtk.main_quit()
                
	def main(self):		
	# Insert any code just before apps goes into gtk.main()
		print 'main()'

	def on_quit_button_clicked(self, widget):
		### Quit whole application and onboard/florence instance
		self.main_quit(widget)

