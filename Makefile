all: 
	export LD_LIBRARY_PATH=./rect
	export CPPFLAGS="-L./rect"
	g++ -fPIC -std=c++11 -c src/rectangle.cpp -o rect/librectangle.o 
	g++ -fPIC -std=c++11 -shared -o rect/librectangle.so rect/librectangle.o
	xdress
	python setup.py build_ext --inplace
