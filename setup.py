from setuptools import find_packages, setup

setup(
    name='flat-simple',
    packages=find_packages(include=['flat_me']),
    version='0.1.0',
    description='Literally just a test library',
    author='Me',
    license='MIT',
    install_requires=['PyInquirer','pyfiglet','pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    entry_points= {'console_scripts': ['flat_me=flat_me.user_prompt:main']}
)