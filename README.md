## Feodora27 Python37 Environment

This introduction is provided by Haoran Yu (俞昊然).
If you cannot understand any part of this file, please contact the author(yuhaoran@jisuanke.com) as soon as possible.

### Before Use
1. Install VirtualBox platform packages(Be aware of the operating system type and platform):
    - https://www.virtualbox.org/wiki/Downloads
    - You may need VirtualBox Extension Pack. Please install it according to your actual needs.

2. Install Vagrant(Be aware of the operating system type and platform)
    - https://www.vagrantup.com/downloads.html

3. You may install `vagrant-vbguest`.

    ```
    vagrant plugin install vagrant-vbguest
    ```

### Usage

Now it is time for you to use our Environment.

Follow the commands below.

```
git clone https://se.jisuanke.com/course/fedora27-python37.git
cd fedora27-python37
vagrant plugin install vagrant-vbguest
vagrant up
vagrant ssh
```

If you see any feedback that looks like

```
Operation timed out after 30002 milliseconds with 0 out of 0 bytes received
```

and lead you to something like

```
The SSH command responded with a non-zero exit status
```

then you should find a better network environment and execute

```
vagrant destroy
```

Entry `y` then

```
vagrant up --provision
```

### Test whether it is done

#### Test 1

Within the root folder where `Vagrantfile` locates, create a new file. Let us call it `TESTFILE`. You can do it by using

```
touch TESTFILE
```

Then you should

```
vagrant ssh
```

to get into the virtual machine and see

```
[vagrant@localhost ~]
```

Now you can switch into some folder `/vagrant` by using

```
cd /vagrant
```

Then check whether `TESTFILE` is synced or not by using

```
ls -l
```

You should then get something similar to the following

```
total 8
-rwxr-xr-x. 1 501 games 1803 Jul 27 05:41 README.md
-rw-rw-r--. 1 501 games    0 Jul 27 05:44 TESTFILE
-rwxr-xr-x. 1 501 games 1484 Jul 27 05:27 Vagrantfile
```

If so, do not forget to remove the `TESTFILE` since this test is passed and the `TESTFILE` is no more useful.

#### Test 2

Type in `python` or `python3` or `python3.7` you should get

```
Python 3.7.0 (default, Jun 28 2018, 08:59:52)
[GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

#### Test 3

Type in `pip --version` or `pip3 --version` you should get

```
pip 18.0 from /home/vagrant/.local/lib/python3.7/site-packages/pip (python 3.7)
```

#### Extra preparation

Type in `cd ~` and then

```
git clone https://github.com/django/django.git
```

We would use it later during our lectures.


*If any test above cannot pass on your machine, contact Haoran Yu (俞昊然) on IM or though Email yuhaoran@jisuanke.com as soon as possible.*
