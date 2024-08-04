from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
command=command_lexer:CommandLexer
'''

setup(
    name="command-pygments",
    version="0.0.1",
    description="Pygments lexer.",
    author="Tin Lam",
    author_email="tinlam@gmail.com",
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=["Pygments>=2.18.0"],
    zip_safe=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
)
