from rectangle_code import Rectangle, InvalidRectangleSide

def run_rectangle_test():
    try:
        r = Rectangle(5, 10)
        print("Rectangle created:", r.length, r.width)
        
        r = Rectangle(-5, 10)
    except InvalidRectangleSide as e:
        print("Exception caught:", e.message)