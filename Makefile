.PHONY: setup

setup:
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
