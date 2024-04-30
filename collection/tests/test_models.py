from django.test import TestCase
from django.contrib.auth.models import User
from collection.models import Category, Kit

class TestCategoriesModel(TestCase):

    #Creating data to test against to set up the test
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return(self):
        """
        Test Category model return default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestKitModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')

        self.data1 = Kit.objects.create(category_id=1, name='django beginners', created_by_id=1, slug='django-beginners', image='django')

        def test_kits_model_entry(self):
            """
            Test kit model data insertion/types/field attributes
            """
            data = self.data1
            self.assertTrue(isinstance(data, Kit))
            self.assertEquel(str(data), 'django beginners')
