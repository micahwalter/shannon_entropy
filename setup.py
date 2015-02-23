from setuptools import setup

setup(name='shannon_entropy',
      version='0.2',
      description='Calculate the Shannon Entropy for an image.',
      url='http://github.com/micahwalter/shannon_entropy',
      author='Micah Walter',
      author_email='micah@micahwalter.com',
      license='MIT',
      packages=['shannon_entropy'],
      install_requires=[
          'Pillow',
      ],
      zip_safe=False)
