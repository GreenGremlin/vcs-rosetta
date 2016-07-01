from setuptools import setup

setup(name='vcs-rosetta',
      description='Version Control System translator',
      author='Jonathan Felchlin',
      author_email='jonathan@xgecko.com',
    #   url='https://www.',
      packages=['translator'],
      data_files=[('translations', ['translator/translations/git_hg.yaml'])],
      scripts=[
          'scripts/g2h',
          'scripts/h2g'
      ]
      # entry_points = {
      #     'console_scripts': [
      #         'g2h = vcs-rosetta.g2h:main',
      #         'h2g = vcs-rosetta.h2g:main'
      #     ]
      # }
)
