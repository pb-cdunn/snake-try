# -j --dryrun --summary --detailed-summary --list --list-target-rules
# --latency-wait=20 --restart-times=2 --timestamp --rerun-incomplete --notemp --keep-shadow
#  --stats=stats.json # useful!
#  --runtime-provile=prof.out # not useful
# --rerun-incomplete --cleanup-metadata # only if absolutely needed
# --verbose --quiet --reason
EXTRA= --latency-wait=20 --restart-times=2 --notemp --keep-shadow
VERBOSE= --reason --printshellcmds --stats=stats.json # --verbose

all:
	snakemake -j -T ${VERBOSE} ${EXTRA} -s foo.snake
summary:
	snakemake --detailed-summary -s foo.snake
dry:
	snakemake --dryrun --verbose -rs foo.snake
clean:
	git clean -xdf .
