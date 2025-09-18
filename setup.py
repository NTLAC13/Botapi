from setuptools import setup, find_packages

setup(
    name="myapiclient",
    version="1.0.0",
    description="کتابخونه ساده برای گرفتن بیو، جوک و دانستنی از codebazan.ir",
    author="YourName",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.6",
)
