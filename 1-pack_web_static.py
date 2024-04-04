#!/usr/bin/python3
"""generate a .tgz archive from the contents of the web_static folder"""

from fabric.api import local
from datetime import datetime
from os import path, makedirs


def do_pack():
    """generate a .tgz archive from the contents of the web_static folder"""
    if not path.exists("versions"):
        makedirs("versions")

    creation_time = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_archive_name = "web_static_{}.tgz".format(creation_time)
    tgz_archive_path = path.join("versions", tgz_archive_name)
    make_tgz = local("tar -cvzf {} web_static".format(tgz_archive_path))

    if make_tgz.succeeded:
        return (tgz_archive_path)
    else:
        return (None)
