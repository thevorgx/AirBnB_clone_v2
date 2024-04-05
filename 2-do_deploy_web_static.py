#!/usr/bin/python3
"""Distributes an archive to web servers using fabric"""

from fabric.api import env, put, run
from os import path


env.user = 'ubuntu'
env.hosts = ['18.206.198.128', '107.23.109.180']


def do_deploy(archive_path):
    """distributes an archive to web servers."""

    if not path.exists(archive_path):
        return False

    put(archive_path, '/tmp')

    filename = path.basename(archive_path)
    filename_no_extension = filename.split('.')[0]

    run(f"mkdir -p /data/web_static/releases/{filename_no_extension}")
    run(f"tar -xzf /tmp/{filename} -C /data/web_static/releases/{filename_no_extension}/")

    run(f"rm /tmp/{filename}")

    run('rm -rf /data/web_static/current')

    run(f"ln -s /data/web_static/releases/{filename_no_extension}/ /data/web_static/current")

    return True
