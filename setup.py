import setuptools

with open('README.md','r') as file:
	long_desc = file.read()

setuptools.setup(
	name = 'preprocess_Bala-Yarabikki',
	version= '0.0.1',
	author= 'Bala Yarabikki',
	author_email='balachowdary777@gmail.com',
	description='This is preprocessing package',
	long_description=long_desc,
	long_description_content_type ='text/markdown',
	packages=setuptools.find_packages(),
	classifiers=[
	'Programming Language :: Python :: 3',
	'Licence :: OSI Aproved :: MIT License',
	'Operating System :: OS Independent'],
	python_requires = '>=3.5')