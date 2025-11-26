from fastapi import FastAPI, UploadFile, File
from classes import creation_cls



app = FastAPI()




@app.post("/assignWithCsv")
def create_soldier_info(path):
    return creation_cls.Create.create_soldiers(path)


@app.post("/assignBedToSoldier/")
def assign_bed(dorm_number, path):
    return creation_cls.Create.assign_bed(dorm_number, path)


@app.post("/soldiersInDorms")
def soldier_in_dorms(dorm_number, path):
    assigned = assign_bed(dorm_number, path)
    count = 0
    for i in assigned:
        if i.soldier_num != False:
            count += 1
    return count


@app.post("/soldiersWithoutBed")
def soldiers_without_bed(dorm_number, path):
    soldiers = creation_cls.Create.create_soldiers(path)
    beds = creation_cls.Create.assign_bed(dorm_number, path)
    return len(beds) - len(soldiers)


@app.post("/soldiersInfos")
def soldiers_info(dorm_number, path):
    result = []
    soldiers = create_soldier_info(path)
    beds = assign_bed(dorm_number, path)
    for i in beds:
        for j in soldiers:
            if j.status:
                result.append({"soldier": i.soldier_num, "in dorms?": j.status, "room": i.room_id, "dorm": i.dorm_id})
            else:
                result.append({"soldier": i.soldier_num, "in dorms?": j.status})
    return result



@app.get("/infosById/{id}")
def info_by_id(id, path, dorm_number):
    result = []
    soldiers = create_soldier_info(path)
    beds = assign_bed(dorm_number, path)
    for i in beds:
        for j in soldiers:
            if j.soldier_num == id:
                if i.soldier_number == id:
                    result.append({"soldier": id, "room": i.room_id, "dorm": i.dorm_id})
    return result