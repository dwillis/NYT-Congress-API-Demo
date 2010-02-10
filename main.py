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
from django.utils import simplejson as json
import os
from google.appengine.ext.webapp import template
from nytcongressapi import nytcongress, NYTCongressApiError
nytcongress.api_key = 'NYT-API-KEY'

class MainHandler(webapp.RequestHandler):
    def get(self):
        first_member = nytcongress.members.get("B001261")
        second_member = nytcongress.members.get("F000457")
        comparison = nytcongress.members.compare("B001261", "F000457", 111, 'senate')
        sponsor_comparison = nytcongress.bills.sponsor_compare("B001261", "F000457", 111, 'senate')
        template_values = { 'first_member' : first_member, 'second_member': second_member, 'comparison': comparison, 'sponsor_comparison': sponsor_comparison, 'bills':len(sponsor_comparison)}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
