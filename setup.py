import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()



__version__ = "0.1.0"

REPO_NAME = "Text-Summarizer-project"
AUTHOR = "Srikaran "
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "varaganisrikaran@gmail.com"


setuptools.setup(
    name = REPO_NAME,
    version = __version__,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    description = "A package to summarize text for NLP APP",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR}/{SRC_REPO}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR}/{SRC_REPO}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),


)
