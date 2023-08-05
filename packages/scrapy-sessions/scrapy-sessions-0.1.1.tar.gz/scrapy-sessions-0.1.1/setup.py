import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='scrapy-sessions',
    version='0.1.1',
    author='Thomas Aitken',
    author_email='tclaitken@gmail.com',
    description='Session management extension for Scrapy.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ThomasAitken/scrapy-sessions',
    packages=[
        'scrapy_sessions',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ]
)
