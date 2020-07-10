# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.fti import DexterityFTI
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.restapi.behaviors import IBlocks
from zope.interface import alsoProvides

from kitconcept.voltoformbuilder.testing import (
    KITCONCEPT_voltoformbuilder_INTEGRATION_TESTING,
)  # noqa
from kitconcept.voltoformbuilder.testing import (
    KITCONCEPT_voltoformbuilder_FUNCTIONAL_TESTING,
)  # noqa

import unittest
import requests
import transaction


class FormSubmitFunctionalTest(unittest.TestCase):

    layer = KITCONCEPT_voltoformbuilder_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.request = self.layer["request"]
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        fti = DexterityFTI("blocksdocument")
        self.portal.portal_types._setObject("blocksdocument", fti)
        fti.klass = "plone.dexterity.content.Container"
        fti.behaviors = ("volto.blocks",)
        self.portal.invokeFactory("blocksdocument", id="doc")
        self.doc = self.portal["doc"]
        alsoProvides(self.doc, IBlocks)
        transaction.commit()

    def test_form_submit(self):
        data = {
            "email": "john@example.com",
            "subject": "hello world",
            "comment": "lorem ipsum",
        }
        response = requests.post(
            self.doc.absolute_url() + "/submit-form",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json=data,
        )
        transaction.commit()

        self.assertEqual(201, response.status_code)
        self.assertEqual(data, self.doc.data)

    def test_form_submit_appends_data(self):
        self.doc.data = {
            "email": "john@example.com",
            "subject": "hello world",
            "comment": "lorem ipsum",
        }
        transaction.commit()

        newdata = {
            "email": "jane@example.com",
            "subject": "hi from jane",
            "comment": "hi there",
        }
        response = requests.post(
            self.doc.absolute_url() + "/submit-form",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json=newdata,
        )
        transaction.commit()

        self.assertEqual(201, response.status_code)
        # todo: check that data is appended
