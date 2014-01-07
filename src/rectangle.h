#pragma once

namespace shapes {
    typedef void (*area_handler)(void* context, int data);

    class Rectangle {
    public:
        int x0, y0, x1, y1;
        Rectangle(int x0, int y0, int x1, int y1);
        ~Rectangle();
        int getLength();
        int getHeight();
        int getArea();
        void move(int dx, int dy);
        void do_with_area(area_handler, void*);
    };
}
