from setuptools import setup


def readme():
    try:
        with open("README.md") as f:
            return f.read()
    except:
        return ""

setup(
    name="theark",
    version="v1.0.0",
    author="meltmedia QA Team",
    author_email="qa-d@meltmedia.com",
    description="meltQA Tools Common Library.",
    license="Apache Software License",
    keywords="selenium helpers qa automation",
    url="https://github.com/melt-media/the-ark",
    packages=['the_ark', 'the_ark.resources'],
    long_description=readme(),
        install_requires=[
        "boto3",
        "requests",
        "selenium"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
    ],
)
