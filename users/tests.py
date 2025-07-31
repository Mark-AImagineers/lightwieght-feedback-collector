from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):
    """Tests for the custom EmailUser model."""

    def test_create_superuser_is_saved_and_staff(self):
        """Superusers should be created, saved, and marked as staff."""
        User = get_user_model()
        user = User.objects.create_superuser(
            email="admin@example.com",
            password="testpass123",
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(User.objects.filter(email="admin@example.com").exists())
