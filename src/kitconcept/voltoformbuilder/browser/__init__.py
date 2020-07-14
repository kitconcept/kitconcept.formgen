# -*- coding: utf-8 -*-
from plone.rest import Service
from plone.restapi.deserializer import json_body

import logging
import transaction

logger = logging.getLogger("kitconcept.voltoformbuilder")


class FormPost(Service):
    def render(self):
        # todo: data needs to be appended
        self.context.data = json_body(self.request)
        transaction.commit()
        logger.info("FORM: POST DATA")
        return self.request.response.setStatus(201)


class FormGet(Service):
    def render(self):
        logger.info("FORM: GET")
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
