# ssh-failed-attempt

## Dependencies
You need to install `Vagrant` and `VirtualBox`, need to add some new interface with IP specified in `Vagrantfile`

## Bring up Env
To bring the environment you just need to run `vagrant up` and for redeploy/re-run just run `vagrant provision`.
There will be stuck in final of client deployment, so need to bring up again if you send the exit signal, you can use `vagrant provision`.

For ssh or going to vagrant box you can open a new terminal and run `vagrant ssh <boxname>`.
