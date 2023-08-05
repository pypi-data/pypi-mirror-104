default:
	python3 setup.py build_ext -j 4 --inplace

debug:
	python3 setup.py --debug build_ext -j 4 --inplace

# Build Cython extensions with the CYTHON_TRACE flag enabled to allow coverage tracking.
coverage:
	python3 setup.py --coverage build_ext -j 4 --force --inplace

clean:
	find . -name "*.so" -type f -delete
	find . -name "*.dll" -type f -delete

realclean: clean
	git clean -fX

lint:
	pylint --rcfile=.pylintrc ./finesse/
