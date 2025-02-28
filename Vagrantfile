# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

    config.vm.box = "debian/bookworm64"
  
    config.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = 2048
    end
    
      config.ssh.insert_key = false
    
      config.vm.provision "shell", inline: <<-SHELL
          # Installation de base
          echo "deb http://deb.debian.org/debian/ bookworm main contrib non-free" >> /etc/apt/sources.list
          echo "deb-src http://deb.debian.org/debian/ bookworm main contrib non-free" >> /etc/apt/sources.list
          apt-get update -yq
          apt-get upgrade -yq
          apt-get install -yq curl vim tree
          # Installation de pip
          apt-get install -yq pip
          # Installation de docker
          apt-get install -yq curl vim tree docker.io docker-compose
          # installation de terraform
          wget -O - https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
          echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list
          apt -yq update && apt -yq install terraform
  
      SHELL
  
  end
  
    