# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docrunner', 'docrunner.languages', 'docrunner.utils']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0', 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['docrunner = docrunner.main:app']}

setup_kwargs = {
    'name': 'docrunner',
    'version': '0.1.2',
    'description': 'A command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.',
    'long_description': "## DocRunner\n\nA command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.\n\n## What does it do?\n\nDocrunner goes through your markdown file and runs any code in it, providing you safe testing for any markdown documentation. You can specify the path to the markdown file, along with other options, with flags.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install docrunner.\n\n```bash\npip install docrunner\n```\n\n## QuickStart\n\n```cmd\npy -m docrunner --help\n```\n\nor\n\n```cmd\ndocrunner\n```\n\n### Python Example\n\n```cmd\ndocrunner python --markdown-path ./README.md --multi-file\n```\n\nThis command executes all python within your README markdown file and does so by putting each snippet of python from your README into a separate file, and running each file. If you don't want each snippet in a separate python file, just remove the --multi-file option.\n\n\n## Contributing and Local Development\nIf you would like to contribute to `docrunner` and develop locally on your system, please follow the following instructions\nto set a local development environment for docrunner on your system\n\n1. Install `poetry`, a dependency management tool, with `pip` if it is not already installed:\n```powershell\npip install poetry\n```\n2. Install the necessary packages for the project with:\n```powershell\npoetry install\n```\n3. To run the docrunner cli tool, run:\n```powershell\npoetry run docrunner --help\n```\n4. You're all set! You can now edit source code within the `docrunner` directory\n5. (Testing CLI Tool) Run the usage example with:\n```powershell\npoetry run docrunner <language> --markdown-path example/example.md\n```\n\n\n## Supported Languages\n\n- Python\n- Javascript\n- Typescript\n",
    'author': 'DudeBro249',
    'author_email': 'appdevdeploy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DudeBro249/docrunner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
