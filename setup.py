import setuptools

setuptools.setup(
    name="hashfile",
    version="0.0.1",
    author="Zhang",
    author_email="",
    description="hash file with different method",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "hash=hashfile:main",
        ]
    },
)
