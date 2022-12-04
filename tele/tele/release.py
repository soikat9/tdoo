# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

RELEASE_LEVELS = [ALPHA, BETA, RELEASE_CANDIDATE, FINAL] = ['alpha', 'beta', 'candidate', 'final']
RELEASE_LEVELS_DISPLAY = {ALPHA: ALPHA,
                          BETA: BETA,
                          RELEASE_CANDIDATE: 'rc',
                          FINAL: ''}

# version_info format: (MAJOR, MINOR, MICRO, RELEASE_LEVEL, SERIAL)
# inspired by Python's own sys.version_info, in order to be
# properly comparable using normal operarors, for example:
#  (1,1,0,'beta',0) < (1,1,0,'candidate',1) < (1,1,0,'candidate',2)
#  (1,1,0,'candidate',2) < (1,1,0,'final',0) < (1,1,2,'final',0)
version_info = (1, 0, 0, FINAL, 0, '')
version = '.'.join(str(s) for s in version_info[:2]) + RELEASE_LEVELS_DISPLAY[version_info[3]] + str(version_info[4] or '') + version_info[5]
series = serie = major_version = '.'.join(str(s) for s in version_info[:2])

product_name = 'Tele'
description = 'Tele Server'
long_desc = '''Tele identifies itself as more of a "System" than a Software as a Service (SaaS) provider for small to large enterprises. The multi-industry system possesses the ability to streamline business processes, enhance overall revenues while reducing overhead costs associated with outsourcing everyday technology resources.
'''
classifiers = """Development Status :: 1 - Production/Stable
License :: OSI Approved :: GNU Lesser General Public License v3

Programming Language :: Python
"""
url = 'https://www.tele.studio'
author = 'Tele INC.'
author_email = 'info@tele.studio'
license = 'LGPL-3'

nt_service_name = "tele-server-" + series.replace('~','-')
