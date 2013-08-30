dmenu-i3
========

Get focus on your active x window clients using dmenu in i3!

Installation
===


```shell
git clone https://github.com/xiwenc/dmenu-i3.git


# Example: Install the executables
cd dmenu-i3
cloned_dir=$(pwd)

cd ~/bin/
for i in recall.py list-client.py dmenu-i3; do
    ln -s $cloned_dir/$i
done
```

Bind *dmenu-i3* to a key combination in your i3 config
