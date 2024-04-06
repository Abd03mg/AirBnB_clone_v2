#!/usr/bin/python3
""" Full deployment"""

from fabric.api import *
from datetime import datetime as dt
from os import makedirs
from os.path import exists


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
        return True
    except Exception:
        return False


def deploy():
    """function that calls de_deply and so_pack"""
    try:
        an = do_pack()

        if not an:
            return False
        ret = do_deploy(an)
        return ret
    except Exception:
        return False
