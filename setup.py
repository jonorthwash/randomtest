from setuptools import setup, find_namespace_packages

setup(
	name="MyApp",
	author="I. M. Me",
	version="0.0.1",
	packages=find_namespace_packages(
		include=["MyApp.*"]
	),
	description="MWE test app",
	entry_points={
		"console_scripts": [
			"MyApp = MyApp.__main__:main"
		]
	},
	#command_options={
	#	'nuitka': {
	#		'--standalone': True,
	#	}
	#},
)
