#!/usr/bin/python3
""" Full deployment"""
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


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
