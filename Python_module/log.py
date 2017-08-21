# -*- coding: utf-8 -*-
import os
import sys
import datetime
import platform


class log:
    def __init__(self, file_name, prints=False):
        self.br = '\n'
        if platform.system() is 'Windows':
            self.br = '\r\n'

        self.prints = prints

        # _logFolder = sys.path[0] + '/logs/'
        _logFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + '/logs/'

        if not os.path.isdir(_logFolder):
            os.mkdir(_logFolder)
        self.log_file = _logFolder + file_name
        print('LogFolder: %s' % self.log_file)

    def _write_log(self, log):
        _tmp_time = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

        if os.path.exists(self.log_file):
            if os.path.getsize(self.log_file) / 1024 / 1024 > 10:
                new_name = self.log_file + '.' + str(
                    len([f for f in os.listdir(os.path.dirname(self.log_file)) if 'log' in f]))
                os.renames(self.log_file, new_name)

        if self.prints:
            print ('%s %s' % (_tmp_time, log))

        with open(self.log_file, 'a') as f:
            f.write('%s %s %s' % (_tmp_time, log, self.br))
        f.close()

    def INFO(self, info):
        self._write_log('INFO: %s' % info)

    def WARNING(self, warning):
        self._write_log('WARNING: %s' % warning)

    def ERROR(self, error):
        self._write_log('ERROR: %s' % error)


if __name__ == '__main__':
    l = log('kk.log', True)
    l.INFO('info')
    l.WARNING('warning')
    l.ERROR('error')
