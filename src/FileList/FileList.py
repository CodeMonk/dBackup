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
		self.directories = directories
		self.exclude_regexps = self.__preCompile(exclude_regexps)

	def __preCompile(self, regexps):
		""" 
		Precompile our list of regular expressions for speed later
		@param[in] regexps  - our list of regular expressions
		@returns a list of compiled regular expressions
		"""
		result = []
		for regexp in regexps:
			result.append(re.compile(regexp))

		return result

	def __getFilesFromDirectory(self, dir):
		"""
		Recursively return all files from the Directory
		"""
		files=[]
		for root, dirnames, filenames in os.walk(dir):
			for filename in filenames:
				files.append(os.path.join(root,filename))
		return files

	def __matchesAny(self, string, regexps):
		"""
		Return true if string matches any of the regexps
		"""
		for reg in regexps:
			if reg.search(string):
				return True
		return False

	def __scrubFiles(self, files, excludes):
		"""
		Remove any files from list that match excludes, and return the
		scrubbed array.
		"""

		result=[]

		for file in files:
			if not self.__matchesAny(file, excludes):
				result.append(file)

		return result


	def getFiles(self):
		""" Return an array of the files found matching our parameters """
		self.files=[]
		for dir in self.directories:
			dir_files = self.__getFilesFromDirectory(dir)
			self.files += self.__scrubFiles(dir_files, self.exclude_regexps)

		return self.files
