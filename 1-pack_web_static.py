#!/usr/bin/python3
""" Fabric script that generates archive."""

from fabric.api import local
from datetime import datetime as dt
from os import makedirs


def do_pack():
    """ Function that archive """

    ArchName = "versions/web_static_{}".format(
            dt.now().strftime("%Y%m%d%H%M%S"))
    makedirs('versions', exist_ok=True)

    ret = local("tar -cvzf {} web_static".format(ArchName))
    if ret.succeeded:
        return ret.command.split(" ")[2]
