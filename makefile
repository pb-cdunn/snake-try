# Mutually exclusive, somewhat:
# -j --dryrun --summary --detailed-summary --list --list-target-rules
# --rerun-incomplete --cleanup-metadata # only if absolutely needed
# --verbose --quiet --reason
# Others:
#  --keep-going
#  --stats=stats.json # useful!
#  --runtime-profile=prof.out # not useful
EXTRA= --latency-wait=20 --restart-times=2 --notemp --keep-shadow
VERBOSE= --reason --printshellcmds --stats=stats.json # --verbose

all: | work
	cd work; snakemake -j -T ${VERBOSE} -s ../foo.snake
summary:
	snakemake --detailed-summary -s foo.snake
dry:
	snakemake --dryrun --verbose -rs foo.snake
work:
	mkdir -p $@
clean:
	rm -rf work/
distclean:
	git clean -xdf .
