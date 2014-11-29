from setuptools import setup

setup(
    name="shellstats",
    version="0.1",
    description="Show the most used shell commands.",
    url="https://github.com/rahiel/shellstats",
    author="Rahiel Kasim",
    author_email="rahielkasim@gmail.com",
    license="MIT",
    py_modules=["shellstats"],
    install_requires=["click"],
    entry_points={
        "console_scripts": ["shellstats = shellstats:main"]
    },
    extras_require = {
        "Plotting": ["matplotlib"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: System :: Shells",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ]
)
