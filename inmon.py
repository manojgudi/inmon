#!/usr/bin/env python

# path variable is where the module_file resides
import os
#path = os.getenv('HOME') #This shouldnt work since this program will run as root
path = '/home/manoj/'

def check_module_file_exists(path):
	try:
		open(path+'/input_touch','r')
		return True
	except:
		return False
			

if __name__=="__main__" :
	
	if not check_module_file_exists(path):
		import UI_GTK
		front_obj=UI_GTK.front_end()
		front_obj.main()
    		UI_GTK.gtk.main()
