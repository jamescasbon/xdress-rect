#pragma once

namespace shapes {


    // Example 1.  As per unit tests, works fine...
    // typedef struct AreaHandlerStruct { double (*op)(int); } AreaHandlerStruct;

    // Example 2.  Doesn't like void in callback function, see stacktrace2.txt
    // This fails at generation of the wrapper class, before even the callback
    typedef struct VoidAreaHandlerStruct { void (*op)(int); } VoidAreaHandlerStruct;

    // Example 3.  How can I expose a typedef??
    // Fails to generate the callback, see stacktrace2.txt
    // typedef void (*area_handler)(void* context, int data);

    // Example 4, see stacktrace4.txt
    // no typedefs

    class Rectangle {
    public:
        int x0, y0, x1, y1;
        Rectangle();
        Rectangle(int x0, int y0, int x1, int y1);
        // ~Rectangle();
        int getLength();
        int getHeight();
        int getArea();
        void move(int dx, int dy);

        // Example 1. 
        // double do_with_area(AreaHandlerStruct x);

        // Example 2.
        void do_with_area(VoidAreaHandlerStruct x);

        // Example 3
        // void do_with_area(area_handler, void*);
        
        // Example 4, like as 3 but without typedef
        // void do_with_area(void (*op)(int));

    };
}
