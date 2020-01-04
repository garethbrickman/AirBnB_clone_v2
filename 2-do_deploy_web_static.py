#!/usr/bin/python3
""" Fabric script deploys .tgz archive to servers
"""
import os
from pathlib import Path
from fabric.api import *


def do_deploy(archive_path):
    """ Uploads archive to /tmp/, uncompresses, cleans up
    """
    env.user = 'ubuntu'
    env.hosts = [
        '35.243.219.137',
        '35.237.245.133'
        ]
    filename, file_extension = os.path.splitext(archive_path)
    p = Path(archive_path)
    try:
        put("archive_path", "/tmp")
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(p.name, filename))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
    except:
        return False
    else:
        return True
