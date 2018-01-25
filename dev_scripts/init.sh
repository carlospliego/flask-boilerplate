#!/usr/bin/env bash


# development entry point




# creates a make file for installation based on the one found in configs/make_templates/makefile
source configs/bin/env.sh; rm -rf makefile; envsubst < "configs/file_templates/make/makefile" > "makefile"