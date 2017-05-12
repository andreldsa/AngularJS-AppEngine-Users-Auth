# -*- coding: utf-8 -*-
"""Main."""

import webapp2

import json

from google.appengine.api import users


def login_required(method):
    """Handle required login."""
    def login(self, *args):
        user = users.get_current_user()
        if user is None:
            self.response.write(json.dumps({
                'msg': 'Auth needed',
                'login_url': 'http://%s/api/auth/login' % self.request.host
            }))
            self.response.set_status(401)
            return
        method(self, user, *args)
    return login


def json_response(method):
    """Add content type header to the response."""
    def response(self, *args):
        self.response.headers[
            'Content-Type'] = 'application/json; charset=utf-8'
        method(self, *args)
    return response


class LoginHandler(webapp2.RequestHandler):
    """Handles Login requests."""

    def get(self):
        """Handle HTTP GET request."""
        user = users.get_current_user()
        if user:
            self.redirect('/')
        else:
            self.redirect(users.create_login_url(self.request.path))


class LogoutHandler(webapp2.RequestHandler):
    """Handles Login requests."""

    def get(self):
        """Handle HTTP GET request."""
        redirectTo = self.request.get('redirect') or '/'
        user = users.get_current_user()
        if user:
            self.redirect(users.create_logout_url(redirectTo))


class MainHandler(webapp2.RequestHandler):
    """Handles Login requests."""

    @json_response
    @login_required
    def get(self, user):
        """Handle HTTP GET request."""
        self.response.write(json.dumps({
            'email': user.email(),
            'id': user.user_id(),
            'nickname': user.nickname(),
            'logout': 'http://%s/api/auth/logout?redirect=%s' %
            (self.request.host, self.request.path)
        }))


app = webapp2.WSGIApplication([
    ('/api/auth/login', LoginHandler),
    ('/api/auth/logout', LogoutHandler),
    ('/api.*', MainHandler)
])
