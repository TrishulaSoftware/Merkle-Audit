from setuptools import setup
from Cython.Build import cythonize

setup(
    name="MerkleAudit",
    ext_modules=cythonize("behavior_audit.py", compiler_directives={'language_level': "3"}),
    zip_safe=False,
)