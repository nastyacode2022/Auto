from setuptools import setup, find_packages

setup(
      name='API_testing',
      version='1.0',
      description='Practice API testing',
      author='Anastasiia',
      author_email='tarsasov74@gmail.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
            "pytest==7.1.1",
            "pytest-html==3.1.1",
            "requests==2.27.1",
            "requests-oauthlib==1.3.1",
            "PyMySQL==1.0.2",
            "WooCommerce==3.0.0",
      ]
      )

