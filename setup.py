from setuptools import setup


setup(
    name="shellstats",
    version="0.1",
    py_modules=["shellstats"],
    install_requires=["click"],
    entry_points={
        "console_scripts": ["shellstats = shellstats:main"]
    },
    extras_require = {
        "Plotting": ["matplotlib"]
    }
)
