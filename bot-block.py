from pywikibot import pagegenerators, Site, Category
from datetime import datetime, timezone
import re

wikinews = Site('es', 'wikinews')

def latest_pages() -> list:
    """
    Gets the latest available pages. Consider that these pages are only the last 30 days.

    :return list(Page)
    """
    return list(filter(lambda page: not page.isRedirectPage(), pagegenerators.NewpagesPageGenerator(site=wikinews, namespaces=[0])))

def all_published_pages() -> list:
    """
    Gets all pages, regardless of the creation date.

    :return list(Page)
    """
    return list(pagegenerators.CategorizedPageGenerator(Category(wikinews, title='Category:Artículos publicados'), namespaces=[0]))

def filter_unprotected(pages: list, days: int) -> list:
    """
    Filters unprotected pages that haven't been edited for more than X days.
    """
    now_utc = datetime.now(timezone.utc)
    return list(filter(lambda page: 'edit' not in page.protection() and abs((page.latest_revision.timestamp.astimezone(timezone.utc) - now_utc).days) > days, pages))

if __name__ == '__main__':
    pages_to_process = filter_unprotected(all_published_pages(), 7)
    for page in pages_to_process:
        print(f"<< {page.title()}")
        try:
            page.protect(reason="Política de archivado", protections={'edit': 'sysop', 'move': 'sysop'})
            text = page.get()
            text = re.sub(r'\{\{\s*[Pp]ublicad[oa]\s*\}\}', '{{publicado}}', text)
            text = re.sub(r'\{\{\s*[Aa]rchivad[oa]\s*\}\}', '{{archivada}}', text)
            text = text.replace('{{publicado}}{{archivada}}', "{{publicado}}\n{{archivada}}")
            if '{{publicado}}' in text and '{{archivada}}' not in text:
                text = text.replace('{{publicado}}', "{{publicado}}\n{{archivada}}")
            page.put(text, summary="Estandarización de plantillas {{archivada}} y {{publicado}}")
            print(f">>> {page.title()} protegida")
        except Exception as e:
            print(f"[!] {page.title()}: {e}")
