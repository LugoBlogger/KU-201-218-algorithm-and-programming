def print_rangoli(size):
  # your code goes here
  # print([chr(97 + i) for i in range(26)])
  for i in list(range(size)) + list(range(size-2, -1, -1)):
    print("-".join([chr(97 + size-1 - j) 
      for j in list(range(i+1)) + list(range(i-1, -1, -1))])
        .center(size + size-1 + size-1 + size-1, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)