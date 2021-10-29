import setuptools

setuptools.setup(
    name="hashtool",
    version="0.0.2",
    author="Zhang",
    author_email="",
    description="hash file or text with different method",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "hash=hashtool:main",
        ]
    },
)
