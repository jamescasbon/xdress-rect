Conversion of the classic cython rectangle cpp demo to use xdress.

Additions

quickstart: 

    # TODO:  move this into the build
    export LD_LIBRARY_PATH=./rect
    g++ -fPIC -std=c++11 -c src/rectangle.cpp -o rect/librectangle.o 
    g++ -fPIC -std=c++11 -shared -o rect/librectangle.so rect/librectangle.o

    xdress --debug -p clang 
    python setup.py build_ext --inplace


Current status: callbacks not working


