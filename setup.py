from setuptools import setup, find_packages

setup(
    name='buttersalt_saltapi',
    description='The ButterSalt wrapper around the salt-api',
    version='1.0.3',
    author='lfzyx',
    author_email='lfzyx.me@gmail.com',
    url='https://github.com/lfzyx/ButterSalt-saltapi',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    python_requires='>=3.6.4',
    install_requires=[
          'requests',
      ],
    keywords='buttersalt saltapi',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

)
