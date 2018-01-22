init:
	source configs/env.sh; rm -rf makefile; envsubst < "configs/makefile_template" > "makefile";