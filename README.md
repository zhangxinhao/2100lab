## Feodora27 Python37 Environment

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
