"""@package docstring
Produce a list of files.

This module will accept regular expressions, and a list of root
directories, and will produce a list of files.


"""

class FileList():
	"""
	Produce a list of files, from specified roots and include / exclude lists
	"""

	def __init__(self, directories=[], exclude_regexps=[]):
		""" Constructor """
		self.directories = directories
		self.exclude_regexps = exclude_regexps


	def getFiles(self):
		""" Return an array of the files found matching our parameters """

		return []
