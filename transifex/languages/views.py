import os

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import list_detail
from django.utils.translation import ugettext_lazy as _
from django.contrib.syndication.views import feed
from django.template import RequestContext

from translations.models import POFile
from models import Language
from projects.models import Project
from releases.models import Release

def slug_feed(request, slug=None, param='', feed_dict=None):
    """
    Override default feed, using custom (including inexistent) slug.
    
    Provides the functionality needed to decouple the Feed's slug from
    the urlconf, so a feed mounted at "^/feed" can exist.
    
    See also http://code.djangoproject.com/ticket/6969.
    """
    if slug:
        url = "%s/%s" % (slug, param)
    else:
        url = param
    return feed(request, url, feed_dict)


def language_detail(request, slug, *args, **kwargs):
    language = get_object_or_404(Language, code__iexact=slug)
        
    return list_detail.object_detail(
        request,
        object_id=language.id,
        *args, **kwargs
    )
