import codecs
from string import ascii_uppercase
from classes import soldier_cls
from classes import bed_cls
import csv


class Create:


    @staticmethod
    def create_soldiers(file):
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            soldiers = []
            for row in reader:
                soldier = soldier_cls.Soldier(row["soldier_num"], row["first_name"], row["last_name"], row["gender"],
                                              row["residence_city"], row["distance"])
                soldiers.append(soldier)
            return soldiers

    @staticmethod
    def sort_distance(soldiers):
        distance_soldiers = []
        for soldier in soldiers:
            distance_soldiers.append(
                {"soldier_num": soldier.soldier_num, "distance": soldier.distance, "status": soldier.status})
        top_distance_soldiers = sorted(distance_soldiers, key=lambda d: int(d["distance"]))
        return top_distance_soldiers[::-1]

    @staticmethod
    def assign_bed(dorm_numbers, file):
        beds = int(dorm_numbers) * 10 * 8
        occupied_beds = []
        soldiers = Create.create_soldiers(file)
        furthest_soldiers = Create.sort_distance(soldiers)[:beds]
        for i in range(len(furthest_soldiers)):
            if furthest_soldiers[i]["soldier_num"].startswith("8"):
                if not furthest_soldiers[i]["status"]:
                    bed = bed_cls.Bed(i, soldier_num=furthest_soldiers[i]["soldier_num"])
                    if i < 11:
                        bed.room_id = 1
                    else:
                        bed.room_id = i // 10
                    if i < 81:
                        bed.dorm_id = ascii_uppercase[0]
                    else:

                        bed.dorm_id = ascii_uppercase[beds // 80]
                    furthest_soldiers[i]["status"] = True
                    occupied_beds.append(bed)
            else:
                return 'file error invalid soldier_num'
        return occupied_beds

