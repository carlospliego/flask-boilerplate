# creates a make file for installation based on the one found in configs/make_templates/makefile
source configs/env.sh; rm -rf makefile; envsubst < "configs/templates/make/makefile" > "makefile"