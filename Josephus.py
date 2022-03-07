import sys

class Link(object):
    def __init__ (self, data, next = None, before = None):
        self.data = data
        self.next = next
        self.before = before

    def __str__(self):
        return str(self.before) + " --> " + str(self.data) + " --> " + str(self.next)


class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.first = None

  # Insert an element (value) in the list
  def insert ( self, data ):
      newLink = Link(data)
      if(self.first is None):
          self.first = newLink
      else:
          current = self.first
          while(current.next is not None):
              current = current.next
          current.next = newLink
          before = current
          current = current.next
          current.before = before

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
      current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if.
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):
      pass

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
      pass

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):
      return str(self.first)

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code
  CirularList = CircularList()

if __name__ == "__main__":
  main()
