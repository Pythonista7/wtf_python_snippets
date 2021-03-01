# Walrus Operator!
# Syntax -> NAME:= expr

def some_func():
        # Assume some expensive computation here
        # time.sleep(1000)
        return 5

# So instead of,
if some_func():
        print(some_func()) # Which is bad practice since computation is happening twice

# or
a = some_func()
if a:
    print(a)

# Now you can concisely write
if a := some_func():
        print(a)
