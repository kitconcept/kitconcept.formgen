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

import unittest2 as unittest
import requests
import transaction


class FormIntegrationTest(unittest.TestCase):

    layer = KITCONCEPT_FORMGEN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Form')
        schema = fti.lookupSchema()
        self.assertEqual(IForm, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Form')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Form')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IForm.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Form', 'Form')
        self.assertTrue(
            IForm.providedBy(self.portal['Form'])
        )


class FormFunctionalTest(unittest.TestCase):

    layer = KITCONCEPT_FORMGEN_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.request = self.layer['request']
        self.portal = self.layer['portal']
        self.portal_url = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Form', id='form')
        self.form = self.portal['form']
        transaction.commit()

    def test_get_schema(self):
        response = requests.get(
            self.form.absolute_url(),
            headers={'Accept': 'application/json'},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
        )
        self.assertEqual(200, response.status_code)

    def test_post_schema(self):
        response = requests.post(
            self.form.absolute_url(),
            headers={'Accept': 'application/json'},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
        )
        self.assertEqual(201, response.status_code)

    def test_patch_schema(self):
        response = requests.patch(
            self.form.absolute_url(),
            headers={'Accept': 'application/json'},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
        )
        self.assertEqual(204, response.status_code)

    def test_delete_schema(self):
        response = requests.delete(
            self.form.absolute_url(),
            headers={'Accept': 'application/json'},
            auth=(SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
        )
        self.assertEqual(204, response.status_code)
