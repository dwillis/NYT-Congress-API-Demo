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

class MainHandler(webapp.RequestHandler):

  def get(self, member):
    if member:
        member_id = member
        try:
            member = nytcongress.members.get(member_id)
            appearances = nytcongress.members.floor(id=member_id)
            hcr = [a for a in appearances if "Service" in a.title or "Health Care Reform" in a.title]
        except:
            member = None
            appearances = None
            
        template_values = {
                    'appearances': hcr,
                    'member': member,
                    }
    else:
        members = nytcongress.members.filter(congress=111, chamber='senate')
        template_values = {
                    'members': members
                    }
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

def main():
  application = webapp.WSGIApplication([('/(.*)', MainHandler)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
