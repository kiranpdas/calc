build: clean
	mkdir ./dist
	cp ./src/main.py ./dist
	cd ./src && zip -x main.py -r ../dist/app.zip .

test:
	python -m unittest tests/test_calc.py

.venv:
	if [ ! -e ".venv/bin/activate_this.py" ] ; then virtualenv --clear .venv ; fi

 clean:
	rm -rf dist