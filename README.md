# Steganography tool
Software for concealing information (text, image) in an image.

## 📚 Requirements :
- [Python 3 with Tkinter](https://www.python.org/download/releases/3.0/)

- Python Imaging Library (PIL)
> If you don’t have pip (a very useful tool), install it using :
> ```sh
> $ sudo apt-get install python-pip
> ```

> With pip installed, install the required development packages:
> ```sh
> $ sudo apt-get install python-dev libjpeg-dev libfreetype6-dev zlib1g-dev
> ```

>Once you install these packages, we have to symlink the three image libraries into /usr/lib. Wait, now what is “symlink”? A symlink, which is short for symbolic link, is a special type of file that contains a reference to another file or directory. The reference is in the form of an absolute or relative path and it affects path-name resolution. To do that, type in the following commands on the terminal :
> ```sh
> $ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
> $ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
> $ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
> ```

Now we are ready to install PIL. Type the following :
```sh
$ sudo pip install pil
```

To install Pillow (recommended), type the following :
```sh
$ sudo pip install Pillow
```

## 📥 Installation
```sh
$ git clone https://github.com/TwistAtom/Steganography.git
```

## 🚀 Launch
```sh
$ cd Steganography
$ python3 Interface.py
```



