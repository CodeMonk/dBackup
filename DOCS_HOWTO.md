
To generate docs:

1. Run doxygen
2. update branch to gh-pages:
 $ git checkout gh-pages
 $ git pull origin gh-pages
3. Update all files in the docs directory with stuff from html:
 $ rm -rf docs
 $ mv ../docs/html docs
 $ git add docs
4. Make sure stuff looks good and commit:
 $ git status
 $ git commit
5. Push:
 $ git push origin gh-pages
6. Go back to main branch and clean up:
 $ git checkout master
 $ git status


