#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import run, put, env, local
import datetime
from os.path import exists

env.user = "ubuntu"
env.hosts = ['54.166.92.138', '54.198.185.75']


def do_pack():
    """comment"""
    try:
        time = datetime.datetime.now()
        date = time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(date))
        return("versions/web_static_{}.tgz".format(date))
    except exception:
        return None


def do_deploy(archive_path):
    """Comment"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[1]
        filename_no_extension = filename.split(".")[0]
        file_path = "/data/web_static/releases/" + filename_no_extension + "/"
        run("mkdir -p " + file_path)
        run("tar -xzf /tmp/" + filename + " -C " + file_path)
        run("mv " + file_path + "web_static/*" + " " + file_path)
        run("rm /tmp/{}".format(filename))
        run("rm -rf " + file_path + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + file_path + " /data/web_static/current")
        print("New version deployed!")
        return True

    except Exception:
        return False


def deploy():
    """comment"""
    path = do_pack()
    if exists(path):
        return do_deploy(path)
    else:
        return False
