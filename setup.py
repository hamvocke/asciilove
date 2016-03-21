from setuptools import setup

setup(name='asciilove',
        version='0.0.1',
        description='Convert images to ASCII art in your command line',
        url='https://github.com/hamvocke/asciilove',
        author='Hermann Vocke',
        author_email='ham@hamvocke.com',
        license='MIT',
        packages=['asciilove'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Artistic Software',
            ],
        keywords='ascii art asciiart',
        install_requires=[
            'wand'
        ],
        entry_points={
            'console_scripts': ['asciilove=asciilove.commandline:main'],    
        }
    )
