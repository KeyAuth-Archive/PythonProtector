cd ..

black -v .

autopep8 --in-place --aggressive --aggressive --recursive -v .


autoflake --in-place --remove-unused-variables .
