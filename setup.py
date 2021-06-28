from setuptools import setup

setup(name='docx-mailmerge-conted',
      version='0.5.1',
      description='Performs a Mail Merge on docx (Microsoft Office Word) files',
      long_description=open('README.rst').read(),
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Text Processing',
      ],
      author='Tim Nyborg',
      author_email='tim.nyborg@conted.ox.ac.uk',
      url='http://github.com/timnyborg/docx-mailmerge',
      license='MIT',
      py_modules=['mailmerge'],
      zip_safe=False,
      install_requires=['lxml']
)
