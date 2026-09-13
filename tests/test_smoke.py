import unittest
from apps.notifier.notifier import ReleaseNotifier

class Smoke(unittest.TestCase):
    def test_entrypoint_exists(self):
        self.assertTrue(hasattr(ReleaseNotifier, "announce"))
