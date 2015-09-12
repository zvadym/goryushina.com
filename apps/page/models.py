from django.core.urlresolvers import reverse
from django.db import models
from tinymce.models import HTMLField
from sorl.thumbnail import ImageField

from apps.menu.models import MenuItem


class Page(MenuItem):
    title = models.CharField(max_length=128)
    text = HTMLField(
        verbose_name=u'Text',
        help_text='The best video/photo size is 695x390'
    )

    slug = models.SlugField()

    category = models.ForeignKey('page.Category', blank=True, null=True)
    preview = ImageField(upload_to='page_preview')

    create_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        
    @staticmethod
    def object_type():
        return 'Page'

    def get_url(self):
        return reverse('ui:page', kwargs={'slug': self.slug})

    def __str__(self):
        return '%s: %s' % (self.object_type(), self.title)

    def get_absolute_url(self):
        return self.get_url()


class Category(MenuItem):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    @staticmethod
    def object_type():
        return 'Category'

    def get_url(self):
        return reverse('ui:category', kwargs={'slug': self.slug})

    @property
    def active_pages(self):
        return self.page_set.filter(is_active=True)

    def __str__(self):
        return '%s: %s' % (self.object_type(), self.title)

    def get_absolute_url(self):
        return self.get_url()
