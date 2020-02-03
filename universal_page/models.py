from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from universal_page.blocks import WhiteHeaderWithButton, ThreeColumnsWithHeaders, Faq, BlockQuoteWithHeader
from wagtail.core import blocks


class UniversalPage(Page):
    body = StreamField([
        ('grey_header', blocks.CharBlock(classname="grey_header")),
        ('white_header_with_button', WhiteHeaderWithButton()),
        ('three_columns_with_headers', ThreeColumnsWithHeaders()),
        ('small_grey_header', blocks.CharBlock(classname="small_grey_header")),
        ('faq', Faq()),
        ('blockquote', blocks.CharBlock(classname="blockquote")),
        ('blockquote_with_header', BlockQuoteWithHeader()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
