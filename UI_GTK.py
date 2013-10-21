#!/usr/bin/env python

import sys
import subprocess as sp


try:
	import pygtk
	import gobject
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
		
		#Set glade file
		self.gladefile = "./UI.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.gladefile)
		
		#Set window file
		self.window=self.glade.get_object("inmon_window")
		self.window.show_all()
		self.window.connect("destroy",self.main_quit)
		
		#Set Label 
		self.seconds_label = self.glade.get_object("inmon_label2")
		# Intialize Seconds
		self.seconds_label.set_text('20')


		## dic start
		self.dic = {
		"on_okay_press" : self.on_okay_press

		}
		## End of dic
		self.glade.connect_signals(self.dic)

	def main_quit(self,widget):
		"""
			Predefined callback.
			Equivalent to self.quit()
		"""                    
		
		print "Exiting..."
		gtk.main_quit()
                
	def main(self):		
	# Insert any code just before apps goes into gtk.main()
		self.timer()
		print 'main()'

	

	def on_okay_press(self, widget):
		self.inmon_button = self.glade.get_object("inmon_button")
		self.touch_success()

		print 'pressed okay'

	### TIMER CODE ###
	def timer(self):
		self.timer_id = gobject.timeout_add(1000,self.update_clock)

	def update_clock(self):
		if self.timer_id is not None:
			seconds = self.seconds_label.get_text()
			if len(seconds):
				seconds = int(seconds)
			else:
				seconds = 10
			
			# Count backwards
			seconds = seconds - 1
			self.seconds_label.set_text(str(seconds))
			print seconds

			if seconds == 0:
				self.timer_id = None
				print "Preparing to copy different touch config files"
				self.touch_failed()

			return True
		
		return False
	### END TIMER CODE ###

	def touch_failed(self):
		pass

	def touch_success(self):
		pass
