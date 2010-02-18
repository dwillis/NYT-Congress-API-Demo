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
        gop = ['B001261','C001071','K000352','S001141','V000127','A000360','B000382','B000611','B000953','B001066','B001135','C000286','C000560','C000567','C001035','C001056','C000880','D000595','E000194','E000285','G000359','G000386','G000445','H000338','H001016','I000024','I000055', 'J000291','L000504','M000303','M000355','M001153','R000584','R000307','S000320','S000663','T000250','V000126','W000437']
        dems = ['F000457','I000025','L000123','T000464','S000033','B000243','B001233','B001265','B000468','B000711','B000944','B001266','B001210','C000127','C000141','C000174','C001070','C000705','D000388','D000432','D000563','F000061','F000062','G000555','H001049','H000206','J000177','K000373','K000148','K000367','K000305','L000550','L000174','L000261','L000035','M001170','M000639','M001176','M000702','M001111','N000032','N000180','P000590','R000122','R000146','R000361','S000148','S001181','S000709','S000770','U000038','U000039','W000805','W000803','W000802','W000779']
        try:
            first_member = nytcongress.members.get(random.choice(gop))
            second_member = nytcongress.members.get(random.choice(dems))
            comparison = nytcongress.members.compare(first_member.member_id, second_member.member_id, 111, 'senate')
            sponsor_comparison = nytcongress.bills.sponsor_compare(first_member.member_id, second_member.member_id, 111, 'senate')
            template_values = { 'first_member' : first_member, 'second_member': second_member, 'comparison': comparison, 'sponsor_comparison': sponsor_comparison, 'bills':len(sponsor_comparison)}
        except NYTCongressApiError:
            error = "Looks like you didn't supply an API key."
            template_values = {'error': error}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
