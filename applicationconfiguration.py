#!/usr/bin/env python
# Copyright (C) 2015 Brent Baude <bbaude@redhat.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super(Singleton, cls).__new__(cls)
            instance._singleton_init(*args, **kwargs)
            cls._instance = instance
        return cls._instance

    def __init__(self, *args, **kwargs):
        pass

    def _singleton_init(self, *args, **kwargs):
        """Initialize a singleton instance before it is registered."""
        pass


class ApplicationConfiguration(Singleton):
    def _singleton_init(self, parserargs=None):
        super(ApplicationConfiguration, self)._singleton_init()
        self.workdir = parserargs.workdir
        self.logfile = parserargs.logfile
        self.number = parserargs.number
        self.reportdir = parserargs.reportdir
        self.nocache = parserargs.nocache

    def __init__(self, parserargs=None):
        pass