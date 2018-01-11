#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
sample code.
"""

import os
import glob
from mbglob.MbGlob import MbGlob as mbglob


def main(pathname):
    print(pure_glob(pathname))
    print(use_mbglob(pathname))


def pure_glob(pathname):
    return glob.glob(pathname)


def use_mbglob(pathname):
    return mbglob().glob(pathname)


if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = os.path.join(root_dir, "demo_tree")
    search_string = 'ぱいそん*'

    main(os.path.join(base_dir, search_string))
