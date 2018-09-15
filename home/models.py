from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


class HomePage(Page):
    slide_content_1 = RichTextField(blank=True)
    slide_content_2 = RichTextField(blank=True)
    slide_content_3 = RichTextField(blank=True)
    quote = RichTextField(blank=True)
    cite = RichTextField(blank=True)
    about_head = RichTextField(blank=True)
    about_content = RichTextField(blank=True)
    quote2 = RichTextField(blank=True)
    contact_intro = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('slide_content_1', classname="full"),
        FieldPanel('slide_content_2', classname="full"),
        FieldPanel('slide_content_3', classname="full"),
        FieldPanel('quote', classname="full"),
        FieldPanel('cite', classname="full"),
        FieldPanel('about_head', classname="full"),
        FieldPanel('about_content', classname="full"),
        FieldPanel('quote2', classname="full"),
        FieldPanel('contact_intro', classname="full"),
    ]
