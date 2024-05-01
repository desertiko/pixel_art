import pixel_art.pixels as pixels
def colors():
  print(f"{pixels.BLACK}{pixels.Back.RESET} - 'black'")
  print(f"{pixels.RED}{pixels.Back.RESET} - 'red'")
  print(f"{pixels.GREEN}{pixels.Back.RESET} - 'green'")
  print(f"{pixels.YELLOW}{pixels.Back.RESET} - 'yellow'")
  print(f"{pixels.BLUE}{pixels.Back.RESET} - 'blue'")
  print(f"{pixels.MAGENTA}{pixels.Back.RESET} - 'magenta'")
  print(f"{pixels.CYAN}{pixels.Back.RESET} - 'cyan'")
  print(f"{pixels.WHITE}{pixels.Back.RESET} - 'white'")

def house():
  img = pixels.Image()
  img.add_row(0, 'cyan')
  img.add_row(1, 'cyan', 'yellow', 'cyan', 'red', 'cyan', 'cyan', 'cyan')
  img.add_row(2, 'cyan', 'cyan', 'red', 'red', 'red', 'cyan', 'cyan')
  img.add_row(3, 'cyan', 'red', 'red', 'red', 'red', 'red', 'cyan')
  img.add_row(4, 'cyan', 'white', 'white', 'white', 'white', 'white', 'cyan')
  img.add_row(5, 'cyan', 'white', 'white', 'black', 'white', 'white', 'cyan')
  img.add_row(6, 'green')
  img.display()
# test your code here
# test your code here
if __name__ == '__main__':
  house()