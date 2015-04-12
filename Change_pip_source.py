# -*- coding:utf-8 -*-
from os.path import expanduser
from platform import system
from ConfigParser import ConfigParser

__author__ = VicYu


def modifyPipSource(url, path='~'):
    '''
        缺少 多源支持
    '''
    # Judge OS type
    if system() == 'Windows':
        path = expanduser(path) + '\pip\pip.ini'
    elif system() == 'Linux':
        path = expanduser(path) + '/.pip/pip.conf'
    else:
        print 'Sorry, Not known Operation System'

    # Write setting
    with open(path, 'w') as f:
        conf = ConfigParser()
        conf.add_section('global')
        conf.set('global', 'index-url', url)
        conf.write(f)


if __name__ == '__main__':
    src = 'http://pypi.douban.com/simple'   # 豆瓣源
    modifyPipSource(src)
