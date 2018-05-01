
import math
global_X = 27

def my_function(param1=123, param2="hi mom"):
    local_X = 654.321
    print("\n=== local namespace ===")
    for key,val in list(locals().items()):
        print("name:", key, "value:", val)

    for key, val in list(globals().items()):  # line 2
        print("name:", key, "value:", val)
    print('------------------------')  # line 3

    print("=======================")
    print("local_X:", local_X)
    print("global_X:", global_X)

my_function()
print("\n--- global namespace ---")   # line 1

# print('local_X: ',local_X)          # line 4
print('global_X:',global_X)
print('math.pi: ',math.pi)
# print('pi:',pi)                     # line 5