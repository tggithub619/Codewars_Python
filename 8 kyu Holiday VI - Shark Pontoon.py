#https://www.codewars.com/kata/57e921d8b36340f1fd000059/train/python

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    shT =  shark_distance/shark_speed
    myT = pontoon_distance/you_speed
    shTd = 2*shark_distance/shark_speed
    return 'Alive!' if (dolphin and myT<shTd or myT<shT ) else 'Shark Bait!'