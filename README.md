## How to modify pages

1. $ bash
2. $ workon pelican (sets up python virtualenv)
3. modify files in content/
4. $ make rsync_upload


## Theme
 - used modified **notmyidea-cms** theme
 - default location in *virtualenv* directory ~/.virtualenvs/pelican/lib/python2.7/site-packages/pelican/themes/ symlinked to ./modified pelican-themes
 - my modifications are hosted on  <https://github.com/palmstrom/pelican-themes/commits/master>

### Modify Theme
edit in ./modified pelican-themes/notmyidea-cms

	# try it
	$ make rsync_upload
	# commit modifications
	$ cd ./modified pelican-themes/
	$ git commit -a
	$ git push origin master
	
### Sync Modified Themes with Upstream
<https://help.github.com/articles/fork-a-repo#pull-in-upstream-changes>

## Instalation
    $ sudo yum install python-virtualenvwrapper
    $ mkvirtualenv pelican
    $ pip install pelican
    $ pip install Markdown
    $ pip install typogrify
