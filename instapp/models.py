from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profile/',null=True,blank=True)
    bio = models.CharField(max_length=60,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def update_profile(cls,id,bio):
        updated = Image.objects.filter(id=id).update(bio = bio)
        return updated




class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    caption = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.caption
    class Meta:
        ordering = ['-upload_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,caption):
        captioned = Image.objects.filter(id=id).update(caption = caption)
        return captioned

    @classmethod
    def get_images(cls):
        image = Image.objects.all()
        return image

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=Image.id)
        return image

class Comment(models.Model):
    comments = models.CharField(max_length=60,blank=True,null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    def __str__(self):
        return self.comments

    class Meta:
        ordering = ['-comment_date']

    def save_comment(self):
        return self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment
