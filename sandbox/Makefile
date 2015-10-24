TARGET ?= ""

default: one two three
	(test -f summary/${TARGET} && cat summary/${TARGET}) || echo ok
setup:
	pip install -e ../misc
	pip install handofcats # or using argparse, click..
one:
	mkdir -p source
	python -m misc.cli.nums --items=10 --nums=10 --outfile=source/
two:
	mkdir -p normalized
	python -m misc.cli.abs --outfile=normalized/${TARGET} source/${TARGET}
three:
	mkdir -p summary
	python -m misc.cli.summary --outfile=summary/${TARGET} normalized/${TARGET}
clean:
	rm -rf source normalized summary

.PHONY: one two three clean default setup
