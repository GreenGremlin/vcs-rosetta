from setuptools import setup

setup(name='vcsrosetta',
      description='Version Control System translator - includes g2h (git to hg) and h2g (hg to git)',
      author='Jonathan Felchlin',
      author_email='jonathan@xgecko.com',
    #   url='https://www.',
      packages=['vcsrosetta'],
      package_data={'vcsrosetta': ['data/git_hg.yaml']},
      scripts=[
          'scripts/g2h',
          'scripts/h2g'
      ]
)
