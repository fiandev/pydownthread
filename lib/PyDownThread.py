from concurrent.futures import ThreadPoolExecutor
from utils.functions import download_url

class PyDownThread:
  def __init__(self, resources: list, output: str = "."):
      self.resources = resources
      self.workers = 5
  def setWorkers (amount: int):
      self.workers = amount
  def start (self):
      def runner (resource: list):
          try:
            filename = resource.split("/").pop()
            download_url(resource, f"{ self.output }/{ filename }")
          except Exception as err:
            print(err)
      with ThreadPoolExecutor(max_workers=self.workers) as executor:
          executor.map(runner, self.resources)