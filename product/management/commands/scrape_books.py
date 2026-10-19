import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from product.models import Product
from decimal import Decimal
from urllib.parse import urljoin


class Command(BaseCommand):
    def handle(self, *args, **options):
        base_url = 'https://books.toscrape.com/'
        catalogue_url = urljoin(base_url, 'catalogue/page-1.html')

        self.stdout.write('scraping')

        response = requests.get(catalogue_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.select('article.product_pod h3 a')
        self.stdout.write(f'Found {len(books)} books on the first page')

        for book in books:
            relative_link = book.get('href')
            detail_url = urljoin(catalogue_url, relative_link)
            self.scrape_book_detail(detail_url)

        self.stdout.write(self.style.SUCCESS('Scraping finished!'))

    def scrape_book_detail(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Name
            name = soup.select_one('div.product_main h1').text.strip()

            # Price
            import re
            price_tag = soup.select_one('p.price_color')
            price_text = price_tag.text if price_tag else '0'
            price_match = re.search(r'[\d.]+', price_text)
            if price_match:
                price = Decimal(price_match.group())
            else:
                price = Decimal('0.00')

            # Description
            description_tag = soup.select_one('#product_description')
            if description_tag and description_tag.find_next_sibling('p'):
                description = description_tag.find_next_sibling('p').text.strip()
            else:
                description = 'No description'

            # Stock
            availability = soup.select_one('p.instock.availability')
            stock_text = availability.text.strip() if availability else '0'
            stock = 0
            for word in stock_text.split():
                if word.isdigit():
                    stock = int(word)
                    break

            # Save or update
            product, created = Product.objects.update_or_create(
                name=name,
                defaults={
                    'description': description,
                    'price': price,
                    'stock': stock,
                    'is_digital': False,
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {name}'))
            else:
                self.stdout.write(f'Updated: {name}')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error scraping {url}: {e}'))