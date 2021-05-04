from django.test import TestCase


from django.contrib.auth import get_user_model
from .models import Status
User = get_user_model()


class UserTestCase(TestCase): 
    def setUp(self): 
        user =  User.objects.create(username='cfe', email='hello@cfe.com')
        user.set_password("yeahhhcfe")
        user.save()

    def test_creating_status(self):
        user =User.objects.get(username= 'cfe')
        obj = Status.objects.create(user = user, content='some cool content')
        self.assertEqual(obj.id, 1)
        qs = Status.objects.all()
        self.assertEqual(qs.count(),1)