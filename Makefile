bootstrap:
	pip install -e .
	pip install "file://`pwd`#egg=shecodes-ciphers[tests]"

lint:
	flake8 shecodes_ciphers/

test:
	PYTHONPATH=`pwd` py.test $(ARGS) shecodes_ciphers/tests.py

.PHONY: bootstrap test lint