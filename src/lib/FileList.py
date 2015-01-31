"""@package docstring
Produce a list of files.

This module will accept regular expressions, and a list of root
directories, and will produce a list of files.


"""

import os
import re


class FileList():
	"""
	Creates a list of files from a list of directories and a list of
	regular expressions.  The expressions are sets of files to exclude
	from the ones found searching the directories.

	Right now, after construction, the main external function is 
	getFiles, which returns an array of the files found.
	"""

	def __init__(self, directories=[], exclude_regexps=[]):
		""" 
		Constructor 
		@param[in] directories     A list of directories to search
		@param[in] exclude_regexps A list of regexps to exclude from search
		"""
		## List of directories to search for backup files.
		self.directories = directories

		## List of compiled regular expressions to exclude 
		#  from the files found
		self.exclude_regexps = self.__preCompile(exclude_regexps)
		
		## Will contain a list of files found, after directories are 
		#  searched, and excludes processed.
		self.files = None

	def __preCompile(self, regexps):
		""" 
		Precompile our list of regular expressions for speed later
		@param[in] regexps  - our list of regular expressions
		@returns a list of compiled regular expressions
		"""
		## List that we will be returning, after compilation
		result = []
		for regexp in regexps:
			result.append(re.compile(regexp))

		return result

	def __getFilesFromDirectory(self, dir):
		"""
		Recursively search for files starting at dir,
		and return them in a list.
		@param[in] dir Directory to search
		@returns a list of files found.
		"""
		## List of files we found from the directory
		files=[]
		for root, dirnames, filenames in os.walk(dir):
			for filename in filenames:
				files.append(os.path.join(root,filename))
		return files

	def __matchesAny(self, string, regexps):
		"""
		Return true if string matches any of the regexps

		@param[in] string String to check
		@param[in] regexps List of Regular expressions to check
		@returns True if string matches any regular expression in regexps
		"""
		for reg in regexps:
			if reg.search(string):
				return True
		return False

	def __scrubFiles(self, files, excludes):
		"""
		Remove any files from list that match excludes, and return the
		scrubbed array.
		@param[in] files     List of files to check
		@param[in] excludes  List of expressions to check files against
		@returns List of files that did *not* match the excludes.
		"""

		## List of files minus the excludes.
		result=[]

		for file in files:
			if not self.__matchesAny(file, excludes):
				result.append(file)

		return result


	def getFiles(self):
		""" 
		Return an array of the files found matching our parameters 

		Uses class variables passed into the instance:
		@param[in] self.directories      List of directories to search.
		@param[in] self.exclude_regexps  List of regular expressions to exclude.
		@param[out] self.files
		@returns self.files List of files found.
		"""
		self.files=[]
		for dir in self.directories:
			dir_files = self.__getFilesFromDirectory(dir)
			self.files += self.__scrubFiles(dir_files, self.exclude_regexps)

		return self.files
