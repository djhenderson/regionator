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



import kml.genkml
import kml.genxml

document = kml.genxml.Document()

document.Add_Feature(kml.genkml.LatLonOutline(80,60,-130,-90,'foo'))
document.Add_Feature(kml.genkml.LatLonOutline(20,10,-130,-90,'goo'))

k = kml.genxml.Kml()
k.Feature = document.xml()

f = open('outline.kml','w')
f.write(k.xml())
f.close

