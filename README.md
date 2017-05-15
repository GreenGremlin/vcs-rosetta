# VCS Rosetta
A handy tool to help devs transition between version control systems.

Prints out the equivalent command in the other VCS.

## Installation
``` shell
pip install --user git+git://github.com/GreenGremlin/vcs-rosetta.git
```

## Usage
### g2h (git to hg)
``` shell
$ g2h checkout

git checkout:
=============
Translates as:
    git checkout [file]                                       => hg revert [file]
    git checkout HEAD                                         => hg update tip
    git checkout `git rev-list -n 1 --before="[date]" master` => hg update --date [date]
    git checkout -f                                           => hg update -C
    git checkout [branch]                                     => hg update [branch]
```

### h2g (hg to git)
``` shell
$ h2g update

hg update:
==========
Translates as:
    hg update --date=[date] => git checkout `git rev-list -n 1 --before="[date]" master`
```
