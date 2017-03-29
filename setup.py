from setuptools import setup, find_packages

setup(
    name='colonias playground',
    classifiers=[
        'Development Status :: 0 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: pygame',
        'Topic :: Games/Entertainment :: Arcade',
    ],
    # data_files=[('.', ['alembic.ini'])],
    license='GPL-3.0',
    author='Chase',
    author_email='',
    maintainer='',
    maintainer_email='',
    description='',
    include_package_data=True,
    long_description='',
    package_dir={'colonia': 'src'},
    packages=find_packages(),
    # package_data={'solarwolf': []},
    url='',
    install_requires=['pygame'],
    version='1.6.0a4',
    entry_points={
        'console_scripts': [
            'solarwolf=solarwolf.cli:main',
        ],
    },
)
