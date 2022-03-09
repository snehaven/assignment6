import sys

class Link(object):
    def __init__ (self, data, next = None, before = None):
        self.data = data
        self.next = next
        self.before = before

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
    def __str__(self):
        lst = [self.data, self.next.data]
        #stringrep = str(self.data) + " --> " + str(self.next.data) + " --> "
        current = self.next
        while (current.next.data is not self.data):
            lst.append(current.next.data)
            #stringrep += str(current.next.data) + " --> "
            current = current.next
        return str(lst)


class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.first = None

  # Insert an element (value) in the list
  def insert ( self, data ):
      newLink = Link(data)
      if(self.first is None):
          self.first = newLink
          self.first.next = self.first
      else:
          current = self.first

          while(current.next is not self.first):
              current = current.next
          current.next = newLink
          before = current
          current = current.next
          current.before = before
          current.next = self.first

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    current = self.first
    if (current == None):
      return None

    if (data == self.first.data):
      return self.first

    # search and find the position of the given data, the get the link if.
    while (current.data != data):
      if (current.next == self.first.data):
        return None
      else:
        current = current.next

    return current

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there

  def delete ( self, data ):
    need_to_delete = self.find(data)
    if (need_to_delete is None):
        return None

    before = need_to_delete.before
    after = need_to_delete.next
    before.next = after
    after.before = before

    return need_to_delete


  def delete_after ( self, start, n ):
        current = start
        for i in range(n - 1):
            current = current.next

        self.delete(current.data)
        return current.data, current.next

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

  # Create a circular list
  circularList = CircularList()

  #Populate circular list
  for i in range (1, num_soldiers + 1 ):
      circularList.insert(i)

  #Delete every nth soldier
  start = circularList.find( start_count )

  while num_soldiers >= 1:
        eliminated, start = circularList.delete_after ( start, elim_num )
        num_soldiers -= 1
        print( eliminated)

if __name__ == "__main__":
  main()

