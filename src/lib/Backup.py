"""@package docstring
Our main Backup Class

This module will do most backup related tasks.


"""

import os, platform
import ctypes

from FileList import FileList

class Backup():
	"""
	Will read it's configuration from *somewhere*.

	Will create a FileList based on entries in the configuration.

	Has routines to create a backup at the destination (from the
		configuration)
	"""

	def __init__(self, config={}):
		""" 
		Constructor 
		@param[in] config     Will be *something*.  For now, just a dict.
		"""
		## Store our config (or load it?)
		self.config = config

		## Our file list, created from the configuration
		self.FileList = FileList( directories = self.config['directories'],
			exclude_regexps = self.config['exclude_regexps']);

		## This will be a class soon, so it can handle removeable media.
		# For now, it's just a directory.
		self.Destination = self.config['destination']

		## Copy of our files to backup
		self.FilesToBackup = None

	def __scanSources(self):
		""" 
		Scan our file list and grab a reference to the source files,
		so that they could be displayed later.

		@param[in] self.FileList - Our file list.
		@param[out] self.FilestoBackup - for review, and passing to manifest
		"""
		self.FilesToBackup = self.FileList.getFiles()


	def __checkDestination(self):
		"""
		Check that destination is writeable by createing and then deleting
		a file.  Failures WILL throw exceptions.

		Check free space on destination, and store it.

		@returns self.DestinationSpace
		"""
		# Create a quick file on the destination drive, the delete it

		## TempFile to use
		tmpFile = os.path.join(self.Destination, "django.tmp")
		open(tmpFile,"w").write("testing write")
		os.remove(tmpFile)

		# And, check our space
		self.DestinationSpace = self.__getFreeSpaceMb()

		print "DEBUG: {} has {}Mb free".format(self.Destination,
			self.DestinationSpace)

	def __getFreeSpaceMb(self):
		""" Return folder free space in Mb """

		if platform.system() == "Windows":
			#yeuch
			free_bytes = ctypes.c_ulonglong(0)
			ctypes.windll.kernel32.GetDiskFreeSpaceExW(
				ctypes.c_wchar_p(self.Destination), None,
				None, ctypes.pointer(free_bytes))
			return free_bytes.value /1024/1024
		else:
			st = os.statvfs(self.Destination)
			return st.f_bavail * st.f_frsize/1024/1024

	def Backup(self):
		## Do simple backup -- probably just for testing.

		self.__checkDestination()
		self.__scanSources()