import discogs_client

from collections import namedtuple
import re


class JARSDiscogsClient:

    def __init__(self, user_choices):
        self.user_choices = user_choices
        self.client = discogs_client.Client('Blaaah', user_token='dvZQgnADMOHEjxZSbgZtbYTDKCxlbyvWxpRndIYh')

    def query_database(self):

        results = self.client.search('', **self.user_choices)
        if self.user_choices.get('sort'):
            results.sort()  #TODO: Implement

        return DiscogsResults(results)


class DiscogsPageResults:

    def __init__(self, results):
        self.results = results
        self.page_numbers = results.pages

    def __iter__(self):
        self.page = 1
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.page <= self.page_numbers:
            page_results = self.results.page(self.page)
            clean_page_results = self.clean_results(page_results)
            self.page += 1
            return clean_page_results
        else:
            raise StopIteration()

    def clean_results(self, page_results):

        Release = namedtuple('Release', ['artist', 'release'])
        clean_results = []

        str_results = [str(result) for result in page_results]  # Done to avoid making request to API for every release

        for str_result in str_results:
            artist, release = self.extract_artist_release(str_result)
            clean_results.append(Release(artist, release))

        return clean_results

    def extract_artist_release(self, str_result):
        regex_extract_artist_release = "^<Release [\d]{1,10} [\"\'](.*)[\"\']>$"
        match_object = re.match(regex_extract_artist_release, str_result)

        artist_release = match_object.group(1)

        artist, release = self.split_artist_and_release(artist_release)
        artist = self.remove_discogs_tag_from_artist(artist)

        return artist, release

    def split_artist_and_release(self, artist_release):
        artist_release_list = artist_release.split(' - ')

        artist = artist_release_list[0]
        release = ' - '.join(artist_release_list[1:])

        return artist, release

    def remove_discogs_tag_from_artist(self, artist):
        """
        Artist (7) -> Aritst
        :param artist: String Artist
        :return: String Artist without tags
        """
        artist_regex = '(.*)( \(\d+\))?'
        match_object = re.match(artist_regex, artist)

        artist_no_tags = match_object.group(1)

        return artist_no_tags


class DiscogsResults:

    def __init__(self, results):
        self.page_results_client = iter(DiscogsPageResults(results))

    def __iter__(self):
        self.page_results = []
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self.page_results) == 0:
            self.page_results = next(self.page_results_client)
            return self.page_results.pop(0)
        else:
            return self.page_results.pop(0)

