# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD

from kitconcept.formgen.testing import KITCONCEPT_FORMGEN_INTEGRATION_TESTING  # noqa
from kitconcept.formgen.testing import KITCONCEPT_FORMGEN_FUNCTIONAL_TESTING  # noqa
from kitconcept.formgen.interfaces import IForm

import unittest
import json
import requests
import transaction


class FormIntegrationTest(unittest.TestCase):

    layer = KITCONCEPT_FORMGEN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name="Form")
        schema = fti.lookupSchema()
        self.assertEqual(IForm, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name="Form")
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name="Form")
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IForm.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory("Form", "Form")
        self.assertTrue(IForm.providedBy(self.portal["Form"]))


class FormFunctionalTest(unittest.TestCase):

    layer = KITCONCEPT_FORMGEN_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.request = self.layer["request"]
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.portal.invokeFactory("Form", id="form")
        self.form = self.portal["form"]
        transaction.commit()

    def test_get_schema(self):
        schema = {
            "title": "Form",
            "type": "object",
            "properties": {
                "email": {"type": "string"},
                "subject": {"type": "string"},
                "comments": {"type": "string"},
            },
            "required": ["email", "subject", "comments"],
        }
        self.form.schema = schema
        response = requests.get(
            self.form.absolute_url(),
            headers={"Accept": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
        )
        self.assertEqual(200, response.status_code)

    def test_post_schema(self):
        schema = {
            "title": "Form",
            "type": "object",
            "properties": {
                "email": {"type": "string"},
                "subject": {"type": "string"},
                "comments": {"type": "string"},
            },
            "required": ["email", "subject", "comments"],
        }
        response = requests.post(
            self.form.absolute_url(),
            headers={
                "Accept": "application/json",
                "Content-Type": "application/schema-instance+json",
            },
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json=schema,
        )
        transaction.commit()

        self.assertEqual(201, response.status_code)
        self.assertEqual(bytes(json.dumps(schema), "utf-8"), self.form.schema)

    def test_patch_schema(self):
        schema = {
            "title": "Form",
            "type": "object",
            "properties": {
                "email": {"type": "string"},
                "subject": {"type": "string"},
                "comments": {"type": "string"},
            },
            "required": ["email", "subject", "comments"],
        }
        response = requests.patch(
            self.form.absolute_url(),
            headers={
                "Accept": "application/json",
                "Content-Type": "application/schema-instance+json",
            },
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json=schema,
        )
        transaction.commit()

        self.assertEqual(204, response.status_code)
        self.assertEqual(bytes(json.dumps(schema), "utf-8"), self.form.schema)

    def test_delete_schema(self):
        self.form.schema = '{"type": "object"}'
        transaction.commit()

        response = requests.delete(
            self.form.absolute_url(),
            headers={"Accept": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
        )
        transaction.commit()

        self.assertEqual(204, response.status_code)
        self.assertEqual(u"{}", self.form.schema)

    def test_form_submit(self):
        schema = {
            "email": "john@example.com",
            "subject": "hello world",
            "comment": "lorem ipsum",
        }
        response = requests.post(
            self.form.absolute_url() + "/submit",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
            json=schema,
        )
        transaction.commit()

        self.assertEqual(201, response.status_code)
