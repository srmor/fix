from setuptools import setup, find_packages


setup(name='thefix',
      version=1.7,
      description="Magnificent app which corrects your previous console command with an appropriate name",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/thefix',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['pathlib'],
      entry_points={'console_scripts': [
          'thefix = thefix.main:main']})
