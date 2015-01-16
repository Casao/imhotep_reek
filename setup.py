from setuptools import setup, find_packages

setup(
    name='imhotep_reek',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/casao/imhotep_reek',
    license='MIT',
    author='Colin Ewen',
    author_email='colin@draecas.com',
    description='An imhotep plugin for reek code analysis tool',
    entry_points={
        'imhotep_linters': [
            '.py = imhotep_reek.plugin:RubyReek'
        ],
    },
)