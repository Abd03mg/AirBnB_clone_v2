#!/usr/bin/python3
""" Fabric script that generates archive."""

from fabric.api import *
from datetime import datetime as dt
from os import makedirs
from os.path import exists as ex


env.user = "ubuntu"
env.hosts = ['18.209.179.152', '3.86.13.133']


def do_pack():
    """ Function that archive """

    try:
        ArchName = "versions/web_static_{}.tgz".format(
                dt.now().strftime("%Y%m%d%H%M%S"))
        makedirs('versions', exist_ok=True)

        ret = local("tar -cvzf {} web_static".format(ArchName))
        if ret.succeeded:
            return ret.command.split(" ")[2]
        else:
            return None
    except Exception:
        return None


def do_deploy(arch):
    """function that distributes
    an archive to your web servers"""

    ArName = arch.split("/")[-1][0:-4]
    dest = "/data/web_static/releases/"
    if (not ex(arch)):
        return False
    put(arch, "/tmp/")
    res = run("mkdir -p {dest}{ArName}/ ;"
              "tar -xzf /tmp/{arch} -C {dest}{ArName}/ ;"
              "mv {dest}{ArName}/web_static/* {dest}{ArName}/ ;"
              "rm -rf {dest}{ArName}/web_static;"
              "rm -rf /data/web_static/current;"
              "ln -s {dest}{ArName}/ /data/web_static/current".format(
                  dest, ArNaem, arch, dest, ArName, dest, ArName,
                  dest, ArName, dest, ArName, dest, ArName))

    return False if res.failed else True
