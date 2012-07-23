import os

from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'PasteScript>=1.3',
    ]

setup(name='w20e.buildoutskel',
      version='1.0.0a',
      description='Paster template',
      long_description="",
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Wyldebeast & Wunderliebe',
      author_email='info@w20e.com',
      url='',
      keywords='buildout',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require= requires,
      entry_points = """\
      [paste.paster_create_template]
      buildout=w20e.buildoutskel:BuildoutSkel
      """,
      )

