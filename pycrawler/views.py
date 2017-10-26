# coding=utf-8
import csv
import glob
import json
import time
import bibtexparser
import os

import sys

import math
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome import service as _service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from pycrawler.models import *
from settings import BASE_DIR

csv.field_size_limit(sys.maxsize)
DEFAULT_FOLDER = "E:\\Downloads"


class HomeView(TemplateView):
    template_name = 'home.html'

# region scopus
CHROME_DRIVER = os.path.join(BASE_DIR, 'chromedriver_win32', 'chromedriver')
CHROME_EXEC = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome'
SCOPUS_FOLDER = os.path.join(BASE_DIR, 'data', 'scopus')


# Lấy dữ liệu về tất cả các năm
class ScopusYearsView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        # init
        service = _service.Service(CHROME_DRIVER)
        service.start()
        capabilities = {
            'chrome.binary': CHROME_EXEC,
        }
        driver = webdriver.Remote(service.service_url, capabilities)

        # login
        driver.get("https://www.scopus.com")
        driver.find_element_by_css_selector('#paywall_username').send_keys("thuy221286@gmail.com")
        driver.find_element_by_css_selector('#paywall_password').send_keys("*IGVN3172")
        driver.find_element_by_css_selector('#paywall_login_submit_button_element').click()

        # search
        driver.find_element_by_css_selector('#searchterm1').send_keys('Viet Nam')
        driver.find_element_by_css_selector('#field1-button > span:first-child').click()
        driver.find_element_by_css_selector('#ui-id-12').click()
        driver.find_element_by_css_selector('#searchBtnRow > button').click()

        # show all year
        driver.find_element_by_css_selector('#viewAllLink_PUBYEAR').click()
        time.sleep(1)
        years = [int(x.get_attribute('value')) for x in driver.find_elements_by_css_selector('#overlayBody_PUBYEAR > ul > li > input:first-child')]
        doc_counts = [int(x.text.replace(',', '')) for x in driver.find_elements_by_css_selector('#overlayBody_PUBYEAR > ul > li > button > span:first-child > span:nth-child(2)')]
        selectors = ['#overlayBody_PUBYEAR label[for="%s"]' % x.get_attribute('id') for x in driver.find_elements_by_css_selector('#overlayBody_PUBYEAR > ul > li > input:first-child')]
        ScopusYear.objects.all().delete()
        for (year, doc_count, selector) in zip(years, doc_counts, selectors):
            ScopusYear.objects.create(year=year, doc_count=doc_count, selector=selector)

        return redirect(reverse('home'))


# Download các năm < 2000 bài
class ScopusLt2000View(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        # init
        service = _service.Service(CHROME_DRIVER)
        service.start()
        capabilities = {
            'chrome.binary': CHROME_EXEC,
        }
        driver = webdriver.Remote(service.service_url, capabilities)

        # login
        driver.get("https://www.scopus.com")
        driver.find_element_by_css_selector('#paywall_username').send_keys("thuy221286@gmail.com")
        driver.find_element_by_css_selector('#paywall_password').send_keys("*IGVN3172")
        driver.find_element_by_css_selector('#paywall_login_submit_button_element').click()

        for year in ScopusYear.objects.filter(doc_count__lte=2000, filename__isnull=True):
            # search
            driver.find_element_by_css_selector('#globalLinks > li:first-child > a').click()
            driver.find_element_by_css_selector('#searchterm1').clear()
            driver.find_element_by_css_selector('#searchterm1').send_keys('Viet Nam')
            driver.find_element_by_css_selector('#field1-button > span:first-child').click()
            driver.find_element_by_css_selector('#ui-id-12').click()
            driver.find_element_by_css_selector('#searchBtnRow > button').click()

            # show all year
            driver.find_element_by_css_selector('#viewAllLink_PUBYEAR').click()
            time.sleep(5)
            driver.find_element_by_css_selector(year.selector).click()
            driver.find_element_by_css_selector('#overlayFooter_PUBYEAR > div > input:first-child').click()
            time.sleep(1)

            driver.find_element_by_css_selector('label[for="allPageCheckBox"]').click()
            driver.find_element_by_css_selector('#directExport').click()

            default_path = os.path.join(DEFAULT_FOLDER, "scopus.csv")
            # wait for downloading finished
            while not os.path.exists(default_path):
                time.sleep(1)
            filename = "%d.csv" % year.year
            os.rename(default_path, os.path.join(SCOPUS_FOLDER, filename))
            year.filename = filename
            year.save()

        return redirect(reverse('home'))


# Lấy dữ liệu về tất cả các lĩnh vực của các năm > 2000 bài
class ScopusGt2000SubjectsView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        # init
        service = _service.Service(CHROME_DRIVER)
        service.start()
        capabilities = {
            'chrome.binary': CHROME_EXEC,
        }
        driver = webdriver.Remote(service.service_url, capabilities)

        # login
        driver.get("https://www.scopus.com")
        driver.find_element_by_css_selector('#paywall_username').send_keys("thuy221286@gmail.com")
        driver.find_element_by_css_selector('#paywall_password').send_keys("*IGVN3172")
        driver.find_element_by_css_selector('#paywall_login_submit_button_element').click()

        ScopusSubject.objects.all().delete()
        for year in ScopusYear.objects.filter(doc_count__gt=2000):
            # search
            driver.find_element_by_css_selector('#globalLinks > li:first-child > a').click()
            driver.find_element_by_css_selector('#searchterm1').clear()
            driver.find_element_by_css_selector('#searchterm1').send_keys('Viet Nam')
            driver.find_element_by_css_selector('#field1-button > span:first-child').click()
            driver.find_element_by_css_selector('#ui-id-12').click()
            driver.find_element_by_css_selector('#searchBtnRow > button').click()

            # show all year
            driver.find_element_by_css_selector('#viewAllLink_PUBYEAR').click()
            time.sleep(5)
            driver.find_element_by_css_selector(year.selector).click()
            driver.find_element_by_css_selector('#overlayFooter_PUBYEAR > div > input:first-child').click()
            time.sleep(3)

            # show all subjects
            driver.find_element_by_css_selector('#viewAllLink_SUBJAREA').click()
            time.sleep(5)
            names = [x.text for x in driver.find_elements_by_css_selector('#overlayBody_SUBJAREA > ul > li > label > span')]
            selectors = ['#overlayBody_SUBJAREA label[for="%s"]' % x.get_attribute('id') for x in driver.find_elements_by_css_selector('#overlayBody_SUBJAREA > ul > li > input:first-child')]
            for (name, selector) in zip(names, selectors):
                ScopusSubject.objects.create(name=name, selector=selector, year=year.year)

            # close
            driver.find_element_by_css_selector('#resultViewMoreModalMainContent_SUBJAREA [data-dismiss="modal"]').click()
            time.sleep(1)

        return redirect(reverse('home'))


# Download các lĩnh vực của các năm > 2000 bài
class ScopusGt2000DownloadView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        # init
        service = _service.Service(CHROME_DRIVER)
        service.start()
        capabilities = {
            'chrome.binary': CHROME_EXEC,
        }
        driver = webdriver.Remote(service.service_url, capabilities)

        # login
        driver.get("https://www.scopus.com")
        driver.find_element_by_css_selector('#paywall_username').send_keys("thuy221286@gmail.com")
        driver.find_element_by_css_selector('#paywall_password').send_keys("*IGVN3172")
        driver.find_element_by_css_selector('#paywall_login_submit_button_element').click()

        while ScopusSubject.objects.filter(export_status__isnull=True).exists():
            subject = ScopusSubject.objects.filter(export_status__isnull=True).first()
            # search
            driver.find_element_by_css_selector('#globalLinks > li:first-child > a').click()
            driver.find_element_by_css_selector('#searchterm1').clear()
            driver.find_element_by_css_selector('#searchterm1').send_keys('Viet Nam')
            driver.find_element_by_css_selector('#field1-button > span:first-child').click()
            driver.find_element_by_css_selector('#ui-id-12').click()
            driver.find_element_by_css_selector('#searchBtnRow > button').click()

            # show all year
            driver.find_element_by_css_selector('#viewAllLink_PUBYEAR').click()
            time.sleep(5)
            year = ScopusYear.objects.filter(year=subject.year).first()
            driver.find_element_by_css_selector(year.selector).click()
            driver.find_element_by_css_selector('#overlayFooter_PUBYEAR > div > input:first-child').click()
            time.sleep(3)

            excludes = ScopusSubject.objects.filter(year=subject.year, export_status='exported')
            # exclude exported subject
            if excludes.exists():
                # show all subjects
                driver.find_element_by_css_selector('#viewAllLink_SUBJAREA').click()
                time.sleep(5)

                for s in excludes:
                    driver.find_element_by_css_selector(s.selector).click()
                driver.find_element_by_css_selector('#overlayFooter_SUBJAREA > div > input:nth-child(2)').click()
                time.sleep(3)

            doc_count = int(driver.find_element_by_css_selector('.resultsCount').text.replace(',', ''))
            done = False
            if doc_count > 2000:
                # show all subjects
                driver.find_element_by_css_selector('#viewAllLink_SUBJAREA').click()
                time.sleep(5)

                driver.find_element_by_css_selector(subject.selector).click()
                driver.find_element_by_css_selector('#overlayFooter_SUBJAREA > div > input:first-child').click()
                time.sleep(3)
                doc_count = int(driver.find_element_by_css_selector('.resultsCount').text.replace(',', ''))
            else:
                done = True

            driver.find_element_by_css_selector('label[for="allPageCheckBox"]').click()
            driver.find_element_by_css_selector('#directExport').click()

            default_path = os.path.join(DEFAULT_FOLDER, "scopus.csv")
            # wait for downloading finished
            while not os.path.exists(default_path):
                time.sleep(1)
            filename = "%s.csv" % subject.name
            folder = os.path.join(SCOPUS_FOLDER, str(year.year))
            if not os.path.exists(folder):
                os.makedirs(folder)
            os.rename(default_path, os.path.join(folder, filename))
            subject.filename = filename
            subject.doc_count = doc_count
            subject.export_status = 'exported'
            subject.save()
            if done:
                ScopusSubject.objects.filter(year=subject.year, export_status__isnull=True).update(export_status="don't need")

        return redirect(reverse('home'))


SCOPUS_FIELD_NAMES = "Authors,Title,Year,Source title,Volume,Issue,Art. No.,Page start,Page end,Page count,Cited by,DOI,Link,Affiliations,Authors with affiliations,Abstract,Author Keywords,Index Keywords,Molecular Sequence Numbers,Chemicals/CAS,Tradenames,Manufacturers,Funding Details,Funding Text,References,Correspondence Address,Editors,Sponsors,Publisher,Conference name,Conference date,Conference location,Conference code,ISSN,ISBN,CODEN,PubMed ID,Language of Original Document,Abbreviated Source Title,Document Type,Source,EID".split(",")
SCOPUS_FIELD_KEYS = [x.lower().replace(".", "").replace("/", "_").replace(" ", "_") for x in SCOPUS_FIELD_NAMES]
SCOPUS_FIELDS = list(zip(SCOPUS_FIELD_KEYS, SCOPUS_FIELD_NAMES))


# Import csv -> DB các năm < 2000 bài
class ScopusImportLt2000View(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        for year in ScopusYear.objects.filter(filename__isnull=False, doc_count__lte=2000, status='processing'):
            ScopusDocument.objects.filter(year=year).delete()
            year.status = None
            year.save()

        for year in ScopusYear.objects.filter(filename__isnull=False, doc_count__lte=2000, status__isnull=True):
            print year.year
            year.status = 'processing'
            year.save()
            path = os.path.join(SCOPUS_FOLDER, year.filename)
            csvfile = open(path, 'r')
            reader = csv.DictReader(csvfile, SCOPUS_FIELD_NAMES)
            rows = [r for r in reader][1:]
            for row in rows:
                data = {k: row[v] for (k, v) in SCOPUS_FIELDS}
                ScopusDocument.objects.create(**data)
            year.status = 'done'
            year.save()

        return redirect(reverse('home'))


# Import csv -> DB các năm > 2000 bài
class ScopusImportGt2000View(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        for subject in ScopusSubject.objects.filter(filename__isnull=False, status='processing'):
            ScopusDocument.objects.filter(year=subject.year).delete()
            subject.status = None
            subject.save()

        for subject in ScopusSubject.objects.filter(filename__isnull=False, status__isnull=True):
            print subject.year, subject.name
            subject.status = 'processing'
            subject.save()
            path = os.path.join(SCOPUS_FOLDER, str(subject.year), subject.filename)
            csvfile = open(path, 'r')
            reader = csv.DictReader(csvfile, SCOPUS_FIELD_NAMES)
            rows = [r for r in reader][1:]
            for row in rows:
                data = {k: row[v] for (k, v) in SCOPUS_FIELDS}
                ScopusDocument.objects.create(**data)
            subject.status = 'done'
            subject.save()

        return redirect(reverse('home'))


class ScopusAuthorToJsonView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        for document in ScopusDocument.objects.filter(authors_json__isnull=True):
            print document.id
            authors = [
                {"first_name": author[0], "last_name": author[1] if len(author) >= 2 else None, "organize": author[2] if len(author) >= 3 else None}
                for author
                in [
                    str_author.split(', ', 2)
                    for str_author
                    in document.authors_with_affiliations.split("; ")
                    ]
            ]
            document.authors_json = json.dumps(authors)
            document.save()

        return redirect(reverse('home'))

# endregion

# region isi

ISI_FOLDER = os.path.join(BASE_DIR, 'data', 'isi')
FIREFOX_EXEC = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox'
FIREFOX_DRIVER = os.path.join(BASE_DIR, 'geckodriver-v0.19.0-win64', 'geckodriver')
SEARCHED_URL = 'http://apps.webofknowledge.com/Search.do?product=WOS&SID=U2OWYOQ4xSjnqzMy426&search_mode=GeneralSearch&prID=235f5bd2-62ed-4fc3-8226-d93983a11080'


class IsiPaginateView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        # init
        # To prevent download dialog
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', DEFAULT_FOLDER)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-bibtex')
        profile.set_preference('browser.helperApps.alwaysAsk.force', False)
        # set FF preference to socks proxy
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", "112.137.131.9")
        profile.set_preference("network.proxy.socks_port", 7778)
        profile.set_preference("network.proxy.socks_version", 5)
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        firefox_capabilities['binary'] = FIREFOX_EXEC
        driver = webdriver.Firefox(profile, capabilities=firefox_capabilities, executable_path=FIREFOX_DRIVER)

        if not IsiPaginate.objects.exists():
            driver.get(SEARCHED_URL)
            time.sleep(3)

            total = int(driver.find_element_by_css_selector('.title4 > span').text.replace(',', ''))
            page_size = 500.0
            page_count = int(math.ceil(total / page_size))
            pages = [
                {
                    "start": x*int(page_size) + 1,
                    "end": min((x+1)*int(page_size), total)
                } for x in range(page_count)
            ]
            for page in pages:
                IsiPaginate.objects.create(**page)

        # download
        for page in IsiPaginate.objects.filter(filename__isnull=True):
            # search
            driver.get(SEARCHED_URL)
            time.sleep(3)

            Select(driver.find_element_by_css_selector('#saveToMenu')).select_by_visible_text('Save to Other File Formats')
            time.sleep(1)
            driver.find_element_by_css_selector('#numberOfRecordsRange').click()
            driver.find_element_by_css_selector('#markFrom').send_keys(str(page.start))
            driver.find_element_by_css_selector('#markTo').send_keys(str(page.end))
            Select(driver.find_element_by_css_selector('#bib_fields')).select_by_visible_text('Full Record and Cited References')
            Select(driver.find_element_by_css_selector('#saveOptions')).select_by_visible_text('BibTeX')
            driver.find_element_by_css_selector('.quickoutput-action').click()

            default_path = os.path.join(DEFAULT_FOLDER, "savedrecs.bib")
            # wait for downloading finished
            while not os.path.exists(default_path):
                time.sleep(3)
            filename = "%d_%d.bib" % (page.start, page.end)
            folder = os.path.join(ISI_FOLDER)
            if not os.path.exists(folder):
                os.makedirs(folder)
            time.sleep(3)
            os.rename(default_path, os.path.join(folder, filename))

            page.filename = filename
            page.save()

        return redirect(reverse('home'))


class IsiKeyView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        for page in IsiPaginate.objects.filter(key_status__isnull=True):
            path = os.path.join(ISI_FOLDER, page.filename)
            print page.start, page.end
            with open(path) as bibtex_file:
                bibtex_str = bibtex_file.read().decode('latin1')
                bib_database = bibtexparser.loads(bibtex_str)
                for entry in bib_database.entries:
                    for key in entry.keys():
                        if key not in ["ENTRYTYPE", "ID"]:
                            key = key.replace("-", '_')
                            check = IsiKey.objects.filter(name=key)
                            if not check:
                                print key
                                IsiKey.objects.create(name=key)
                page.key_status = 'done'
                page.save()

        return redirect(reverse('home'))


class IsiImportView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        for page in IsiPaginate.objects.filter(status='processing'):
            IsiDocument.objects.filter(start=page.start, end=page.end).delete()
            page.status = None
            page.save()

        keys = [x.name for x in IsiKey.objects.all()]
        for page in IsiPaginate.objects.filter(status__isnull=True):
            page.status = 'processing'
            page.save()
            path = os.path.join(ISI_FOLDER, page.filename)
            print page.start, page.end
            with open(path) as bibtex_file:
                bibtex_str = bibtex_file.read().decode('latin1')
                bib_database = bibtexparser.loads(bibtex_str)
                for entry in bib_database.entries:
                    data = {k.replace('-', '_'): v for k, v in entry.items() if k.replace('-', '_') in keys}
                    data['start'] = page.start
                    data['end'] = page.end
                    IsiDocument.objects.create(**data)
                page.status = 'done'
                page.save()
        return redirect(reverse('home'))


class IsiAuthorJson(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        for document in IsiDocument.objects.filter(authors_json__isnull=True):
            print document.id
            l = map(self.map_row, document.affiliation.replace(' (Reprint Author)', '').replace('\\&', '&').split('.\n'))
            authors = [item for sublist in l for item in sublist]
            document.authors_json = json.dumps(authors)
            document.save()
        return redirect(reverse('home'))

    def map_row(self, row):
        parts = row.split('; ')
        last = parts[len(parts) - 1]
        last_author = self.parse_author(last)
        authors = map(self.parse_author, parts)
        for author in authors:
            author['organize'] = last_author['organize']
        return authors

    def parse_author(self, s):
        parts = s.split(', ')
        return {
            "first_name": parts[0],
            "last_name": parts[1] if len(parts) >= 2 else None,
            "organize": parts[2] if len(parts) >= 3 else None,
        }

# endregion
