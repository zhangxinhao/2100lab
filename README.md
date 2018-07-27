## Feodora28 Python37 Environment

### Before Use
1. Install VirtualBox platform packages(Be aware of the operating system type and platform):
    - https://www.virtualbox.org/wiki/Downloads

   (You may need VirtualBox Extension Pack. Please install it according to your actual needs.)

2. Install Vagrant(Be aware of the operating system type and platform)
    - https://www.vagrantup.com/downloads.html

3. You may need to install `vagrant-vbguest` if you are on some Microsoft Windows system.

    ```
    vagrant plugin install vagrant-vbguest
    ```

### Usage

Now it is time for you to use our Environment.

Follow the commands below.

```
git clone https://se.jisuanke.com/course/fedora28-python37.git
cd fedora28-python37
vagrant plugin install vagrant-vbguest
vagrant up
vagrant ssh
```
