import setuptools
import itertools

INSTALL_REQUIRES = [
        "datetime"
]

EXTRAS_REQUIRE = {
    "dev": [],
    "test": [
        "pytest",
        "black"
    ]
}

# populate dev from specified deps
EXTRAS_REQUIRE["dev"] = list(itertools.chain.from_iterable(EXTRAS_REQUIRE.values()))

setuptools.setup(
    name="datetime-model",
    version="0.1",
    description="Predict date components in a string",
    url="https://github.com/luminous-supergiant/datetime-model",
    author="luminous-supergiant",
    author_email="luminous.supergiant@gmail.com",
    license="Apache-2.0",
    include_package_metadata=True,
    include_package_data=True,
    package_dir={"datetime-model": "datetime-model"},
    package_data={
        "datetime-model": [
        ]
    },
    install_requires=INSTALL_REQUIRES,  # specifies dependencies of python packages in pip
    extras_require=EXTRAS_REQUIRE,
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)