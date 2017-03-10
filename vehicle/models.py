from __future__ import unicode_literals

from django.db import models
import os.path
from django.utils import timezone
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your models here.



class PostsSubmit(models.Model):
    vehicle_no = models.CharField(max_length=100)
    type = models.TextField()
    vehicle_image = models.ImageField(upload_to='pic_folder/')
    insurance_renewed_date = models.DateTimeField(blank=True, null=True)
    # image_height = models.IntegerField()
    # image_width = models.IntegerField()
    thumbnail = models.ImageField(upload_to="thumbs/")
    # thumbnail_height = models.IntegerField()
    # thumbnail_width = models.IntegerField()
    caption = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return "%s" % self.vehicle_no

    def __unicode__(self):
        return self.vehicle_no

    def save(self, force_update=False, force_insert=False, thumb_size=(180, 300)):
        vehicle_image = Image.open(self.product_image)

        if vehicle_image.mode not in ('L', 'RGB'):
            product_image = vehicle_image.convert('RGB')

        # save the original size
        self.vehicle_image_width, self.vehicle_image_height = vehicle_image.size

        vehicle_image.thumbnail(thumb_size, Image.ANTIALIAS)

        # save the thumbnail to memory
        temp_handle = StringIO()
        vehicle_image.save(temp_handle, 'png')
        temp_handle.seek(0)  # rewind the file

        # save to the thumbnail field
        suf = SimpleUploadedFile(os.path.split(self.vehicle_image.name)[-1],
                                 temp_handle.read(),
                                 content_type='image/png')
        self.thumbnail.save(suf.name + '.png', suf, save=False)
        self.thumbnail_width, self.thumbnail_height = vehicle_image.size

        # save the image object
        super(PostsSubmit, self).save(force_update, force_insert)

    def publish(self):
        self.insurance_renewed_date = timezone.now()
        self.save()