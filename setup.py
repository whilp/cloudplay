from distutils.core import setup

meta = dict(
    name='cloudplay',
    version='0.1',
    description='play the cloud',
    long_description='Build playlists of tracks published on cloud services.',
    author='Will Maier',
    author_email='wcmaier@m.aier.us',
    url='http://github.com/wcmaier/cloudplay',
    install_requires=['lxml', 'requests'],
    scripts=["cloudplay"],
    license='ISC',
    classifiers=(
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)

setup(**meta)
