from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractForm, AbstractFormSubmission
from django import forms


# Create your models here.
class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class RagingGooseDoc(Page):
    intro = RichTextField(blank=True)
    name = models.CharField(blank=True, max_length=100)  # Define the 'name' field
    problem = models.TextField(blank=True, max_length=500)  # Define the 'problem' field
    thank_you_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('problem'),
        ], heading='User Input'),
    ]
