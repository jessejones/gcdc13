from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Language, Profile

class ProfileTestCase(TestCase):

    def test_add_language_with_no_active_language_set(self):
        """
        When adding languages to a profile with no active language set,
        active language should be set to the first in the list of languages
        when ordered alphabetically.
        """
        new_user = User.objects.create(username='user')
        profile = new_user.profile
        german = Language.objects.create(lang='German')
        greek = Language.objects.create(lang='Greek')

        profile.languages.add(german, greek)
        self.assertEqual(profile.active_language, german)

    def test_set_active_language_and_add_to_profile(self):
        """
        When an active language is set, make sure that it is included
        in the profile's list of languages.
        """
        new_user = User.objects.create(username='user')
        profile = new_user.profile
        new_language = Language.objects.create(lang='New Language')

        profile.active_language = new_language
        profile.save()
        self.assertEqual(profile.languages.all()[0], profile.active_language)