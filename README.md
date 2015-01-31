# dBackup
Successor to kBackup, re-written in dJango

## Useful Links
* Project Page (just the construction template): http://codemonk.github.io/dBackup
* Doxygen Docs: http://codemonk.github.io/dBackup/docs

## Installing Django Under Windows
* Install Python (we'll test with 2.7 and 3.latest) from here: http://python.org/download/
* Install setuptools: http://pypi.python.org/pypi/setuptools
	* Download ez_setyp.py
	* As Administratory: python ez_setup.py
* Install pip (was already installed for me by setuptools)
* Install django: pip install django
* Test django: django-admin
* If test does not work, check python bindings:

        C:\> assoc .py
        (should be Python)
        C:\> ftype Python
        (check that it's grabbing the right python, otherwise set)
        C:\> ftype Python="c:\Python27\python.exe" "%1" %*

