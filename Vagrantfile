# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "fedora/28-cloud-base"
  config.vm.box_url = "https://mirrors.tuna.tsinghua.edu.cn/fedora/releases/28/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-28-1.1.x86_64.vagrant-virtualbox.box"
  config.vm.box_download_checksum = "81b970a4852edee2d532a1ddbab0a8c6c912e2636423193196f1586e0b30949b"
  config.vm.box_download_checksum_type = :sha256

  config.vm.network "private_network", ip: "192.168.55.33"
  config.vm.synced_folder ".", "/vagrant", create: true, nfs: true
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    dnf install -y git redhat-rpm-config

    type -fp python3.7 &>/dev/null || (
      dnf install -y python37
      python3.7 -mensurepip
    )

    type -fp mysql &>/dev/null || (
      dnf install -y mariadb-server mariadb-devel
      systemctl enable mariadb
      systemctl start mariadb
      mysqladmin -u root password vagrant
    )

    [[ -f /etc/pip.conf ]] || cat > /etc/pip.conf <<'EOF'
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
EOF

    pip3.7 install ipython bpython
  SHELL
end
