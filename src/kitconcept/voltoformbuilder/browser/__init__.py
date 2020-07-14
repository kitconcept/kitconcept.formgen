# -*- coding: utf-8 -*-
from plone.rest import Service
from plone.restapi.deserializer import json_body

import transaction


class FormPost(Service):
    def render(self):
        # todo: data needs to be appended
        self.context.data = json_body(self.request)
        transaction.commit()
        return self.request.response.setStatus(201)


class FormGet(Service):
    def render(self):
        return [
            {
                "email": "john@example.com",
                "subject": "hello world",
                "comment": "lorem ipsum",
            },
            {
                "email": "jane@example.com",
                "subject": "hi from jane",
                "comment": "hi there",
            },
        ]
