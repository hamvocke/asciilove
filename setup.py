from setuptools import setup

setup(name='asciilove',
        version='0.1',
        description='Convert images to ASCII art in your command line',
        url='https://github.com/hamvocke/asciilove',
        author='Hermann Vocke',
        author_email='ham@hamvocke.com',
        license='MIT',
        packages=['asciilove'],
        install_requires=[
            'wand'
        ],
        entry_points={
            'console_scripts': ['asciilove=asciilove.commandline:main'],    
        }
    )
