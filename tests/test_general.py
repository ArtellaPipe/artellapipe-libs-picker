#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for artellapipe-libs-maya
"""

import pytest

from artellapipe.libs.picker import __version__


def test_version():
    assert __version__.get_version()
