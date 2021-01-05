#https://www.codewars.com/kata/57f604a21bd4fe771b00009c


def meeting(rooms):
    if 'O' in rooms:
        return rooms.index('O')
    else:
        return 'None available!'