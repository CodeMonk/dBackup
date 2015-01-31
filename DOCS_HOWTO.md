
To generate docs:

1. Run doxygen
2. Move docs out of the way:  $ mv docs ..
3. update branch to gh-pages:
   $ git checkout gh-pages
   $ git pull origin gh-pages
4. Update all files in the docs directory with stuff from html:
   $ rm -rf docs/*
   $ cp -a ../docs/html/* docs
   $ git add docs
5. Make sure stuff looks good:
   $ git status
6. Push:
   $ git push origin gh-pages
7. Go back to main branch and clean up:
   $ git checkout master
   $ rm -rf docs
   $ git status


