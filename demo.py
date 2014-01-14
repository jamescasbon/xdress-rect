import rect.rectangle as r

# example as in the unit tests
callback_struct = r.AreaHandlerStruct()
callback_struct.op = lambda x: float(x) * 2

result = r.Rectangle().do_with_area(callback_struct)
assert result == 20.
print 'the first example works'
