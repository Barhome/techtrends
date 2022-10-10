# set up the default terminal
ENV["TERM"]="linux"

Vagrant.configure("2") do |config|
  
  # set the image for the vagrant box
  config.vm.box = "opensuse/Leap-15.2.x86_64"
  ## Set the image version
  # config.vm.box_version = "15.2.31.247"

  # st the static IP for the vagrant box
  config.vm.network "private_network", ip: "192.168.56.4"
  
  # consifure the parameters for VirtualBox provider
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 4
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
  end
  config.vm.define "master" do |master|
    master.vm.box = "opensuse/Leap-15.2.x86_64"
    master.vm.hostname = "master"
    master.vm.network 'private_network', ip: "192.168.0.200",  virtualbox__intnet: true
    master.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh", disabled: true
    master.vm.network "forwarded_port", guest: 22, host: 2000 # Master Node SSH
    master.vm.network "forwarded_port", guest: 6443, host: 6443 # API Access
    for p in 30000..30100 # expose NodePort IP's
      master.vm.network "forwarded_port", guest: p, host: p, protocol: "tcp"
      end
    master.vm.provider "virtualbox" do |v|
      v.memory = "3072"
      v.name = "master"
      end
    master.vm.provision "shell", inline: <<-SHELL
      sudo zypper refresh
      sudo zypper --non-interactive install bzip2
      sudo zypper --non-interactive install etcd
      sudo zypper --non-interactive install apparmor-parser
      curl -sfL https://get.k3s.io | sh -
    SHELL
  end
end
