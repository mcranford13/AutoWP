#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AutoWPTrue.py
#  
#  Copyright 2016 root <root@kali>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


#################
#   Libraries   #
#################
try:
	from subprocess import Popen, PIPE, STDOUT, call
	from email.mime.text import MIMEText
	from email.MIMEMultipart import MIMEMultipart
	import datetime,os,sys, smtplib, email.utils
	import argparse
except:
	print "You are missing some needed libraries."
	sys.exit(1)
	

########################
#   Global Variables   #
########################

DEVNULL = open("/dev'null", 'w')
	
###############	
#   Classes   #
###############


class Setup():
	
	def Banner(self):
		
		'''
		This function outputs a banner to the console.
		'''
		os.system("clear")
		print"######################################################"
		print"#          ___         __       _      _  ___        #"
		print"#         / _ | __ __ / /_ ___ | | /| / // _ \       #"
		print"#        / __ |/ // // __// _ \| |/ |/ // ___/       #"
		print"#       /_/ |_|\_,_/ \__/ \___/|__/|__//_/           #"
		print"#                                                    #"
		print"######################################################"
		
		
	def CheckRoot(self):
		'''
		This procedure checks to see if the user is Root or using sudo. If they aren't, it closes gracefully.
		'''
		isRoot = os.geteuid()
		if isRoot != 0:
			print "[!] AutoWP must be run as root or sudo!"
			print "Exiting..."
			sys.exit(0)
		return
		
	

class Cmsmap():
	
	
	
	#cmd = ["python", "/opt/VulnerabilityAnalysis/cmsmap/cmsmap.py", "-t", target] #Need to add output information
	
	
	def __init__(self, folder, target):
		self.folder = folder
		self.target = target
		return
		
		
	
	
	def CheckIfAvailable(self):
		cmd = ["cmsmap", "-h"]
		isAvailable = check_output(cmd, stdout=PIPE)
		
		if isAvailable != 0:
			return false
		else:
			return true
		

	
class Wpscan():
	def __init__(self, folder):
		self.folder = folder
		return
		
	def CheckIfAvailable(self):
		
		cmd = ["wpscan", "-h"]
		isAvailable = check_output(cmd, stdout=PIPE)
		if isAvailable != 0:
			return false
		else:
			return true
		
		
	

class Scanner():

	def __init__(self, cmsmap, wpscan):
		
		self.cmsmap = Cmsmap("", "")
		self.wpscan = Wpscan("")
	

	def Scan():
		
		return
	


#class Alert():
	

def ArgumentParse():
	parser = argparse.ArgumentParser(description = 'AutoWP is an automatic WP scanner')
	parser.add_argument('-e', '--email', dest='email',default=None, type=str, help='(OPTIONAL) The email you wish to send the report to.')
	
		
	options = parser.parse_args()
	
	
	return options

def main(args):
	
	setup = Setup()
	setup.Banner()
	setup.CheckRoot()
	options = ArgumentParse()
	
	email = options.email
	
	targets = open("targets.txt", 'r').readlines()
	
	
	
	
	
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
