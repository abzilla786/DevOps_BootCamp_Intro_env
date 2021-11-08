Vagrant.configure("2") do |config|

 config.vm.box = "ubuntu/bionic64"
# creating a virtual machine ubuntu 

  config.vm.network "forwarded_port", guest: 80, host: 8080,
    auto_correct: true

# assign private ip to our VM
 config.vm.network "private_network", ip: "192.168.10.100"   

 # Ensure to install hostsupdater plugin on our localhost before rerunning the vagrant
 config.hostsupdater.aliases = ["development.local"]

# sync folder from os to vm
            # "." means current location - into / inside our vm
 config.vm.synced_folder ".", "home/vagrant/app"
  

end
