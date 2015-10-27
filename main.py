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

import webapp2
from google.appengine.ext.webapp import util
import urllib
import random
import json
import os
from google.appengine.ext.webapp import template
from nytcongressapi import nytcongress, NYTCongressApiError

class MainHandler(webapp2.RequestHandler):
    def get(self):
        gop = [u'A000360', u'A000368', u'B000575', u'B001135', u'B001236', u'B001261', u'C000542', u'C000567', u'C000880', u'C001035', u'C001047', u'C001056', u'C001071', u'C001075', u'C001095', u'C001098', u'D000618', u'E000285', u'E000295', u'F000444', u'F000463', u'G000359', u'G000386', u'G000562', u'H000338', u'H001041', u'H001061', u'I000024', u'I000055', u'J000293', u'K000360', u'L000575', u'L000577', u'M000303', u'M000355', u'M000934', u'M001153', u'P000449', u'P000603', u'P000612', u'R000307', u'R000584', u'R000595', u'R000605', u'S000320', u'S001141', u'S001184', u'S001197', u'S001198', u'T000250', u'T000461', u'T000476', u'V000127', u'W000437']
        dems = [u'B000711', u'B000944', u'B001230', u'B001267', u'B001277', u'B001288', u'C000127', u'C000141', u'C000174', u'C001070', u'C001088', u'D000563', u'D000607', u'F000062', u'F000457', u'G000555', u'H001042', u'H001046', u'H001069', u'K000367', u'K000384', u'L000174', u'M000133', u'M000639', u'M000702', u'M001111', u'M001169', u'M001170', u'M001176', u'M001183', u'N000032', u'P000595', u'R000122', u'R000146', u'S000148', u'S000770', u'S001181', u'S001194', u'T000464', u'U000039', u'W000779', u'W000802', u'W000805', u'W000817', u'K000383', u'S000033']
        try:
            first_member = nytcongress.members.get(random.choice(gop))
            second_member = nytcongress.members.get(random.choice(dems))
            comparison = nytcongress.members.compare(first_member.member_id, second_member.member_id, 114, 'senate')
            sponsor_comparison = nytcongress.bills.sponsor_compare(first_member.member_id, second_member.member_id, 114, 'senate')
            template_values = { 'first_member' : first_member, 'second_member': second_member, 'comparison': comparison, 'sponsor_comparison': sponsor_comparison, 'bills':len(sponsor_comparison)}
        except:
            error = "Oops. Something went wrong."
            template_values = {'error': error}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

def main():
    application = webapp2.WSGIApplication([('/', MainHandler)],
                                       debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
