# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import csv
import datetime as dt
from pathlib import Path

# useful for handling different item types with a single interface

BASE_DIR = Path(__file__).parent.parent

FIELDS = ('Статус', 'Количество')
DIR = 'results'
DT = '%Y-%m-%dT%H-%M-%S'
FILE = 'status_summary_{time}.csv'
TIME_NOW = dt.datetime.now().strftime(DT)


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = {}
        self.result_dir = BASE_DIR / DIR
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        pep_status = item['status']
        if self.results.get(pep_status):
            self.results[pep_status] = self.results[pep_status]+1
        else:
            self.results[pep_status] = 1
        return item

    def close_spider(self, spider):
        file_dir = self.result_dir / FILE.format(
            time=TIME_NOW
        )
        with open(file_dir, mode="w", encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow((FIELDS))
            for key, value in self.results.items():
                writer.writerow([key, value])
            writer.writerow(['Total', sum(self.results.values())])
