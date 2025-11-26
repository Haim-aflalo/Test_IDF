import csv
class Soldier:
    def __init__(self, soldier_num: str, first_name: str, last_name: str, gender: str,residence_city:str, distance: int,status:bool = False):
        self.soldier_num = soldier_num
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.residence_city = residence_city
        self.distance = distance
        self.status = status


