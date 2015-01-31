"""@package docstring
Produce a list of files.

This module will accept regular expressions, and a list of root
directories, and will produce a list of files.


"""

import os
import re


class FileList():
	"""
	Produce a list of files, from specified roots and include / exclude lists
	"""

	def __init__(self, directories=[], exclude_regexps=[]):
		""" Constructor """
		self.directories = directories
		self.exclude_regexps = self.__preCompile(exclude_regexps)

	def __preCompile(self, regexps):
		""" Precompile our list of regular expressions for speed later"""
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
