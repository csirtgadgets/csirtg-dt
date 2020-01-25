import os
from setuptools import setup, find_packages
import versioneer
import sys

# https://www.pydanny.com/python-dot-py-tricks.html
if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'coverage',
        'pytest_cov',
    ]

    try:
        modules = map(__import__, test_requirements)

    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirements." % err_msg
        raise ImportError(msg)

    r = os.system('py.test test -v --cov=csirtg_dt --cov-fail-under=0 --pep8')

    if r == 0:
        sys.exit()
    else:
        raise RuntimeError('tests failed')

setup(
    name="csirtg-dt",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="CSIRTG DateTime Utils",
    long_description="",
    url="https://github.com/csirtgadgets/csirtg-dt",
    license='MPL2',
    classifiers=[
               "Programming Language :: Python",
               ],
    keywords=['security'],
    author="Wes Young",
    author_email="wes@csirtgadgets.com",
    packages=find_packages(),
    install_requires=[
        'arrow'
    ],
    scripts=[],
    entry_points={
        'console_scripts': [
            'csirtg-dt=csirtg_dt:main'
        ]
    },
)
