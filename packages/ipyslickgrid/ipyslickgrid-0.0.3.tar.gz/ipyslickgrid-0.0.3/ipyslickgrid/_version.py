# Modifications copyright (C) 2021 8080 Labs GmbH

# - set version_info = (0, 0, 1, "final")

# "0.0.3"
version_info = (0, 0, 3, "final")

_specifier_ = {"alpha": "a1", "beta": "b", "candidate": "rc", "final": ""}

__version__ = "%s.%s.%s%s" % (
    version_info[0],
    version_info[1],
    version_info[2],
    _specifier_[version_info[3]],
)
__version__ = "0.0.3"