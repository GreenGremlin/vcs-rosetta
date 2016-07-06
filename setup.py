from setuptools import setup

setup(name='vcsrosetta',
      description='Version Control System translator - includes g2h (git to hg) and h2g (hg to git)',
      author='Jonathan Felchlin',
      author_email='jonathan@xgecko.com',
      url = 'https://github.com/GreenGremlin/vcs-rosetta',
      download_url = 'https://github.com/GreenGremlin/vcs-rosetta/tarball/0.1',
      packages=['vcsrosetta'],
      package_data={'vcsrosetta': ['data/git_hg.yaml']},
      scripts=[
          'scripts/g2h',
          'scripts/h2g'
      ],
      version = '0.1',
      keywords = ['git', 'mercurial', 'hg', 'rosetta'], # arbitrary keywords
      classifiers = []
)
