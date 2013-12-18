"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from gvms.pilot.models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TestAuth(TestCase):
	def test_MD5Comparison(self):
		"""
		Checks MD5 Comparison with mkpasswd
		"""
		password = Profile.mkpasswd("test", "test")
		check = "05a671c66aefea124cc08b76ea6d30bb"
		
		self.assertEqual(password, check)
			
		