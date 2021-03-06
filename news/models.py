from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.urls import reverse
# Create your models here.

@python_2_unicode_compatible

class Column(models.Model):
    name = models.CharField('Column_name',max_length=256)
    slug = models.CharField('Column_site', max_length=256, db_index=True)
    intro = models.TextField('Column_intro', default='')

    nav_display = models.BooleanField('Navigation', default=False)
    home_display = models.BooleanField('Home Page', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'
        ordering = ['name']  # order by name

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))


@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='Column_belongs')
    # id = models.AutoField(primary_key=True)

    title = models.CharField('title', max_length=256)
    slug = models.CharField('site', max_length=256, db_index=True)

    pub_date = models.DateTimeField('pub_date', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('update_date', auto_now=True, null=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='auth',on_delete=models.CASCADE)
    content = models.TextField('content', default='', blank=True)
    # content = UEditorField('Content', height=300, width=1000,
    #                        default=u'', blank=True, imagePath="uploads/images/",
    #                        toolbars='besttome', filePath='uploads/files/')
    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.slug))

    published = models.BooleanField('isPublished', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
