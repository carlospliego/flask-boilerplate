When a package (A) in the system imports another package (B) in the system. Package (B)
must be in the commmon directory.

The goal is to eliminate cross dependencies. And keep packages that other packages depend on in one place.
Think if other packages use this software, it belongs in this directory.

Do this
[package_a] -> [common.package_b]

Do not do this

[package_a] -> [package_b]