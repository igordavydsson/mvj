from auditlog.registry import auditlog
from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from field_permissions.registry import field_permissions
from users.models import User

from .mixins import NameModel, TimeStampedSafeDeleteModel


class CommentTopic(NameModel):
    """
    In Finnish: Aihe
    """
    class Meta(NameModel.Meta):
        verbose_name = pgettext_lazy("Model name", "Comment topic")
        verbose_name_plural = pgettext_lazy("Model name", "Comment topics")


class Comment(TimeStampedSafeDeleteModel):
    """
    In Finnish: Kommentti
    """
    lease = models.ForeignKey('leasing.Lease', verbose_name=_("Lease"), related_name='comments',
                              on_delete=models.PROTECT)

    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.PROTECT)

    topic = models.ForeignKey(CommentTopic, verbose_name=_("Topic"), on_delete=models.PROTECT)

    # In Finnish: Kommentti
    text = models.TextField(verbose_name=_("Text"), null=True, blank=True)

    class Meta:
        verbose_name = pgettext_lazy("Model name", "Comment")
        verbose_name_plural = pgettext_lazy("Model name", "Comments")
        ordering = ('-created_at', )


auditlog.register(Comment)

field_permissions.register(Comment, exclude_fields=['lease'])
field_permissions.register(CommentTopic)
