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



# Simple test of Tile extraction

import sys

import kml.extractor

in_image = sys.argv[1]

ex = kml.extractor.Extractor(in_image,256,256,'JPEG')
ex.Extract(0,0,256,256,'0')
ex.Extract(256,0,256,256,'1')
ex.Extract(0,256,256,256,'2')
ex.Extract(256,256,256,256,'3')



