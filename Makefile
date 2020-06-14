.venv:
	if [ ! -e ".venv/bin/activate_this.py" ] ; then virtualenv --clear .venv ; fi

test:
	python -m unittest tests/test_calc.py
 