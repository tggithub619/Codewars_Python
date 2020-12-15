#https://www.codewars.com/kata/57ae18c6e298a

def replace_all(obj, find, replace):
  if type(obj) == str:
      return obj.replace(find, replace)
  else:
      return [replace if x == find else x for x in obj]

  def replace_all(obj, find, replace):
      if type(obj) == str:
          return obj.replace(find, replace)
      else:
          for i in range(len(obj)):
              if obj[i] == find:
                  obj[i] = replace
          return obj