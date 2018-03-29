# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from plone.formgen.testing import PLONE_FORMGEN_INTEGRATION_TESTING  # noqa
from plone.formgen.interfaces import IForm

import unittest2 as unittest


class FormIntegrationTest(unittest.TestCase):

    layer = PLONE_FORMGEN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

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
