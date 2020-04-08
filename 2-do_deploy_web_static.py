#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""
import os.path
from fabric.api import *
from fabric.contrib import files

env.user = "ubuntu"
env.hosts = ['34.74.200.157', '107.20.131.122']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not os.path.isfile(archive_path):
        return False
    basename = path = os.path.basename(archive_path)
    root, ext = os.path.splitext(basename)
    target = '/data/web_static/releases/{}'.format(root)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(target))
        run("sudo tar -xzf /tmp/{} -C {}/".format(path, target))
        run("sudo rm /tmp/{}".format(path))
        run("sudo mv {}/web_static/* {}/".format(target, target))
        run("sudo rm -rf {}/web_static".format(target))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target))
        print('New version deployed!')
    except:
        return False
    else:
        return True
