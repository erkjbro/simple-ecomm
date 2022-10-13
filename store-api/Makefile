SHELL := /bin/bash
.PHONY: setup build test deploy

setup:
	if [ ! -d .venv/bin ] ; then python3 -m venv .venv ; fi
	source .venv/bin/activate \
	&& python3 -m pip install -q -U pip \
	&& python3 -m pip install -q -U setuptools wheel \
	&& python3 -m pip install -q -r dev.txt

lint:
	source .venv/bin/activate && pylint app shared_layer tests

test:
	source .venv/bin/activate \
	&& ENV=test pytest
