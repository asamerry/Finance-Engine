all: fe-env

fe-env:
	@python3 -m venv .fe-env/
	@.fe-env/bin/pip3 install -r requirements.txt

clean:
	@rm -rf .fe-env/ *data/ *exports/