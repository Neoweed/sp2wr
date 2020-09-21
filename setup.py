import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'sp2wr',
      packages = ['sp2wr'],
      version='0.1',
      license='none',
      description='Convert Spoken English given as text to Written English ',
      author='Akhilank Kaipu',
      author_email='akhilank.kaipu@iiitb.org',
      #url='https://github.com/cyberdhiman/Spoken-To-Written-English',
      classifiers = [
     					 'Intended Audience :: Agnaitha',
      					'Programming Language :: Python'
  				],
	  #long_description=open_file('README.rst').read()

     )