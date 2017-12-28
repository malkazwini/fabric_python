""" This is fab file help to install docker on CentOS and Ubuntu Machines"""

from fabric.api import sudo , env, roles, execute , put, run, local, prompt, cd, parallel

import os

# define groups of webservers 
env.roledefs = {
	"remote_server": [ "IP HERE" ]
}

env.roledefs["all"] = [h for r in env.roledefs.values() for h in r]

# define the packages needed
packages = {
	"remote_server": [ "docker", "docker-compose"]
}

def install_dockerYUM():
	#install docker
	sudo("yum -y install %s" %" ".join(packages["remote_server"]),pty=True)
def install_dockerAPT():
        #install docker 
        sudo("apt-get -y install %s" %" ".join(packages["remote_server"]),pty=True)

def UpdateServerAPT():
	sudo("apt-get -y update", pty=True)
def UpdateServerYUM():
	sudo("yum -y update", pty=True)
@roles("all")
def deployYUM():
	#call the functions above
	execute (UpdateServerYUM)
	execute (install_dockerYUM)
	print "Docker on CentOS Ready"
def deployAPT():
	#call apt installer
	execute (UpdateServerAPT)
	execute (install_dockerAPT)
	print "Docker on Ubuntu Ready"
