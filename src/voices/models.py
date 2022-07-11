from django.db import models
from users.models import User


class Record(models.Model):
    record_text = models.TextField(verbose_name='Record text', max_length=500)
    file = models.FileField(verbose_name='Record file', upload_to='voices/', max_length=500)

    def __str__(self):
        return str(self.id)


class RecordHistory(models.Model):
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
        verbose_name='Record',
        related_name='record'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='user'
    )
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Record History'
        verbose_name_plural = 'Record Histories'



