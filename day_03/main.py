data = [i for i in open('input').readlines()]
fabric_width=1000
fabric_height=1000
fabric = [[0 for x in range(fabric_width)] for y in range(fabric_height)]

def get_claim(line):
  id_claim, _, coord, dim = line.split()
  id_claim = id_claim[1:]
  x, y = map(int, coord[:-1].split(','))
  width, height = map(int, dim.split('x'))  
  return id_claim, x, y, width, height

if __name__ == "__main__":
  for line in data:
    _, x, y, width, height = get_claim(line)
    for column in range(width):
      for row in range(height):
          fabric[x+column][y+row] += 1
  
  print("Square Inches with two ore more claims: ", len([column for row in fabric for column in row if column > 1]))
  print("------------------------")
  
  for line in data:
    id_claim, x, y, width, height = get_claim(line)
    failed = False
    for column in range(width):
      for row in range(height):
          if fabric[x+column][y+row] != 1:
            failed = True
    if not failed:
      print("Claim without overlap: ", id_claim)
