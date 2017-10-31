# -j --dryrun --summary --detailed-summary --list --list-target-rules
# --latency-wait=20 --restart-times=2 --timestamp --rerun-incomplete --notemp --keep-shadow --stats=stats.json
#  --runtime-provile=prof.out # not very useful
# --verbose --quiet --reason
#
all:
	snakemake --reason --printshellcmds --stats=stats.json -s foo.snake
summary:
	snakemake --detailed-summary -s foo.snake
dry:
	snakemake --dryrun --verbose -rs foo.snake
clean:
	git clean -xdf .
