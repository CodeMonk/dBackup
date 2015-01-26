# Design Spec
Well . . maybe not a full spec, but . . .

## Phase 1 dBackup Specs
* Leverage afio for destination file(s) - if possible.  Windows doesn't have afio, so, we may need to re-implement afio in python.
* Support splititng backup files by size.
* Have include and exclude lists with regular expressions.
	* Have test modes that generate file lists based on include and exclue for testing backup sets.
* Use Web GUI front end.
	* Likely implemented with dJango
* Backup to any destination supported on host machine:
	* Mounted Drive / Directory
	* CD / DVD_ROM
* Ability to Restore w/o previous knowledge of backup.
	* Contents of backup will contain enough information to restore into another directory.
* Support any filename supported by Operating system.  (i.e. handle files / directories with spaces)
* Handle IFS correctly (/ vs \\) in directory structure for both restore and backup.

## Phase 2 dBackup Specs
* Handle backups from multiple machines from one front end.
* Scheduling
* Detailed backup / restore reporting

## kBackup Specs
* Archive format and compression method as well as other parameters get detected automatically during restore or verify operation. You do not need to know how you created the archive, KBACKUP will find it out for you.
* You can use gzip(1) or compress(1) to compress your archives.
* If you have some sensitive data, you can use pgp(1) (Pretty Good Privacy) to compress and encrypt your archives using public key encryption. (Ever wanted to send a tape or disk of sensitive data to someone else? Now you can!) 3.2
* You can schedule backup or restore operations to be executed at a later time or even regularly. KBACKUP supports full at(1) functionality.
* KBACKUP can use double buffering to keep your tape drive streaming continuously even on slow or heavily loaded machines. No longer corrupt your tapes by starting and stopping the drive every few seconds.
* You can keep lists of files and directories that you want to exclude from backups. You can also include and/or exclude files by using standard shell patterns.
* You have the choice between full or incremental backups.
* You can keep different configuration files for your backup tasks. Sample configurations files for backups to tape or floppy disk are included. No manual configuration file editing, just go through the menus and change whatever you like.
* support for accessing remote devices for easy support of LAN backups.
* Tape Drive Support
	* When using tapes or mountable block devices (see section 8.2.3), a complete directory of all files in the archive gets stored at the beginning of the archive. You no longer need to read all the long archive to find out what files it contains.
	* Each archive on a tape is preceded by a header containing option settings, parameters, compress*ion format, date, backup type, etc. This maintains compatibility across different versions of this software and, as it is stored in readable format, helps you restore the data manually if you cannot use KBACKUP for what reason ever 3.1.
	* KBACKUP supports tapes, floppy-drives and removable media like removable hard-drives, magneto-optical drives or others.
	* Reliably handle multi-volume archives. There is no limit for your archives' sizes. By using the MULTIBUF program, KBACKUP automatically detects the length of your tapes.
	* The same MULTIBUF program is capable of performing any operation on the end of a tape, like e.g. telling an automatic loading mechanism to change tapes.
