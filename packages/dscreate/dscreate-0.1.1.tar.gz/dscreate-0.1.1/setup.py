from setuptools import setup, find_packages

setup(name='dscreate',
      version='0.1.1',
      description='Flatiron Iron School Data Science Tools',
      url='http://github.com/learn-co-curriculum/dscreate',
      author='Joél Collins',
      author_email='joelsewhere@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['argparse', 'pyperclip'],
      scripts=['bin/ds'],
      zip_safe=False)