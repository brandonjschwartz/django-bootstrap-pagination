# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

readme = open('README.rst', 'r')
readme_text = readme.read()
readme.close()

setup(
    name='django-bootstrap-pagination',
    version='1.5.1',
    keywords="django bootstrap pagination templatetag",
    author=u'Jason McClellan',
    author_email='jason@jasonmccllelan.net',
    contributor='Brandon J. Schwartz',
    contributor_email='brandon@boomajoom.com',
    packages=find_packages(),
    url='https://github.com/brandonjschwartz/django-bootstrap-pagination',
    license='MIT licence, see LICENCE',
    description='Render Django Page objects as Bootstrap 3.x Pagination compatible HTML, upgraded for py3',
    # long_description=readme_text.encode('UTF-8'),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",        
    ]
)
