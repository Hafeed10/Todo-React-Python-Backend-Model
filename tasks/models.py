from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
     db_table = 'tasks_tasks'


     def _str_(self):
         return self.title

