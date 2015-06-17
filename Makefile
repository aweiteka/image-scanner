SHELL = /bin/sh


DESTDIR="/"

install:
	python setup.py build
	python setup.py install --root=$(DESTDIR)
	mkdir -p $(DESTDIR)/etc/image-scanner
	cp conf/image-scanner.conf $(DESTDIR)/etc/image-scanner
