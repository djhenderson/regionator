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


import kml.kmlparse

print 'test kml.kmlparse.KMLParse go.kml ... start'

kmldoc = kml.kmlparse.KMLParse('go.kml')

latlonbox = kmldoc.ExtractLatLonBox()
if latlonbox.north != '20':
  print 'ERROR in ExtractLatLonBox'
if latlonbox.south != '-20':
  print 'ERROR in ExtractLatLonBox'
if latlonbox.east != '20':
  print 'ERROR in ExtractLatLonBox'
if latlonbox.west != '-20':
  print 'ERROR in ExtractLatLonBox'

#print latlonbox.xml()

icon = kmldoc.ExtractIcon()
if icon.href != 'foo.jpg':
  print 'ERROR in ExtractIcon'

# print icon.xml()

timespan = kmldoc.ExtractTimeSpan()
if timespan.begin != '2006':
  print 'ERROR in ExtractTimeSpan'
if timespan.end != '2007':
  print 'ERROR in ExtractTimeSpan'

# print timespan.xml()

go = kmldoc.ExtractGroundOverlay()
# print go.xml()
if go.drawOrder != '10':
  print 'ERROR in ExtractGroundOverlay'

print 'test kml.kmlparse.KMLParse go.kml ... done'

