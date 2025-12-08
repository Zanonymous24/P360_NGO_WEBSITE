from setuptools import setup, find_packages

setup(
    name="prosperity360-website",
    version="1.0.0",
    description="Prosperity360 Foundation Website",
    author="Prosperity360 Team",
    author_email="info@prosperity360.org",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==3.0.0",
        "python-dotenv==1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest==7.4.3",
            "pytest-flask==1.2.0",
            "black==23.11.0",
            "flake8==6.1.0",
            "pre-commit==3.5.0",
            "safety==2.3.5",
            "bandit==1.7.5",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10",
)