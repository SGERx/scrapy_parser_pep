import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

FIELDS = ('Статус', 'Количество')
DIR = 'results'
DT = '%Y-%m-%dT%H-%M-%S'
FILE = 'status_summary_{time}.csv'
TIME_NOW = dt.datetime.now().strftime(DT)


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = defaultdict(int)
        self.result_dir = BASE_DIR / DIR
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
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
