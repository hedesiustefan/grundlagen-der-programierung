def prim(number):
    if number ==1 :
        return False
    if number == 2:
        return True
def test_prim():
   assert prim(1) == False
   assert prim(2) == True
   assert prim(11) == True
   assert prim(9) == False


