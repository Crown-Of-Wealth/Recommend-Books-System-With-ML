from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

REPO_NAME = 'Recommend-Books-System-With-ML'
AUTHOR_USER_NAME = 'Crown-Of-Wealth'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(name=SRC_REPO,
      version='0.0.1',
      author=AUTHOR_USER_NAME,
      description='A small package for Recommending Books',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
      author_email='ogunlanaoluwabunmi@gmail.com',
      packages=[SRC_REPO],
      python_requires='>=3.10',
      install_requires=LIST_OF_REQUIREMENTS
)