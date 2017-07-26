.PHONY: test
test:
	@tox

build:
	@charm build -rl DEBUG

push:
	@charm push `echo $(JUJU_REPOSITORY)`/builds/geminabox cs:~creativedrive/geminabox --resource geminabox=/home/ubuntu/geminabox.snap
