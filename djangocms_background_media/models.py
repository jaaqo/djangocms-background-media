# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


@python_2_unicode_compatible
class BackgroundMedia(CMSPlugin):
    """
    Used to model the background media instance
    """
    name = models.CharField(_('name'), max_length=50)
    height = models.CharField(_('container height'), max_length=50, default="100%",
        help_text=_('Height in pixels or %'))
    add_style = models.BooleanField(_('add style'), default=True,
        help_text=_('Link default style sheet'))
    overlay = models.CharField(_('overlay'), max_length=25, blank=True, null=True,
        help_text=_('To add a css overlay enter the colour of the overlay, e.g. rgba(0,0,0,0.7)'))

    image = FilerImageField(verbose_name=_('image'), blank=True, null=True,
        related_name='image')
    image_position = models.CharField(_('image position'), max_length=50, default='center center',
        help_text=_('The css position of the image'))

    video_mp4 = FilerFileField(verbose_name=_('Video mp4'),
                               blank=True,
                               null=True,
                               related_name='video_mp4')
    video_ogv = FilerFileField(verbose_name=_('Video ogv'),
                               blank=True,
                               null=True,
                               related_name='video_ogv')
    video_webm = FilerFileField(verbose_name=_('Video webm'),
                                blank=True,
                                null=True,
                                related_name='video_webm')
    video_poster = FilerImageField(verbose_name=_('Video poster'),
                                   blank=True,
                                   null=True)
    vide_json_config = models.TextField(_('Vide.js config'),
                                        blank=True,
                                        null=True,
                                        help_text=_('The optional js object for the vide config. Click <a href="https://github.com/VodkaBears/Vide" target="_blank"> here</a> for more info.'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Background Media')
        verbose_name_plural = _('Background Media')

    def clean(self):
        if self.image and self.has_video():
            raise ValidationError(_('You cannot have both a video and an image selected'))

    def has_video(self):
        return self.video_mp4 or self.video_ogv or self.video_webm
