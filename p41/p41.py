def check_pand(x):
  if "".join(sorted(list(str(x)))) == "123456789"[:len(str(x))]:
    return True
  return False


print check_pand(12346)


