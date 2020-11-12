#https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(h):
    c = 15 if h==1 else 15+9 if h ==2 else ((h-2)*4)+15+9
    d = 15 if h==1 else 15+9 if h ==2 else ((h-2)*5)+15+9
    return [h,c,d]