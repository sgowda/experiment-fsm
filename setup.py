from distutils.core import setup

setup(
  name = 'experiment_fsm',         # How you named your package folder (MyLib)
  packages = ['experiment_fsm'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Pythonic finite state machine',   # Give a short description about your library
  author = 'James Gao, Helene Moorman, Suraj Gowda',                   # Type in your name
  url = 'https://github.com/sgowda/experiment-fsm',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sgowda/experiment-fsm/archive/v0.1.tar.gz',    # I explain this later on
  keywords = ['State machine'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 2.7',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
