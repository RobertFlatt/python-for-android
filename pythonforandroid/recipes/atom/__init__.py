from pythonforandroid.recipe import CppCompiledComponentsPythonRecipe


class AtomRecipe(CppCompiledComponentsPythonRecipe):
    site_packages_name = 'atom'
    version = '0.11.0'
    url = 'https://github.com/nucleic/atom/archive/refs/tags/{version}.zip'
    hostpython_prerequisites = ['cppy']
    depends = ['setuptools']


recipe = AtomRecipe()
