from setuptools import setup

setup(name='vcsrosetta',
      description='Version Control System translator - includes g2h (git to hg) and h2g (hg to git)',
      author='Jonathan Felchlin',
      author_email='jonathan@xgecko.com',
      url='https://github.com/GreenGremlin/vcs-rosetta',
      download_url='https://github.com/GreenGremlin/vcs-rosetta/tarball/0.1',
      packages=['vcsrosetta'],
      package_data={'vcsrosetta': ['data/git_hg.yaml']},
      scripts=[
          'scripts/g2h',
          'scripts/h2g'
      ],
      version='0.1.2',
      license='MIT',
      keywords=['git', 'mercurial', 'hg', 'rosetta', 'translate', 'translation'], # arbitrary keywords
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Documentation',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ]
)
