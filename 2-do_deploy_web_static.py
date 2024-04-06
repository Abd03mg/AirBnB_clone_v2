#!/usr/bin/python3
""" Fabric script that generates archive."""

from fabric.api import *
from os.path import exists


env.user = "ubuntu"
env.hosts = ['18.209.179.152', '3.86.13.133']


def do_deploy(arch):
    """function that distributes
    an archive to your web servers"""
    try:
        ArName = arch.split("/")[-1][0:-4]
        dest = "/data/web_static/releases/"
        if not (exists(arch)):
            return False
        put(arch, "/tmp/")
        run("mkdir -p {}{}/ ;".format(dest, ArName))
        sudo("chown -R $(id -un):$(id -gn) /data/")
        run("tar -xzf /tmp/{}.tgz -C {}{}".format(ArName, dest, ArName))
        run("rsync -a {}{}/web_static/* {}{}/".format(dest, ArName,
            dest, ArName))
        run("rm -rf {}{}/web_static;".format(dest, ArName))
        run("rm -rf /data/web_static/current;")
        run("ln -sf {}{}/ /data/web_static/current".format(dest, ArName))
    except Exception:
        return False
