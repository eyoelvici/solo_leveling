#!/usr/bin/env python3

def outer_function():
    global response
    global other
    global name
    name=input('hello there,what do i call you?')
    response=f"okey {name},what can i help you with"
    other='the name is %s'%name
def inner_function():
    print(other)

outer_function()
inner_function()
