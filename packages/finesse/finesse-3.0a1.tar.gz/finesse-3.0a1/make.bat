@ECHO OFF

python setup.py build_ext --inplace --compiler=mingw32 --build-lib .

PAUSE
