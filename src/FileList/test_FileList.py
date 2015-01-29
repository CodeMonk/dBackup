"""@package docstring
Unittests for FileList.py

Unittests for File List

"""
import unittest

from FileList import FileList

class TestFileList(unittest.TestCase):

	def test_DirectoriesEmpty(self):
		""" Make sure directories are empty on empty constructor"""

		# Check Empty
		fl=FileList()
		self.assertTrue(len(fl.directories) == 0)

	def test_DirectoriesMatch(self):
		""" Make sure directories passed into constructor are set """
		# Check that it matches
		directories = ['a', 'b', 'c']

		fl = FileList(directories=directories)
		self.assertEqual(directories, fl.directories)


if __name__ == '__main__':
	unittest.main()

		
