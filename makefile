#--latency-wait=20 --restart-times=2 --timestamp -l --lt --summary --detailed-summary --verbose --quiet --rerun-incomplete --notemp --keep-shadow --stats=stats.json

all:
	snakemake -j -prs foo.snake
clean:
	git clean -xdf .
