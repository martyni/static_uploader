from setuptools import setup
from pip.req import parse_requirements
import app

install_reqs = parse_requirements('requirements.txt', session=False)

reqs = [ str(i.req) for i in install_reqs ]

setup(name='static_static',
      version="v0.0.4",
      description='simple s3 file uploader',
      url='http://github.com/martyni/static_uploader',
      author='martyni',
      author_email='martynjamespratt@gmail.com',
      license='MIT',
      install_requires=reqs,
      packages=['app'],
      zip_safe=False,
      entry_points = {
               'console_scripts': ['s3_static=app:app.put_files'],
                  },
      include_package_data=True
      )
