from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(

    name='rengine',
    packages=['rengine'],
    version='0.1.5',
    description='Most used methods for recommendation engine',
    author='Rafi Mochamad Fahreza',
    author_email='prokodingproject@gmail.com',
    install_requires=['numpy'],
    keywords=['algorithm', 'recommendation', 'engine'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence ',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
