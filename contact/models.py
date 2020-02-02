from datetime import date

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.admin.mail import send_mail
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core.fields import RichTextField


class FormField(AbstractFormField):
    page = ParentalKey('Contact', related_name='custom_form_fields')


class Contact(AbstractEmailForm):
    thank_you_intro = models.TextField()
    thank_you_text = RichTextField(blank=True)
    intro = models.TextField()
    body = models.TextField()

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
        InlinePanel('custom_form_fields', label='Form fields'),
        FieldPanel('thank_you_intro', classname='full'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], 'Email Notification Config'),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()
