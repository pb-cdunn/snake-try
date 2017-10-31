all:
	snakemake -j -prs foo.snake
clean:
	git clean -xdf .
