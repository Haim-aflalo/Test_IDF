import codecs
from fastapi import FastAPI, UploadFile, File
from classes import  creation_cls


app = FastAPI()




@app.post("/assignWithCsv")
def create_soldier_info(file: UploadFile = File(...)):
    return creation_cls.Create.create_soldiers(file)



@app.post("/assignBedToSoldier/")
def assign_bed(dorm_number, file: UploadFile = File(...)):
    return  creation_cls.Create.assign_bed(dorm_number,file)

@app.post("/soldiersInDorms")
def soldier_in_dorms(dorm_number, file: UploadFile = File(...)):
    assigned = assign_bed(dorm_number,file)
    count = 0
    for i in assigned:
        if i.soldier_num != False:
            count += 1
    return count


@app.post("/soldiersWithoutBed")
def soldiers_without_bed(dorm_number,file: UploadFile = File(...)):
    soldiers = creation_cls.Create.create_soldiers(file)
    beds = creation_cls.Create.assign_bed(dorm_number,file)
    return len(beds) - len(soldiers)


@app.post("/soldiersInfos")
def soldiers_info(dorm_number,file: UploadFile = File(...)):
    result = []
    row = file.read()
    soldiers = create_soldier_info(file)
    beds = assign_bed(dorm_number,file)
    for i in beds:
        for j in soldiers:
            if j.status:
                result.append({"soldier":i.soldier_num,"in dorms?": j.status,"room":i.room_id,"dorm":i.dorm_id})
            else:
                result.append({"soldier": i.soldier_num, "in dorms?": j.status})

    return result

