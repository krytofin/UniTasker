from abc import ABC

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AccountViewTestMixin(ABC):
    url_name = None 
    params = {}

    def test_annonim_user(self):
        uri = reverse(self.url_name, **self.params)
        response = self.client.get(uri)
        self.assertEqual(response.status_code, 302)

    def test_default_user(self):
        user_model = get_user_model()
        user = user_model.objects.create(username="admin")
        user.set_password("1234")
        user.save()

        self.client.login(username="admin", password="1234")

        uri = reverse(self.url_name)
        response = self.client.get(uri)
        self.assertEqual(response.status_code, 200)


class HomeworkListViewTests(TestCase, AccountViewTestMixin):
    url_name = "diary:all_homework"


class HomeworkCreateTests(TestCase, AccountViewTestMixin):
    url_name = "diary:create_subject"



class SubjectListTests(TestCase, AccountViewTestMixin):
    url_name = "diary:all_subjects"

