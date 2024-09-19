# 2.5lb, 5lb, 10lb, 25lb, 35lb, 45lb
# subtract bar weight (45lbs) from input lbs
# divide subtracted lbs by 2
# divide product by 45 (integer is number of 45lbs)
# multiply remainder by 45
# if product/35 < 1, product/25, if that's also < 1, /10 and so on until >= 1. Then repeat with smaller plates.

calc = 0
msg_45 = ""
msg_35 = ""
msg_25 = ""
msg_10 = ""
msg_5 = ""
msg_2_5 = ""


def plate_45(weight):
  global calc
  num_plates = 0
  global msg_45
  calc = (weight-45)/2
  if (calc/45) >= 1:
    num_plates = int(calc//45)
    calc = (calc % 45)
    if num_plates > 1:
      msg_45 = f"{num_plates} 45's\n"
    else:
      msg_45 = "1 45\n"
  else:
    num_plates = 0
  return num_plates
  return calc
  return msg_45

def plate_35(weight):
  global calc
  num_plates = 0
  global msg_35
  if (calc/35) >= 1:
    num_plates = int(calc//35)
    calc = (calc % 35)
    if num_plates > 1:
      msg_35 = f"{num_plates} 35's\n"
    else:
      msg_35 = "1 35\n"
  else:
    num_plates = 0
  return num_plates
  return calc
  return msg_35;

def plate_25(weight):
  global calc
  num_plates = 0
  global msg_25
  if (calc/25) >= 1:
    num_plates = int(calc//25)
    calc = (calc % 25)
    if num_plates > 1:
      msg_25 = f"{num_plates} 25's\n"
    else:
      msg_25 = "1 25\n"
  else:
    num_plates = 0
  return num_plates
  return calc
  return msg_25

def plate_10(weight):
  global calc
  num_plates = 0
  global msg_10
  if (calc/10) >= 1:
    num_plates = int(calc//10)
    calc = (calc % 10)
    if num_plates > 1:
      msg_10 = f"{num_plates} 10's\n"
    else:
      msg_10 = "1 10\n"
  else:
    num_plates = 0
  return num_plates
  return calc
  return msg_10

def plate_5(weight):
  global calc
  num_plates = 0
  global msg_5
  if (calc/5) >= 1:
    num_plates = int(calc//5)
    calc = (calc % 5)
    if num_plates > 1:
      msg_5 = f"{num_plates} 5's\n"
    else:
      msg_5 = "1 5\n"
  else:
    num_plates = 0
  return num_plates
  return calc
  return msg_5

def plate_2_5(weight):
  global calc
  num_plates = 0
  global msg_2_5
  if (calc/2.5) >= 1:
    num_plates = int(calc//2.5)
    calc = (calc % 2.5)
    if num_plates > 1:
      msg_2_5 = f"{num_plates} 2.5's"
    else:
      msg_2_5 = "1 2.5"
  else:
    num_plates = 0
  return num_plates
  return calc
  return msg_2_5

def plate_calc(weight):
  global calc
  w_45 = int(plate_45(weight))
  w_35 = int(plate_35(calc))
  w_25 = int(plate_25(calc))
  w_10 = int(plate_10(calc))
  w_5 = int(plate_5(calc))
  w_2_5 = int(plate_2_5(calc))
  print(f"On each side, put:\n{msg_45}{msg_35}{msg_25}{msg_10}{msg_5}{msg_2_5}")
  if calc > 0:
    print(f"Extra {int(calc*2)} lbs, figure it out :)")

weight = int(input("Put desired weight in lbs: "))
plate_calc(weight)