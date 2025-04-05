deps:
	pip3 install -r requirements.txt
.PHONY: deps

test:
	python3 -m pytest -rP -vv .
.PHONY: test

test-mod:
	python3 -m pytest -rP -vv . $(MODULE)
.PHONY: test-mod
