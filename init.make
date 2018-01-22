init:
	source configs/env.sh; rm -rf makefile; envsubst < "configs/makefile" > "makefile";