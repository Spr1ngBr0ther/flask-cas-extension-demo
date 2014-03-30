#!/usr/bin/env python2
#Copyright (C) 2014, Cameron Brandon White
# -*- coding: utf-8 -*-
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="flask-cas-demo",
        version="0.1.0",
        description="A simple flask app to demo CAS login",
        author="Cameron Brandon White",
        author_email="cameronbwhite90@gmail.com",
        install_requires = [
            "flask",
            "flask-bootstrap",
            "gunicorn",
        ],
        include_package_data=True,
    )
