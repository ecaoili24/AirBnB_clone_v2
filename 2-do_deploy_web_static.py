#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""
import os.path
from fabric.api import put, run, env
from fabric.contrib import files


env.hosts = ['34.74.200.157', '107.20.131.122']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not os.path.isfile(archive_path):
        return False
    a_file = path = os.path.a_file(archive_path)
    no_extenstion = os.path.splitext(a_file)
    path = "/data/web_static/releases/".format(no_extension)
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_extension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(a_file, path, no_extension))
        run('rm /tmp/{}'.format(a_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))
        run('rm -rf {}{}/web_static'.format(path, no_extension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))
        return True
    except:
        return False
