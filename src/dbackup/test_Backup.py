"""@package docstring
Unittests for Backup.py

Unittests for main Backup class

"""
import unittest

from Backup import Backup

class TestBackup(unittest.TestCase):

	def test_CheckBackupToParent(self):
		""" 
		UnitTest: Check a backup of the test dir to it's parent dir.
		"""

		config={'destination':'..',
			'directories':['.'],
			'exclude_regexps':[]}

		b=Backup(config)
		b.Backup()


if __name__ == '__main__':
	unittest.main()
