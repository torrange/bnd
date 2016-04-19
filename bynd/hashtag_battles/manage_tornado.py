#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hashtag_battles.settings")
    from subprocess import call
    call(["python2", "test.py"])

