def create_variables(num_vars):
  """Creates a list of variables with the given number of variables.

  Args:
    num_vars: The number of variables to create.

  Returns:
    A list of variables.
  """
  variables = []
  for i in range(num_vars):
    variable_name = f"variable_{i}"
    exec(f"{variable_name} = {i}")
    variables.append(variable_name)
  return variables


if __name__ == "__main__":
  num_vars = 10
  variables = create_variables(num_vars)
  print("The list of variables:")
  for variable in variables:
    print(type(variable))