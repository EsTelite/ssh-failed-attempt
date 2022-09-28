Vagrant.configure("2") do |config|
  config.vm.define "alphasrv" do |alphasrv|
    alphasrv.vm.box = "ubuntu/focal64"
    alphasrv.vm.network "private_network", ip: "192.168.241.13",
    name: "VirtualBox Host-Only Ethernet Adapter #4"
    alphasrv.vm.hostname = "alphasrv"
    alphasrv.vm.provision "shell",
    inline: "sudo snap install task --classic && cd /vagrant/producer && task install-all"
    alphasrv.vm.boot_timeout = 600
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end
  end
  config.vm.define "alphaclient" do |alphaclient|
    alphaclient.vm.box = "ubuntu/focal64"
    alphaclient.vm.network "private_network", ip: "192.168.241.15",
    name: "VirtualBox Host-Only Ethernet Adapter #4"
    alphaclient.vm.hostname = "alphaclient"
    alphaclient.vm.provision "shell",
    inline: "sudo snap install task --classic && cd /vagrant/producer && task install-dependencies && task setup-event-util && task start-client-watcher"
    alphaclient.vm.boot_timeout = 600
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end
  end
end
