from setuptools import setup, find_packages

version = __import__('pinax').__version__

setup(
    name='Pinax',
    version=version,
    description='Pinax is an open-source collection of re-usable apps for the Django Web Framework',
    long_description=open('docs/intro.txt').read(),
    author='James Tauber',
    author_email='jtauber@jtauber.com',
    maintainer='Jannis Leidel',
    maintainer_email='jannis@leidel.info',
    url='http://pinaxproject.com/',
    packages=find_packages(),
    include_package_data=True,
    # Ignore the tarballs we built our own in a source distribution
    exclude_package_data={
        'requirements': ['%s/*.tar.gz' % version],
    },
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pinax-admin = pinax.core.management:execute_from_command_line',
        ],
        'setuptools.file_finders': [
            'dummy = file_finder:dummylsfiles',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: JavaScript',
    ],
)
