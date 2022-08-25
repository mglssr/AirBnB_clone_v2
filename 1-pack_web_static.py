#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
contents of the web_static."""

from fabric.api import local
import datetime


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
