deps:
	pip3 install -r requirements.txt
.PHONY: deps

test:
	python3 -m pytest .
.PHONY: test
