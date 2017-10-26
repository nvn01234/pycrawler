from django.db import models


class ScopusYear(models.Model):
    doc_count = models.IntegerField(null=True)
    selector = models.CharField(max_length=255, null=True)
    year = models.IntegerField(null=True)
    filename = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'scopus_years'
        app_label = 'scopus_years'


class ScopusSubject(models.Model):
    doc_count = models.IntegerField(null=True)
    selector = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    filename = models.CharField(max_length=255, null=True)
    year = models.IntegerField(null=True)
    status = models.CharField(max_length=255, null=True)
    export_status = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'scopus_subjects'
        app_label = 'scopus_subjects'


class ScopusDocument(models.Model):
    authors = models.TextField(null=True)
    title = models.TextField(null=True)
    year = models.TextField(null=True)
    source_title = models.TextField(null=True)
    volume = models.TextField(null=True)
    issue = models.TextField(null=True)
    art_no = models.TextField(null=True)
    page_start = models.TextField(null=True)
    page_end = models.TextField(null=True)
    page_count = models.TextField(null=True)
    cited_by = models.TextField(null=True)
    doi = models.TextField(null=True)
    link = models.TextField(null=True)
    affiliations = models.TextField(null=True)
    authors_with_affiliations = models.TextField(null=True)
    abstract = models.TextField(null=True)
    author_keywords = models.TextField(null=True)
    index_keywords = models.TextField(null=True)
    molecular_sequence_numbers = models.TextField(null=True)
    chemicals_cas = models.TextField(null=True)
    tradenames = models.TextField(null=True)
    manufacturers = models.TextField(null=True)
    funding_details = models.TextField(null=True)
    funding_text = models.TextField(null=True)
    references = models.TextField(null=True)
    correspondence_address = models.TextField(null=True)
    editors = models.TextField(null=True)
    sponsors = models.TextField(null=True)
    publisher = models.TextField(null=True)
    conference_name = models.TextField(null=True)
    conference_date = models.TextField(null=True)
    conference_location = models.TextField(null=True)
    conference_code = models.TextField(null=True)
    issn = models.TextField(null=True)
    isbn = models.TextField(null=True)
    coden = models.TextField(null=True)
    pubmed_id = models.TextField(null=True)
    language_of_original_document = models.TextField(null=True)
    abbreviated_source_title = models.TextField(null=True)
    document_type = models.TextField(null=True)
    source = models.TextField(null=True)
    eid = models.TextField(null=True)
    authors_json = models.TextField(null=True)

    class Meta:
        db_table = 'scopus_documents'
        app_label = 'scopus_documents'


class IsiPaginate(models.Model):
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    status = models.CharField(max_length=255, null=True)
    filename = models.CharField(max_length=255, null=True)
    key_status = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'isi_paginate'
        app_label = 'isi_paginate'


class IsiKey(models.Model):
    name = models.TextField(null=True)

    class Meta:
        db_table = 'isi_keys'
        app_label = 'isi_keys'


class IsiDocument(models.Model):
    abstract = models.TextField(null=True)
    address = models.TextField(null=True)
    affiliation = models.TextField(null=True)
    article_number = models.TextField(null=True)
    author = models.TextField(null=True)
    author_email = models.TextField(null=True)
    booktitle = models.TextField(null=True)
    book_author = models.TextField(null=True)
    cited_references = models.TextField(null=True)
    da = models.TextField(null=True)
    doc_delivery_number = models.TextField(null=True)
    doi = models.TextField(null=True)
    editor = models.TextField(null=True)
    eissn = models.TextField(null=True)
    funding_acknowledgement = models.TextField(null=True)
    funding_text = models.TextField(null=True)
    isbn = models.TextField(null=True)
    issn = models.TextField(null=True)
    journal = models.TextField(null=True)
    journal_iso = models.TextField(null=True)
    keyword = models.TextField(null=True)
    keywords_plus = models.TextField(null=True)
    language = models.TextField(null=True)
    meeting = models.TextField(null=True)
    month = models.TextField(null=True)
    note = models.TextField(null=True)
    number = models.TextField(null=True)
    number_of_cited_references = models.TextField(null=True)
    oa = models.TextField(null=True)
    orcid_numbers = models.TextField(null=True)
    organization = models.TextField(null=True)
    pages = models.TextField(null=True)
    publisher = models.TextField(null=True)
    researcherid_numbers = models.TextField(null=True)
    research_areas = models.TextField(null=True)
    series = models.TextField(null=True)
    times_cited = models.TextField(null=True)
    title = models.TextField(null=True)
    type = models.TextField(null=True)
    unique_id = models.TextField(null=True)
    usage_count_last_180_days = models.TextField(null=True)
    usage_count_since_2013 = models.TextField(null=True)
    volume = models.TextField(null=True)
    web_of_science_categories = models.TextField(null=True)
    year = models.TextField(null=True)
    authors_json = models.TextField(null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)

    class Meta:
        db_table = 'isi_documents'
        app_label = 'isi_documents'
