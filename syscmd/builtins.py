# -*- coding: utf-8 -*-
import os

__all__ = [
    "cd",
]

def cd(path):
    os.chdir(path)
