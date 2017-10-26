"""pycrawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from pycrawler.views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^scopus/years$', ScopusYearsView.as_view(), name='scopus_years'),
    url(r'^scopus/lt2000$', ScopusLt2000View.as_view(), name='scopus_lt2000'),
    url(r'^scopus/gt2000/subjects$', ScopusGt2000SubjectsView.as_view(), name='scopus_gt2000_subjects'),
    url(r'^scopus/gt2000/download$', ScopusGt2000DownloadView.as_view(), name='scopus_gt2000_download'),
    url(r'^scopus/lt2000/import$', ScopusImportLt2000View.as_view(), name='scopus_lt2000_import'),
    url(r'^scopus/gt2000/import$', ScopusImportGt2000View.as_view(), name='scopus_gt2000_import'),
    url(r'^scopus/author-to-json$', ScopusAuthorToJsonView.as_view(), name='scopus_author_to_json'),
    url(r'^isi/paginate$', IsiPaginateView.as_view(), name='isi_paginate'),
    url(r'^isi/key$', IsiKeyView.as_view(), name='isi_key'),
    url(r'^isi/import$', IsiImportView.as_view(), name='isi_import'),
    url(r'^isi/author-to-json$', IsiAuthorJson.as_view(), name='isi_author_json'),
]
