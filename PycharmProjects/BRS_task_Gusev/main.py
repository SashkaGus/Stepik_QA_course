import os
import logging
from datetime import datetime
import shutil
import zipfile

logging.basicConfig(level=logging.DEBUG, filename='transfer.log', format='%(asctime)s %(levelname)s: %(message)s')


class FileTrans:
    def __init__(self, path):
        self.path = path
        self.file_cr_date = None

    def file_old(self):
        cur_date = datetime.now().date()
        self.file_cr_date = datetime.strptime(self.path[::-1][:10][::-1], '%Y/%m/%d').date()
        delta = cur_date - self.file_cr_date
        logging.debug('Сheck the file creation time %d days', delta.days)
        return True if delta.days > 90 else False

    def disk_usage(self):
        total, used, free = shutil.disk_usage(self.path)
        total = total // (2 ** 30)
        free = free // (2 ** 30)
        logging.debug('Check disk space %d', round(free / total * 100, 2))
        return True if round(free / total * 100, 2) < 10 else False

    def transfer(self):
        if self.file_old() and self.disk_usage():
            os.chdir(self.path)
            arch_folder = os.path.join('archive', str(self.file_cr_date).replace('-', '/'))
            os.makedirs(arch_folder)
            arch_filename = str(self.file_cr_date)
            logging.debug('Creating archive file %s', arch_filename)
            with zipfile.ZipFile(arch_filename, 'w') as zpf:
                for dirpath, dirnames, filenames in os.walk(self.path):
                    for name in dirnames:
                        new_path = os.path.normpath(os.path.join(dirpath, name))
                        zpf.write(new_path, os.path.relpath(new_path, self.path))
                    for name in filenames:
                        new_path = os.path.normpath(os.path.join(dirpath, name))
                        if os.path.isfile(new_path):
                            zpf.write(new_path, os.path.relpath(new_path, self.path))
            shutil.move(arch_filename, arch_folder)