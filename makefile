all:
	snakemake -j -s foo.snake
clean:
	git clean -xdf .
