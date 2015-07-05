from setuptools import setup

setup(name='KittyBot',
      version='0.1',
      description='A utility for controlling the KittyBot cat toy',
      url='https://github.com/Hernrup/KittyBot',
      author='Mikael Hernrup',
      author_email='mikael@hernrup.se',
      license='MIT',
      packages=[],
      install_requires=[
          'CherryPy==3.7.0',
          'Flask==0.10.1',
          'pyreadline==2.0',
          'watchdog==0.8.3'
          ],
      tests_require=['nose'],
      scripts=['bin/kittyBot.py'],
      zip_safe=False)