pwd
source configs/env.sh; rm -rf makefile; envsubst < "configs/make_templates/makefile" > "makefile"