class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    obj_str = str(self.string)
    return obj_str
  """
  Testing the string to return the string back.
  """

  def vowels(self):
    count = 0
    vowels = "aeiouAEIOU"
    for i in self.string:
      if i in vowels:
        count = count + 1
    if count >= 5:
      return "many"
    return str(count)
  """
  Counting the number of vowels in the string.
  """

  def bothEnds(self):
    for i in range(len(self.string)):
      if len(self.string) >= 2:
        return str(self.string[:2]) + str(self.string[-2:])
      else:
        return ''
    """
    Returning only the first and last two letters of each string.
    """

  def fixStart(self):
    first_char = self.string[0]
    for i in self.string:
      if i == first_char:
        self.replace(i,'*')
        print(str(self.string))
  """
  Replacing each first character in the string with a *.
  """

  def asciiSum(self):
    for i in self.string:
      x = list(self.string)
      print(sum(ord(x)))
  """
  Finding the unicode of each character then adding them up.
  """
      
  def cipher(self):
    for i in self.string:
      self.split(self)
      x = ord(self)
      y = ord(self + len(self))
      final_string = x.string + y.string
      print(chr(final_string))
  """
  Adding the string length to the unicode of each character to return a new string with different characters.
  """