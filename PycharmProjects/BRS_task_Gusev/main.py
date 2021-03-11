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
        try:
            self.file_cr_date = datetime.strptime(self.path[::-1][:10][::-1], '%Y/%m/%d').date()
        except ValueError:
            logging.error(ValueError.args)
            print('Invalid path')
            return 0

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
        if self.file_old() or self.disk_usage():
            try:
                os.chdir(self.path.split('/')[-5])  # choose arch directory
            except IndexError:
                path_len = len(self.path.split('/'))
                os.chdir(self.path.split('/')[-path_len])
            arch_folder = os.path.join('archive', str(self.file_cr_date).replace('-', '/'))
            try:
                os.makedirs(arch_folder)
            except FileExistsError:
                shutil.rmtree(arch_folder, ignore_errors=True)  # remove dir
                os.makedirs(arch_folder)
            for dirpath, dirnames, filenames in os.walk(self.path):
                for name in filenames:
                    if name.endswith('.mp3') or name.endswith('.wav'):
                        with zipfile.ZipFile(arch_folder + '/' + name[:-4] + '.zip', 'w') as zpf:
                            new_path = os.path.normpath(os.path.join(dirpath, name))
                            zpf.write(new_path, os.path.relpath(new_path, self.path),
                                      compress_type=zipfile.ZIP_DEFLATED)
                            os.remove(new_path)


if __name__ == '__main__':
    user_path = input("Enter path in format: <dir>/year/month/day: ")
    new_trans = FileTrans(user_path)
    new_trans.transfer()
