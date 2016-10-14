from setuptools import setup

setup(
    name='httpie-aws-auth',
    version='0.1.0',
    description='Simple HTTPie plugin to help with signed AWS requests.',
    long_description=(open('README.rst')
                      .read()
                      .strip()),
    author='Gabriel Majivu',
    author_email='gmajivu@gmail.com',
    licence='MIT',
    url='https://github.com/gabeno/httpie-aws-auth',
    download_url='https://github.com/gabeno/httpie-aws-auth',
    py_modules=['httpie_aws_auth'],
    install_requires=[
        'requests-aws4auth>=0.9',
        'httpie>=0.9.0'
    ],
    entry_point={
        'httpie.plugins.auth.v1': ['httpie_aws_auth = httpie_aws_auth:AWSAuthPlugin']
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
    ]
)
