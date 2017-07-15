#  ______         _____ _  __  _____        _____ ______ 
# |___  /   /\   / ____| |/ / |  __ \ /\   / ____|  ____|
#    / /   /  \ | |    | ' /  | |__) /  \ | |    | |__   
#   / /   / /\ \| |    |  <   |  ___/ /\ \| |    |  __|  
#  / /__ / ____ \ |____| . \  | |  / ____ \ |____| |____ 
# /_____/_/    \_\_____|_|\_\ |_| /_/    \_\_____|______|
#
#
# Programmed by Zack Pace under the Apache License.
#
# MODULET 2017 (1.0.0)
                                                        
                                                        

from setuptools import setup, find_packages



setup(
  name="modulet",
  version="1.0",
  description="A web framework for use with python.  Inspired by the following: readthedocs.org(github)"
  author="Zack Pace",
  author_email="zack@zacklearns.com",
  url="symphmc.com",
  packages=findpackages(),
  include_package_data=True,
  zip_safe=False,
  classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: None',
    ],
 )
