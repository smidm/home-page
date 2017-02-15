## How to Update Web

1. (optional: switch to virtualenv)
2. add/modify files in content/
3. (optional: `$ ./develop_server.sh start` and check the updated web site on <http://localhost:8000/>)
4. `$ ./update_web.sh`

## Instalation
    (optional - create virtualenv: $ mkvirtualenv pelican)
    $ git clone --recursive https://github.com/smidm/home-page
    $ cd home-page
    $ pip install pelican Markdown typogrify
    
## Upgrade Pelican
    $ cd home-page
    $ pip install --upgrade pelican Markdown typogrify
