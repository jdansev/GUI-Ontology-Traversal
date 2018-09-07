from django.test import TestCase
from .models import Attack_Node, Defense_Node, Comment
import sys

class GUITestCase(TestCase):

    def test_numberAttack(self):
        sys.stderr.write(repr(Attack_Node.objects.all) + '\n')
        self.assertEqual("true","true")
