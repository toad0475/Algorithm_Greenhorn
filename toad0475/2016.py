def solution(a, b):
    weekDays = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    numOfDysForEachMon = [31,29,31,30,31,30,31,31,30,31,30,31]
    return weekDays[(sum(numOfDysForEachMon[:a-1])+b)%7-1]

