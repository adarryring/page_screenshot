#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_screenshot.run_factory import run, run_for_url_list

if __name__ == '__main__':
    # run('https://baidu.com')
    # run_for_url_list('./url_list.txt', count_thread=2)
    # run_for_url_list('./url_list.txt', count_thread=1)
    # run_for_url_list('./url_list.txt', count_thread=3)
    run_for_url_list('./url_list.txt')
