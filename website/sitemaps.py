from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class MySitemap(Sitemap):
    def items(self):
        # Define the URLs to be included in the sitemap
        return ['about-us', 'job-seeker', 'contact-us', 'find-jobs']  # Replace these with your actual URL names

    def location(self, item):
        # Return the URL for each item in the sitemap
        return reverse(item)