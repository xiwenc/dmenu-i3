dmenu-i3
========

Get focus on your active x window clients using dmenu in i3!

Having trouble finding windows on in your awesome i3 setup? Look no further.
dmenu-i3 enables you to search through your pile of clients across workspaces
with the familiar dmenu interface.


Installation
===

```shell
git clone https://github.com/xiwenc/dmenu-i3.git


# Example: Install the executable by creating a symlink
ln -s /path/to/dmenu-i3 ~/bin/dmenu-i3
```

Usage
===

```shell
dmenu-i3 --help
usage: dmenu-i3 [-h] [--show-all] [--window-class]

dmenu for active windows

optional arguments:
  -h, --help      show this help message and exit
  --show-all      Show all type of nodes including docks etc
  --window-class  Render window classes
```

Bind *dmenu-i3* to a key combination in your i3 config, mine is:
```
bindsym $mod+Shift+d exec dmenu-i3 --window-class
```


Credits
===

Ziberna for writing i3.py located at https://github.com/ziberna/i3-py
