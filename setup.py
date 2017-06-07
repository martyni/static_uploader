from setuptools import setup
from pip.req import parse_requirements
import app

install_reqs = parse_requirements('requirements.txt', session=False)

reqs = [ str(i.req) for i in install_reqs ]

setup(name='app',
      version="v0.0.4",
      description='app',
      url='http://github.com/martyni/jenkins_test',
      author='martyni',
      author_email='martynjamespratt@gmail.com',
      license='MIT',
      install_requires=reqs,
      packages=['app'],
      zip_safe=False,
      entry_points = {
               'console_scripts': ['boop=app:app.run'],
                  },
      include_package_data=True
      )
