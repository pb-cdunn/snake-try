# Mutually exclusive, somewhat:
# -j --dryrun --summary --detailed-summary --list --list-target-rules
# --rerun-incomplete --cleanup-metadata # only if absolutely needed
# --verbose --quiet --reason
# Others:
#  --keep-going
#  --stats=stats.json # useful!
#  --runtime-profile=prof.out # not useful
EXTRA= --latency-wait=20 --restart-times=2 --notemp --keep-shadow
#FAST=-j
VERBOSE= --debug --reason --printshellcmds --stats=stats.json # --verbose
S=snakemake
#S=/Users/cdunn2001/Library/Python/3.6/bin/snap

all: | work
	cd work; $S ${FAST} ${VERBOSE} -T -s ../foo.snake
summary:
	snakemake --detailed-summary -s foo.snake
dry:
	snakemake --dryrun --verbose -rs foo.snake
work:
	mkdir -p work
	ln -s ../data work/data
clean:
	rm -rf work/
distclean:
	git clean -xdf .
