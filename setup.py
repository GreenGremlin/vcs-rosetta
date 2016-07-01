from setuptools import setup

setup(name='vcs-rosetta',
      description='Version Control System translator',
      author='Jonathan Felchlin',
      author_email='jonathan@xgecko.com',
    #   url='https://www.',
      packages=['translator'],
      package_data={'translator': ['data/*.yaml']},
      scripts=[
          'scripts/g2h',
          'scripts/h2g'
      ]
)
