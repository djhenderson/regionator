#!/usr/bin/python

"""
Copyright (C) 2006 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
$URL: https://regionator.googlecode.com/svn/trunk/scripts/mkregionboxes.py $
$Revision: 251 $
$Date: 2007-03-10 12:27:26 -0800 (Sat, 10 Mar 2007) $
"""

import os
import sys
import kml.getsupertiles

if len(sys.argv) != 5:
  app = os.path.basename(sys.argv[0])
  print 'usage: %s url.kml level tardir output.tar' % app
  print '       level 0 is finest grain'
  sys.exit(1)

inputkml = sys.argv[1]
level = int(sys.argv[2])
tardir = sys.argv[3]
output = sys.argv[4]

kml.getsupertiles.GetSuperTiles(inputkml, level, tardir, output)
