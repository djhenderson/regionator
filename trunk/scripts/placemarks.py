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
$URL$
$Revision$
$Date$
"""

import sys

import kml.placemarkregionator

if len(sys.argv) != 4:
  print 'usage: %s input.kml odir oroot.kml' % sys.argv[0]
  sys.exit(1)

kmlfile = sys.argv[1]
dir = sys.argv[2]
rootkml = sys.argv[3]

lod = 256
per = 16

pmr = kml.placemarkregionator.PlacemarkRegionator()
if pmr:
  pmr.Regionate(kmlfile,lod,per,rootkml,dir)
