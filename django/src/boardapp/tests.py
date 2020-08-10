from django.test import TestCase, Client
from django.db.models import Max

from .models import BoardModel

# Create your tests here.
class BoardTestCase(TestCase):

    def setUp(self):

        # Create airports.
        a1 = BoardModel.objects.create(title="test_title",
                                       content="test_contnt",
                                       author="test_author",
                                       images='',
                                       good=1,
                                       read=2,
                                       readtext="test_readtext"
                                       )


## end of document ###
