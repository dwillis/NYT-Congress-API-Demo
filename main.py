#!/usr/bin/env python2.5
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import urllib
import random
from django.utils import simplejson as json
import os
from google.appengine.ext.webapp import template
from nytcongressapi import nytcongress, NYTCongressApiError

class MainHandler(webapp.RequestHandler):
    def get(self):
        gop = ["A000360", "B001135", "B001236", "B001261", "C000286", "C000560", "C000567", "C000880", "C001035", "C001056", "C001071", "D000595", "E000194", "E000285", "G000359", "G000386", "H000338", "H001016", "I000024", "I000055", "K000352", "L000504", "M000303", "M000355", "M001153", "R000307", "S000320", "S000663", "S001141", "T000250", "V000127", "W000437", "R000584", "J000291", "B001268", "K000360", "R000595", "C000542", "M000934", "P000603", "B000575", "A000368", "H001061", "P000449", "T000461", "L000577", "J000293"]
        dems = ["A000069", "B000243", "B000468", "B000711", "B000944", "C000127", "C000141", "C000174", "C000705", "C001070", "D000563", "F000062", "H000206", "J000177", "K000148", "K000305", "K000367", "L000123", "L000174", "L000261", "L000304", "L000550", "M000639", "M000702", "M001111", "M001170", "N000032", "N000180", "P000590", "R000122", "R000146", "R000361", "S000033", "S000148", "S000770", "T000464", "W000779", "W000802", "W000803", "I000025", "B001265", "U000038", "S001181", "U000039", "H001049", "M001176", "W000805", "B001267", "G000555", "C001088", "M001183", "B001277"]
        try:
            first_member = nytcongress.members.get(random.choice(gop))
            second_member = nytcongress.members.get(random.choice(dems))
            comparison = nytcongress.members.compare(first_member.member_id, second_member.member_id, 112, 'senate')
            sponsor_comparison = nytcongress.bills.sponsor_compare(first_member.member_id, second_member.member_id, 112, 'senate')
            template_values = { 'first_member' : first_member, 'second_member': second_member, 'comparison': comparison, 'sponsor_comparison': sponsor_comparison, 'bills':len(sponsor_comparison)}
        except:
            error = "Oops. Something went wrong."
            template_values = {'error': error}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
