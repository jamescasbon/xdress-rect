#include "rectangle.h"

using namespace shapes;

Rectangle::Rectangle() { }

Rectangle::Rectangle(int X0, int Y0, int X1, int Y1)
{
    x0 = X0;
    y0 = Y0;
    x1 = X1;
    y1 = Y1;
}

// Rectangle::~Rectangle()
// {
// }

int Rectangle::getLength()
{
    return (x1 - x0);
}

int Rectangle::getHeight()
{
    return (y1 - y0);
}

int Rectangle::getArea()
{
    return (x1 - x0) * (y1 - y0);
}

void Rectangle::move(int dx, int dy)
{
    x0 += dx;
    y0 += dy;
    x1 += dx;
    y1 += dy;
}

// // Example 1
// double Rectangle::do_with_area(AreaHandlerStruct x) 
// { 
//     return x.op(10);
// }
// 
// // Example 2
// void Rectangle::do_with_area(VoidAreaHandlerStruct x) 
// { 
//     x.op(10);
// }

// Example 3
// void Rectangle::do_with_area(area_handler callback, void* context) 
// { 
//     return callback(context, 10);
// }

// Example 4
// void Rectangle::do_with_area(void (*op)(int)) 
// {
//     *op(10);
// }
//

int normal_add(int t, int u) { return t + u; }



