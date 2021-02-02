from django.test import TestCase
from .models import Category,Image,Location

# Create your tests here.

class CategoryTestClass(TestCase):
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.search= Category(category='search')

    def test_instance(self):
        self.assertTrue(isinstance(self.search,Category))

    def tearDown(self):
        '''
        Method to clear the test that has been done on category
        '''
        Category.objects.all().delete()

    def test_save_method(self):
        '''
        Method to save category
        
        '''
        self.search.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        '''
        Method to delete the category
        '''
        self.delete_category('search')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location = Location(name = "")
        self.location.save_location()
        self.image = Image(id = 1,title = "test",description = "test description",location = self.location, image_url = "path/to/image")
        
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    def test_save_image(self):
        self.image.save_image()
        self.images = Image.objects.all()
        self.assertTrue(len(self.images) > 0)
        
    def test_get_image_by_id(self):
        self.image.save_image()
        self.image = Image.get_image_by_id(1)
        self.assertTrue(isinstance(self.image,Image))
        
    def test_update_image(self):
        self.image.save_image()
        self.image = Image.objects.filter(id = 1).update(image_url = "/image")
        self.updated_image = Image.get_image_by_id(1)
        self.assertEqual(self.updated_image.image_url,"/image")
        
    def test_search_by_category(self):
        self.image.save_image()
        self.category = categories(name = "test")
        self.category.save_category()
        self.image = Image.get_image_by_id(1).categories.add(self.category)
        self.searched_images = Image.search_by_category('test')
        self.assertTrue(len(self.searched_images) > 0)
        
    def test_filter_by_location(self):
        self.image.save_image()
        self.searched_images = Image.filter_by_location('')
        self.assertTrue(len(self.searched_images) > 0)
        
    def test_delete_image(self):
        self.image.save_image()
        self.searched_image = Image.get_image_by_id(1)
        self.searched_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)
