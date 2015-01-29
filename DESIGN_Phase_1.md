Design - Phase 1
==============

Goals
-----

* Implement settings 
* Get a list of files, based on regular expressions in settings.
* Create a manifest in a portable format to store at the destination.
* Destination is a mounted directory somewehre.
* Store backup data in the destionation
* Fully document all code and classes.
	* Use Sphinx for docs.
* All code must have unit tests


### Backup Specifics

* Backup Format: 
	* We need at least two things here:
		* Blob containing the backup
		* Manifest - JSON
	* I'm hesitatant to use ZIP, as the compression will be for the whole archive, which will make it hard to easily grab the manifest.
	* The blob with the backup needs to be in a format that can be split across devices.  Preferably in a format where a single pieceof a split file can be restored.

### Restore Specifics
* List backups stored in database
* Ability to restore from backup created elsewhere (from the blob)
* Ability to restore from backup in database

### Django Specifics

* Need a settings configuration specifics.
* How to create some kind of progress bar for scanning for files.
* How to create some kind of progress bar for doing backup.
* Need to be able to disconnect and reconnect to check on status of running backup and/or restore.  (with progress)

Old Phase One Design
===========
(moved from DESIGN.md)

* Leverage afio for destination file(s) - if possible.  Windows doesn't have afio, so, we may need to re-implement afio in python.
* Support splititng backup files by size.
* Have include and exclude lists with regular expressions.
	* Have test modes that generate file lists based on include and exclue for testing backup sets.
* Use Web GUI front end.
	* Likely implemented with dJango
* Backup to any destination supported on host machine:
	* Mounted Drive / Directory
	* CD / DVD_ROM -- NEXT PHASE
* Ability to Restore w/o previous knowledge of backup.
	* Contents of backup will contain enough information to restore into another directory.
* Support any filename supported by Operating system.  (i.e. handle files / directories with spaces)
* Handle IFS correctly (/ vs \\) in directory structure for both restore and backup.
