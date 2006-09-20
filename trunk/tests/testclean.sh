#!/bin/sh

# Copyright (C) 2006 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# $URL$
# $Revision$
# $Date$


# clean up after tests.sh and testimg.sh

rm -f testkml.kml
rm -f testxml.xml
rm -f root.kml
rm -f ancestors.kml
rm -rf usboxes
rm -rf pmroot.kml pm
rm -rf lsroot.kml ls
rm -f outline.kml
rm -f screeno.kml screeno*.jpg
rm -f gridso.kml gridso*.jpg
rm -rf mv-polys
rm -f terra.kml terra_e.jpg terra_w.jpg
