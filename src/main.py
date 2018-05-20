import pandas as pd ; 
import numpy as np 
import time , os , sys , random 
import sqlite3 , re , copy



def convert_db_data_to_csv(table_name , connection  , path = './data/' , filename="mydata.csv" ):
    df = pd.DataFrame(pd.read_sql('select * from '+table_name , connection)) ; 
    df.to_csv(os.path.join(path , filename)) ;


class allotment:
    def __init__(self , subjectid ,  facultyid1 , facultyid2 , roomid , dayno , hour , subjectname='' ):
        self.subjectid =subjectid ; 
        self.subjectname = subjectname
        self.facultyid1 = facultyid1
        self.facultyid2 = facultyid2
        self.roomid = roomid
        self.dayno = dayno
        self.hour = hour
        

class faculty:
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
        
        self.faculty_data = self.faculty_data[['facultyId' , 'facultyName' , 'facultyType']]
        self.room_data = self.room_data[['roomId' , 'roomType' , 'roomNo']]
        self.subject_data = self.subject_data[['subjectId' , 'subjectName' , 'subjectType' , 'credits']]
        self.test_data = self.test_data[['batchID' , 'subjectID' , 'facultyID1' , 'facultyID2']]
        
        self.sectionslist = self.get_sections_from_batches() ;  
        self.normal_rooms = self.room_data[(self.room_data.roomType==0) & (self.room_data.roomNo)]
        self.lab_rooms = self.room_data[(self.room_data.roomType==1) & (self.room_data.roomNo)]
    
        self.section_to_subjects = {}
        self.populate_section_to_subject() ; 
        
        self.create_faculty_objects() ; 
        self.init_faculties() ;
        
        
        
    def get_free_faculty(self , facultylist , day , hour ):
        '''Returns a random faculty from a np.array list of faculties who is free at that day and hour '''
        
        faculties = facultylist.values
        
        try:
            for faculty in faculties:
                if(self.faculty_to_day_hour_slot_map.get(faculty).get(day).get(hour).get('alloted') == False):
                    self.faculty_to_day_hour_slot_map.get(faculty).get(day).get(hour)['alloted'] = True
                    return faculty ;
        
        except AttributeError as err:
            print(err , 'faculty = ' , faculty , ' ,  day , hour = ' , day , hour ) ;  
        except Exception as Exp:
            print(Exp) ; 
            
        
        
        
    
    
   
    def populate_section_to_subject(self):
        for section in self.sectionslist:
            self.section_to_subjects[section] = self.test_data[self.test_data.batchID==section].subjectID ;
            
    
        
    def get_sections_from_batches(self):
        '''Assume the string till last but one char as the section name and if there is only 1 char take that as section name'''
        def myfun(x , compiledre):
            if(len(x)==1):
                return x ;
            else:
                if(compiledre.match(x)):
                    return x;  
        
        compiledre = re.compile('^.*?[a-zA-Z]$') ;
        sections = self.test_data.batchID.apply(lambda x : myfun(x , compiledre)) ;
        sectionslist = sections[sections.apply(lambda x : True if x else False)].unique()
        return sectionslist ;
        

        
    def init_faculties(self):
        '''Initialize the faculties to be not allocated to all the hours of all days'''        
        self.faculty_to_day_hour_slot_map = {}
        day_to_hour = {}
        faculty_to_data = {} 

        hour_to_allotflag = {}
        for hour in range(1 , 9):
            hour_to_allotflag.update({hour : copy.deepcopy({'alloted': False})}) ;

        for day in ['mon' , 'tue' , 'wed' , 'thu' , 'fri' , 'sat']:
            day_to_hour.update({day : copy.deepcopy(hour_to_allotflag)}) ;

        for faculty_object in self.faculties:
            self.faculty_to_day_hour_slot_map.update({faculty_object.id : copy.deepcopy(day_to_hour)}) ;
    
    
    
            
                    
    
    def allot_slots_normal_class(self):
        
        allotment = pd.DataFrame(columns=['day' ,'section', 'hour', 'subjectid' , 'roomno' , 'facultyid']) ;
        
        for section in self.sectionslist:
            selected_room = self.normal_rooms.roomNo.sample().values[0] ;
            section_subjects_original = self.section_to_subjects[section].values ;
            
            for day in ['mon' , 'tue' , 'wed' , 'thu' , 'fri' , 'sat']:
                batch_subs = section_subjects_original ; 

                for hour in range(1 , 9):
                    if(not batch_subs.any()):
                        selected_subject = self.section_to_subjects[section].sample().values[0]
                    else:
                        selected_subject_index =  random.randrange(len(batch_subs));
                        selected_subject = batch_subs[selected_subject_index] ; 
                        batch_subs = np.delete(batch_subs , selected_subject_index) ;
                        
                    
                    selected_faculty = self.get_free_faculty(self.test_data[self.test_data['subjectID']==selected_subject].facultyID1 , day= day , hour = hour) 
#                     self.faculty_to_day_hour_slot_map.get(selected_faculty).get(hour).update({'day' : day , 'hour' : hour , 'section' : section , 'subject' : subject})

#                     selected_faculty = self.test_data[self.test_data['subjectID']==selected_subject].facultyID1.sample().values[0]
                        
                    allotment = allotment.append({'section' : section , 'day' : day , 'hour' : hour  , 'subjectid' : selected_subject , 'roomno' : selected_room , 'facultyid' : selected_faculty  } , ignore_index=True)
                    
        self.non_lab_allotment = allotment ; 
                    
    
    
    def create_faculty_objects(self):
        '''Create facultie objects using the data ''' 
        self.faculties = set() ;
        for i in range(self.faculty_data.count().facultyId):
            self.faculties.add(faculty(self.faculty_data.loc[i].facultyId , self.faculty_data.loc[i].facultyName , self.faculty_data.loc[i].facultyType))
                
        
                    
    
    def check_allotment_validity(self , allotment ):
        for allots in self.allotments:
            pass ; 
            

obj = Timetable()



if(__name__=='__main__'):
    obj.allot_slots_normal_class() ; 
    print(obj.non_lab_allotment)