#!/usr/bin/python3
""" Fabric script deploys .tgz archive to servers
"""
from fabric.api import *
from fabric.contrib import files
from pathlib import Path

env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['35.243.219.137', '35.237.245.133']


def do_deploy(archive_path):
    """ Uploads archive to /tmp/, uncompresses, cleans up
    """
    p = Path(archive_path)
    f_full = p.name
    f_noext = p.stem

    if not files.exists(archive_path):
        return False

    put("archive_path", "/tmp")
    run("mkdir -p /data/web_static/releases/{}".format(f_full))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(f_full, f_noext))
    run("rm /tmp/{}".format(f_full))
    run("mv /data/web_static/releases/{}/web_static/*\
    /data/web_static/releases/{}/".format(f_noext))
    run("rm -rf /data/web_static/releases/{}/web_static".format(f_noext))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(f_noext))
