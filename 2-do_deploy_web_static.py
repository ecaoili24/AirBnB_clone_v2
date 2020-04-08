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
    root = os.path.splitext(basename)
    target = "/data/web_static/releases/".format(root)
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(target))
        run('tar -xzf /tmp/{} -C {}{}/'.format(path, target))
        run('rm /tmp/{}'.format(path))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(target, target))
        run('rm -rf {}{}/web_static'.format(target))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(target))
    except:
        return False
    else:
        return True
