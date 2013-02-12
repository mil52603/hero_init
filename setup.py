"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['src/hero_init/__main__.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    name="hero_init",
    version="0.1",
    url="https://github.com/cgranade/hero_init",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    packages=['hero_init', 'hero_init.ui'],
    package_dir={'': 'src'},
    package_data={'hero_init': [
        '_static/*.html',
        '_static/bootstrap/css/*.css',
        '_static/bootstrap/img/*.png',
        '_static/bootstrap/js/*.js',
    ]}
)