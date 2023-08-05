# ==========================================================================
#
#   Copyright NumFOCUS
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0.txt
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==========================================================================*/

"""Insight Toolkit (itk) configuration module.

This module contains user options and paths to libraries and language support
files used internally.

User options can be set by importing itkConfig and changing the option values.

Currently-supported options are:
  DebugLevel: must be one of SILENT, WARN, or ERROR (these values are defined
    in itkConfig). Default is WARN.
  ImportCallback: importing itk libraries can take a while. ImportCallback will
    be called when each new library is imported in the import process.
    ImportCallback must be a function that takes two parameters: the name of
    the library being imported, and a float (between 0 and 1) reflecting the
    fraction of the import that is completed.
  LazyLoading: Only load an itk library when needed. Before the library is
    loaded, the namespace will be inhabited with dummy objects."""

from typing import Dict, List, Optional, Type, Union

# User options
SILENT: int = 0
WARN: int = 1
ERROR: int = 2
DebugLevel: int = WARN
ImportCallback = None
ProgressCallback = None


def _get_environment_boolean(environment_var: str, default_string: str) -> bool:
    # Use defaults if not available as environmental overrides
    # True values are y, yes, t, true, on and 1;
    # False values are n, no, f, false, off and 0.
    # Raises ValueError if val is anything else.
    from os import environ as _environ
    from distutils.util import strtobool as _strtobool

    try:
        _StringDefault: str = _environ.get(environment_var, default_string)
        return bool(_strtobool(_StringDefault))
    except ValueError:
        print(
            f"{environment_var} environment variable has invalid value {_StringDefault}"
        )
        print(
            "   Valid True values are (case insensitive): 'y', 'yes', 't', 'true', 'on', and '1'"
        )
        print(
            "   Valid False values are (case insensitive): 'n', 'no', 'f', 'false', 'off', and '0'"
        )
    return bool(_strtobool(default_string))


LazyLoading: bool = _get_environment_boolean("ITK_PYTHON_LAZYLOADING", "True")
NotInPlace: bool = _get_environment_boolean("ITK_PYTHON_NOTINPLACE", "False")
del _get_environment_boolean

# Internal settings


def _itk_format_warning(
    message: Union[Warning, str],
    category: Type[Warning],  # Ignore category
    filename: str,  # Ignore filename
    lineno: int,  # Ignore lineno
    line: Optional[str] = None,  # Ignore line
) -> str:
    """"Format the warnings issued by itk to display only the message.

    This will ignore the filename and the line number where the warning was
    triggered. The message is returned to the warnings module.

    Ignore the category, filename, lineno, and line elements of a standard warning message
    """
    return str(message) + "\n"


import warnings

# Redefine the format of the warnings
warnings.formatwarning = _itk_format_warning


def _initialize():
    import os

    _this_file_dir: str = os.path.dirname(__file__)

    def _normalized_path(relative_posix_path: str, message) -> str:
        norm_path: str = "None"
        if relative_posix_path != "None":
            relative_path = relative_posix_path.replace("/", os.sep)
            norm_path = os.path.normpath(os.path.join(_this_file_dir, relative_path))
            if not os.path.exists(norm_path):
                print(f"WARNING: Internal configuration path is invalid: {norm_path}")
                print(f"WARNING: Invalid: {message}")
        return norm_path

    _swig_lib: str = _normalized_path(
        "itk",
        "swig_lib: location of the swig-generated shared libraries",
    )
    _swig_py: str = _normalized_path(
        "itk",
        "swig_py: location of the xxxPython.py swig-generated python interfaces",
    )
    _config_py: str = _normalized_path(
        "itk/Configuration",
        "config_py: location of xxxConfig.py CMake-generated library descriptions",
    )

    _config_py_root: str = os.path.dirname(_config_py)

    # put the itkConfig.py path in the path list
    _path = _config_py_root

    # NOT IMPLEMENTED:
    # _doxygen_root = _normalized_path("../Doc", "doxygen_root: location of the doxygen xml files.")
    _doxygen_root: str = "None"

    return _swig_lib, _swig_py, _config_py, _doxygen_root, _path


ITK_GLOBAL_VERSION_STRING: str = "5.2.0"
ITK_GLOBAL_WRAPPING_BUILD_OPTIONS: Dict[str, List[str]] = {
    "ITK_WRAP_IMAGE_DIMS": "2;3;4".split(";"),
    "WRAP_ITK_USIGN_INT": "UC;US".split(";"),
    "WRAP_ITK_SIGN_INT": "SS".split(";"),
    "WRAP_ITK_REAL": "F;D".split(";"),
    "ITK_WRAP_PYTHON_VECTOR_REAL": "itk::Vector< float,2 >;itk::Vector< float,3 >;itk::Vector< float,4 >".split(";"),
    "ITK_WRAP_PYTHON_COV_VECTOR_REAL": "itk::CovariantVector< float,2 >;itk::CovariantVector< float,3 >;itk::CovariantVector< float,4 >".split(";"),
    "ITK_WRAP_PYTHON_RGB": "itk::RGBPixel< unsigned char >".split(";"),
    "ITK_WRAP_PYTHON_RGBA": "itk::RGBAPixel< unsigned char >".split(";"),
    "ITK_WRAP_PYTHON_COMPLEX_REAL": "std::complex< double >;std::complex< float >".split(";"),
}

(swig_lib, swig_py, config_py, doxygen_root, path) = _initialize()
del _initialize
del warnings
