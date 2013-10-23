#!/usr/bin/env python

import sys
import subprocess as sp

import os

# Global_paths
path = os.getenv('HOME')
path = '/home/manoj/'

script_bin_path = path+'/script_bin'
script_bin_syspath = path 
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
		#Modules
		self.modules_list = ['ft5x_ts','ektf2k','gt811_ts']		
		# Determine which should be current module
		self.load_module = self.current_module(self.modules_list)	
		# Load the module
		sp.Popen(["modprobe",self.load_module])		
	
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
		self.touch_success(path, self.current_module)

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
				self.touch_failed(path, self.current_module)

			return True
		
		return False
	### END TIMER CODE ###

	def touch_failed(self,path,module):
		# Register the current_module is bad module
		self.file_obj = open(path+'/bad_modules','a')
		self.file_obj.write(module+' ')
		
		# Change script.bin
		# Note: all script.bin files should be saved as script.bin_modulename
		sp.Popen(['cp',script_bin_path+'/script.bin_'+module, script_bin_syspath+'/script.bin'])
		sp.Popen('reboot')

	def touch_success(self.path,module):
		self.file_obj = open(path+'/input_touch','w')
		self.file_obj.write(module)

	def current_module(self, modules_list):
		# If bad_modules file is not found
		try:
			self.file_obj = open(path+'/bad_modules','r')
			self.bad_modules = self.file_obj.read()
		
			for module in modules_list:
				if self.bad_modules.find(module) == -1:
					return module
		except:
			return modules_list[0]
