# Recreating the variables
import os

tests = "test value" 
variables = "another test value"
s = "single letter variable"
check = "this variable does not end with s"

# Redefining the function
def replace_s_variables():
    variables_dict = globals()
    for var_name in list(variables_dict.keys()):
        if var_name.endswith('s') and var_name != 's':
            new_var_name = var_name[:-1]
            variables_dict[new_var_name] = variables_dict[var_name]
            variables_dict[var_name] = None


print(f'ГЛОБАЛОЧКИ:  {globals()}')