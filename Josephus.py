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
      current = self.first
    if current.next != None:
      if current.data == data:
        current.next.previous = None
        self.first = current.next
        current.next = None
        return current
      else:
        while current.next != None:
          if current.data == data:
            break
          else:
            current = current.next
        if current.next != None:   
          current.previous.next = current.next
          current.next.previous = current.previous
          current.previous = None
          current.next = None
        else:
          current.previous.next = None
          current.previous = None
        return current
    
    if current == None:
      return None

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
      current = start
    print( start.next )
    
    for j in range ( n ):
        if current.next != None:
            current = current.next
    if current.next != None:
        current.before.next = current.next
        current.next.before = current.before
        current.before = None
        current.next = None
        return current.data, current.next
    else:
        current.before.next = None
        current.before = None
        return current.data, None

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):
    strng =""
    current = self.first
    strng += str(current.data) + ' <-> '
    current = current.next
    while(current.next != self.first and current.next != None):
      strng += str(current.data) + ' <-> '
      current = current.next
    strng += str(current.data) + ' <-> '
    return strng

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
  circularList = CircularList()
  for i in range ( num_soldiers ):
        circularList.insert(i)
  start = circularList.find( start_count )

  while num_soldiers > 1:
        eliminated, start = circularList.delete_after ( start, elim_num )
        num_soldiers -= 1
        print( eliminated )

if __name__ == "__main__":
  main()
