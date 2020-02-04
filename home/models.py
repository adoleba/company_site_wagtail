from datetime import datetime

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

from wagtail.core.models import Page


class HomePage(Page):
    header_title = models.CharField(max_length=500)
    header_description = models.TextField()
    about_intro = models.CharField(max_length=200)
    about_description = models.TextField()
    first_card_title = models.CharField(max_length=200)
    first_card_description = models.TextField()
    first_card_button_text = models.CharField(max_length=20)
    first_card_button_url = models.ForeignKey('wagtailcore.Page', on_delete=models.SET_NULL,
                                              null=True, related_name='+')
    second_card_title = models.CharField(max_length=200)
    second_card_description = models.TextField()
    second_card_button_text = models.CharField(max_length=20)
    second_card_button_url = models.ForeignKey('wagtailcore.Page', on_delete=models.SET_NULL,
                                               null=True, related_name='+')
    third_card_title = models.CharField(max_length=200)
    third_card_description = models.TextField()
    third_card_button_text = models.CharField(max_length=20)
    third_card_button_url = models.ForeignKey('wagtailcore.Page', on_delete=models.SET_NULL,
                                              null=True, related_name='+')
    edited = models.DateTimeField(auto_now=datetime.now)

    content_panels = Page.content_panels + [
        FieldPanel('header_title', classname="full"),
        FieldPanel('header_description', classname="full"),
        FieldPanel('about_intro', classname="full"),
        FieldPanel('about_description', classname="full"),
        FieldPanel('first_card_title', classname="full"),
        FieldPanel('first_card_description', classname="full"),
        FieldPanel('first_card_button_text', classname="full"),
        PageChooserPanel('first_card_button_url'),
        FieldPanel('second_card_title', classname="full"),
        FieldPanel('second_card_description', classname="full"),
        FieldPanel('second_card_button_text', classname="full"),
        PageChooserPanel('second_card_button_url'),
        FieldPanel('third_card_title', classname="full"),
        FieldPanel('third_card_description', classname="full"),
        FieldPanel('third_card_button_text', classname="full"),
        PageChooserPanel('third_card_button_url'),
    ]
