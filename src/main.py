# NOTE :- THIS IS JUST A TESTING SOURCE FILE . ALL THE PROGRAM CODE IS IN THE "main.ipnb" FILE 

import pandas as pd ; 
import numpy as np 
import time , os , sys , random
import sqlite3


def convert_db_data_to_csv(table_name , connection  , path = './data/' , filename="mydata.csv" ):
    df = pd.DataFrame(pd.read_sql('select * from '+table_name , connection)) ; 
    df.to_csv(os.path.join(path , filename)) ; 



class Allotment:
    def __init__(self , subjectid ,  facultyid1 , facultyid2 , roomid , dayno , hour , subjectname='' ):
        self.subjectid =subjectid ; 
        self.subjectname = subjectname
        self.facultyid1 = facultyid1
        self.facultyid2 = facultyid2
        self.roomid = roomid
        self.dayno = dayno
        self.hour = hour
        

class Faculty:
    def __init__(self , fid , fname , ftype):
        self.id , self.name , self.type = fid , fname , ftype ; 
    def __str__(self):
        return "< ID : {} , Name : {}  , type : {}  >".format(self.id , self.name , self.type) ;
    def __repr__(self):
        return self.__str__() ;
        
        


class Timetable:
    def __init__(self):
        self.faculty_data = pd.read_csv("data/faculty.csv") ; 
        self.room_data = pd.read_csv('data/room.csv') ; 
        self.subject_data = pd.read_csv('data/subject.csv') ;
        self.test_data = pd.read_csv('data/test.csv') ;
        
        faculty_data = self.faculty_data[['facultyId' , 'facultyName' , 'facultyType']]
        room_data = self.room_data[['roomId' , 'roomType' , 'roomNo']]
        subject_data = self.subject_data[['subjectId' , 'subjectName' , 'subjectType' , 'credits']]
        test_data = self.test_data[['batchID' , 'subjectID' , 'facultyID1' , 'facultyID2']]

        
        self.allotments = []
        self.faculty_to_day_hour_slot_map = {}
        self.faculties = set 

        obj = print(Faculty) ; 
        print(obj) ; 
        
        for i in range(faculty_data.count().facultyId):
            self.faculties.add(faculty(self.faculty_data.loc[i].facultyId , self.faculty_data.loc[i].facultyName , self.faculty_data.loc[i].facultyType))
        
        
        for day in ['mon', 'tue' , 'wed' , 'thu' , 'fri' , 'sat']:
            for hour in range(8):
                for faculty in self.faculties:
                    self.faculty_to_day_hour_slot_map[faculty][day][hour] = {alloted : False} ;
                    
    
    def allot_slots(self):
        pass;
                    
    
    def check_allotment_validity(self , allotment ):
        for allots in self.allotments:
            pass ; 
            


Timetable()