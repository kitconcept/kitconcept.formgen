# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from kitconcept.formgen.testing import KITCONCEPT_FORMGEN_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that kitconcept.formgen is properly installed."""

    layer = KITCONCEPT_FORMGEN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if kitconcept.formgen is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'kitconcept.formgen'))

    def test_browserlayer(self):
        """Test that IPloneFormgenLayer is registered."""
        from kitconcept.formgen.interfaces import (
            IPloneFormgenLayer)
        from plone.browserlayer import utils
        self.assertIn(IPloneFormgenLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KITCONCEPT_FORMGEN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['kitconcept.formgen'])

    def test_product_uninstalled(self):
        """Test if kitconcept.formgen is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'kitconcept.formgen'))

    def test_browserlayer_removed(self):
        """Test that IPloneFormgenLayer is removed."""
        from kitconcept.formgen.interfaces import IPloneFormgenLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPloneFormgenLayer, utils.registered_layers())
