import urllib.request
from lib.DownloadProgressBar import DownloadProgressBar

def download_url(url: str, output_path: str):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
      urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)