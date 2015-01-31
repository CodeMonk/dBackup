"""@package docstring
Unittests for FileList.py

Unittests for File List

"""
import unittest
import os

from FileList import FileList

class TestFileList(unittest.TestCase):

	def test_DirectoriesEmpty(self):
		""" 
		UnitTest: Make sure directories are empty on empty constructor
		"""

		# Check Empty
		fl=FileList()
		self.assertTrue(len(fl.directories) == 0)

	def test_DirectoriesMatch(self):
		""" 
		Unittest: Make sure directories passed into constructor are set 
		"""
		# Check that it matches
		directories = ['a', 'b', 'c']

		fl = FileList(directories=directories)
		self.assertEqual(directories, fl.directories)

	def test_fileSearch(self):
		"""
		Unittest: Do some searches on the local directory -- this will fail if
		files are added or deleted.

		This test does several tests on a file list generated from this directory.
		"""

		# Find python files (2) (minus pyc)
		# Find all files >= python files.

		allFL=FileList(directories=['.'])
		noPycFL=FileList(directories=['.'], exclude_regexps=[r'\.pyc$'])

		allFiles=allFL.getFiles()
		noPycFiles=noPycFL.getFiles()

		# We should have two non .pyc files
		self.assertEqual(len(noPycFiles), 2)
		# We could have some pyc files
		self.assertTrue(len(noPycFiles) <= len(allFiles))

		# Make sure our Module and test were found.
		self.assertIn(os.path.join('.', 'FileList.py'), allFiles)
		self.assertIn(os.path.join('.','test_FileList.py'),allFiles)
		self.assertIn(os.path.join('.', 'FileList.py'), noPycFiles)
		self.assertIn(os.path.join('.','test_FileList.py'),noPycFiles)




if __name__ == '__main__':
	unittest.main()
	# import os, re

	# # Let's create some file lists
	# print "All Files:"
	# fl=FileList(directories=['.'])
	# print fl.getFiles()

	# print "\nMinus .pyc"
	# fl=FileList(directories=['.'], exclude_regexps=[r'\.pyc$'])
	# print fl.getFiles()

	# sep=re.escape(os.sep)
	# test_exp = "{sep}test_[^{sep}]*$".format(sep=sep)
	# print "\nMinus tests (re={})".format(test_exp)
	# fl=FileList(directories=['.'], exclude_regexps=[test_exp])
	# print fl.getFiles()

	# print "\n/tmp"
	# fl=FileList(directories=['/tmp'])
	# print fl.getFiles()

		
