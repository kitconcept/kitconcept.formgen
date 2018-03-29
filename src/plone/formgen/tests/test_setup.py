# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone.formgen.testing import PLONE_FORMGEN_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plone.formgen is properly installed."""

    layer = PLONE_FORMGEN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.formgen is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plone.formgen'))

    def test_browserlayer(self):
        """Test that IPloneFormgenLayer is registered."""
        from plone.formgen.interfaces import (
            IPloneFormgenLayer)
        from plone.browserlayer import utils
        self.assertIn(IPloneFormgenLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_FORMGEN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plone.formgen'])

    def test_product_uninstalled(self):
        """Test if plone.formgen is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plone.formgen'))

    def test_browserlayer_removed(self):
        """Test that IPloneFormgenLayer is removed."""
        from plone.formgen.interfaces import IPloneFormgenLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPloneFormgenLayer, utils.registered_layers())
