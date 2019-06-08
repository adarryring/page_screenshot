#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: page screenshot
@author: xiaohong
@time: 2019-06-07
@feature: a complete capture from a web page
"""

from page_screenshot.model.model import PageScreenshotModel, OUTER_PC_WIDTH, OUTER_PHONE_WIDTH
from page_screenshot.index import PageScreenshot


def run(url, responsive_height=None):
    """
    run

    :param responsive_height: responsive_height
    :param url: url
    :return: void
    """
    screenshot_for_pc_and_phone(url, responsive_height)


def screenshot_for_pc_and_phone(url, responsive_height=None):
    """
    pc and phone

    :param responsive_height: responsive_height
    :param url: url
    :return: void
    """
    page_screenshot_model = screenshot_for_pc(url=url, responsive_height=responsive_height)
    page_screenshot = PageScreenshot(page_screenshot_model)
    screenshot(page_screenshot_model, page_screenshot)

    page_screenshot_model = screenshot_for_phone(page_screenshot_model=page_screenshot_model, responsive_height=responsive_height)
    screenshot(page_screenshot_model, page_screenshot)

    page_screenshot.close()


def screenshot_for_pc(url=None, page_screenshot_model=None, responsive_height=None):
    """
    pc

    :param responsive_height: responsive_height
    :param url: url
    :param page_screenshot_model: model
    :return: page_screenshot_model
    """
    if page_screenshot_model is None:
        page_screenshot_model = PageScreenshotModel.build(url)
    if responsive_height is not None:
        page_screenshot_model.init_height = responsive_height
    page_screenshot_model.set_outer_width(OUTER_PC_WIDTH)
    return page_screenshot_model


def screenshot_for_phone(url=None, page_screenshot_model=None, responsive_height=None):
    """
    phone

    :param responsive_height: responsive_height
    :param url: url
    :param page_screenshot_model: model
    :return: page_screenshot_model
    """
    if page_screenshot_model is None:
        page_screenshot_model = PageScreenshotModel.build(url)
    if responsive_height is not None:
        page_screenshot_model.init_height = responsive_height
    page_screenshot_model.set_outer_width(OUTER_PHONE_WIDTH)
    page_screenshot_model.add_to_js_file_name('phone')
    return page_screenshot_model


def screenshot(page_screenshot_model=None, page_screenshot=None):
    """
    screenshot now

    :param page_screenshot_model: model
    :param page_screenshot: page_screenshot
    :return:
    """
    if page_screenshot is None:
        PageScreenshot(page_screenshot_model).capture()
    else:
        page_screenshot.use_driver(page_screenshot_model).capture()
