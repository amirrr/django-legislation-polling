from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _
#from tinymce.models import HTMLField

# Create your models here.

class Poll(models.Model):
    """ poll model """
    picture = models.ImageField(verbose_name='عکس بنر', upload_to='picture/', null=True, blank=True)
    title = models.CharField(verbose_name='عنوان لایحه', max_length=150)
    description = models.TextField(verbose_name='متن لایحه')
    option_one_count = models.IntegerField(verbose_name='تعداد رای آری', default=0)
    option_two_count = models.IntegerField(verbose_name='تعداد رای خیر', default=0)
    option_three_count = models.IntegerField(verbose_name='تعداد رای ممتنع', default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Poll")
        verbose_name_plural = _("Polls")

    def __str__(self):
        return 'لایحه: ' + self.title

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    def user_can_vote(self, user):
        """
        Returns False is user has already voted, else True
        """
        user_votes = user.vote_set.all()
        qs = user_votes.filter(poll=self)
        if qs.exists():
            return False
        return True


    # use the one below for reusable app
    # tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    # tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)