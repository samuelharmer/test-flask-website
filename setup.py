from setuptools import setup

test_deps = [
    # 'coverage',
    'pytest',
    'tox'
]

extras = {
    'test': test_deps,
}

setup(
    name='website',
    packages=['website'],
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=test_deps,
    extras_require=extras,
)
