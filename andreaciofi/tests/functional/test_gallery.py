from andreaciofi.tests import *

class TestGalleryController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='gallery', action='index'))
        # Test response...
