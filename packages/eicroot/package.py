# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Eicroot(CMakePackage):
    """EicRoot software framework"""

    homepage = "http://github.com/eic/EicRoot"
    url      = "http://github.com/eic/EicRoot"
    git      = "http://github.com/eic/EicRoot.git"

    version('master', branch='master')

    depends_on('root@6.00.00: +vmc')
    depends_on('geant4-vmc')

    def patch(self):
        """Replace __USE_BSD with __USE_MISC in recent gcc."""
        filter_file(
            '__USE_BSD',
            '__USE_MISC',
            "dbase/dbValidation/ValTimeStamp.cxx")

    def cmake_args(self):
        spec = self.spec

        args = []
        args.append('-DCAD2ROOT=no')
        args.append('-DHTC=no')

        return args
