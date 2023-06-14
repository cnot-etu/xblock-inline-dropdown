"""Setup for inline-input xblock"""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='xblock-inline-dropdown',
    version='0.2',
    description='Inline Dropdown XBlock',
    packages=[
        'inline_dropdown',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'inline-dropdown = inline_dropdown:InlineDropdownXBlock',
        ]
    },
    package_data=package_data("inline_dropdown", ["static", "templates"]),
)
