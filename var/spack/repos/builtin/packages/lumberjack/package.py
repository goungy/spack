# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install lumberjack
#
# You can edit this file again by typing:
#
#     spack edit lumberjack
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Lumberjack(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://gitlab.com/Shurizai/Lumberjack"
    url      = "https://gitlab.com/Shurizai/Lumberjack"

    # FIXME: Add proper versions and checksums here.
    version('develop', git='https://gitlab.com/Shurizai/Lumberjack.git', branch='master')

    # FIXME: Add dependencies if required.
    depends_on('cuda@10:')
    depends_on('glew')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
