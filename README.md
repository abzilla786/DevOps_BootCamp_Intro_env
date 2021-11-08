# DevOps_BootCamp_Intro_env

# DevOPs Intro
 - Devops is the culture that bridges the gap between development and operations
 
 ## Life before DevOps
 - Waterfall - V model
 - Transition to Agile and Scrum
 

 ### Key Pillars of Devops
 #### Monolith Architecture
 
 Create `vagrant file` n the current location
 ```
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
```
### Create Provisions
```
#!/bin/bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
```

### Vagrant Commands
```
Common commands:
     autocomplete    manages autocomplete installation on host
     box             manages boxes: installation, removal, etc.
     cloud           manages everything related to Vagrant Cloud
     destroy         stops and deletes all traces of the vagrant machine
     global-status   outputs status Vagrant environments for this user
     halt            stops the vagrant machine
     help            shows the help for a subcommand
     hostsupdater
     init            initializes a new Vagrant environment by creating a Vagrantfile
     login
     package         packages a running vagrant environment into a box
     plugin          manages plugins: install, uninstall, update, etc.
     port            displays information about guest port mappings
     powershell      connects to machine via powershell remoting
     provision       provisions the vagrant machine
     push            deploys code in this environment to a configured destination   
     rdp             connects to machine via RDP
     reload          restarts vagrant machine, loads new Vagrantfile configuration
     resume          resume a suspended vagrant machine
     snapshot        manages snapshots: saving, restoring, etc.
     ssh             connects to machine via SSH
     ssh-config      outputs OpenSSH valid configuration to connect to the machine
     status          outputs status of the vagrant machine
     suspend         suspends the machine
     up              starts and provisions the vagrant environment
     upload          upload to machine via communicator
     validate        validates the Vagrantfile
     version         prints current and latest Vagrant version
     winrm           executes commands on a machine via WinRM
     winrm-config    outputs WinRM configuration to connect to the machine
```

 
