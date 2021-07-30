import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='bitbucket_approver',
     version='1.0',
     scripts=['bitbucket_approver'],
     author="Feng Chen",
     author_email="santo.chan123@gmail.com",
     description="This is the approver client for bitbucket approver",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/santochan/py_bitbucket_approver",
     packages=setuptools.find_packages(),
     install_requires=[
         "python-socketio>4.6.0,<5.0",
         "toml",
         "requests>2.25.0",
         "requests[socks]"
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
