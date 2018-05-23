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
        self.subject_data = self.subject_data[['subjectId' , 'subjectName' , 'subjectType' , 'credits' , 'duration']]
        self.test_data = self.test_data[['batchID' , 'subjectID' , 'facultyID1' , 'facultyID2']]
        
        
#         type : pd.DataFrame
        self.normal_rooms = self.room_data[(self.room_data.roomType==0) & (self.room_data.roomNo)]
        self.lab_rooms = self.room_data[(self.room_data.roomType==1) & (self.room_data.roomNo)]
        

        
#       type = np.array
        self.lab_subjects = self.subject_data[self.subject_data.subjectType==1].subjectId.values
        self.normal_subjects = self.subject_data[self.subject_data.subjectType==0].dropna().subjectId.values
        self.all_lab_batches = self.test_data[self.test_data.subjectID.apply(lambda x : x in self.lab_subjects)].batchID.unique()
        
#         type:np.array
        self.sectionslist = self.test_data[self.test_data.subjectID.apply(lambda sid : True if sid in self.normal_subjects else False)].batchID.unique()
    
    
#     type: dict , map : string -> np.array
        self.section_to_subjects = {}
        self.section_to_batches= {}
#         type dict , map : string -> set()
        self.section_to_labsubjects = {}
        self.subject_to_faculties = {}
        self.lab_subject_to_faculty_tuple = {}
        self.normal_subject_to_faculty = {}
        
                
        
#         method calls
        self.populate_subject_to_faculties() ; 
        self.populate_section_to_subject() ;
        self.populate_section_to_batches() ; 
        self.populate_section_to_labsubjects() ;
        #lab_subject to (facultyid1 , facultyid2) tuple 
        self.populate_lab_subject_to_faculty_tuple() ; 
        self.populate_normal_subject_to_faculty() ; 
        self.create_faculty_objects() ; 
        
        self.init_faculties() ;
        
    def populate_subject_to_faculties(self):
        subs = self.test_data.subjectID.unique()
        for sub in subs:
            self.subject_to_faculties[sub] =  self.test_data[self.test_data.subjectID==sub].facultyID1.unique()
            
    def populate_lab_subject_to_faculty_tuple(self):
        subs = self.lab_subjects
        for sub in subs:
            tempdf = self.test_data[self.test_data.subjectID==sub]
            self.lab_subject_to_faculty_tuple[sub] = (tempdf.facultyID1  , tempdf.facultyID2)

    def populate_normal_subject_to_faculty(self):
        subs = self.normal_subjects
        for sub in subs:
            self.normal_subject_to_faculty[sub] = self.test_data[self.test_data.subjectID==sub].facultyID1.unique()
        
        
    def populate_section_to_labsubjects(self):
        for section in self.sectionslist:
            batches = self.section_to_batches.get(section)
            labs = set() 
            for batch in batches:
                labs = labs.union(set(self.test_data[self.test_data.batchID==batch].subjectID.values))
 
            self.section_to_labsubjects.update({section : labs})
        
    
    def populate_section_to_batches(self):
        for section in self.sectionslist:
            batches = copy.deepcopy([]) ; 
            for batch in self.all_lab_batches:
                if(re.match(section+'\d+$' , batch)):
                    batches.append(batch) ; 
            self.section_to_batches.update({section: batches }) ;
        
        
        
#         returns facultyid if he is free else None
    def get_free_faculty_and_allot(self , facultylist , day , hour ):
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
            
    
    def display_time_table(self , section , facultyid=False , facultyname = True):
        asec = self.non_lab_allotment[self.non_lab_allotment.section=='6A']
        asec = asec.drop(['section' , 'roomno'], axis=1) 
        asec = asec.set_index(['day' , 'hour'])
        asec['subjectname'] = asec.subjectid.apply(lambda x :self.subject_data[self.subject_data.subjectId==x].values[0][1])
        asec = asec[['subjectname' , 'facultyid']].apply(lambda x : x.subjectname + ' >> ' +  str(x.facultyid)  , axis=1).unstack()
        print(asec) ; 
        return asec
        
        
        
    
#     populates the section_to_subjects dict  , maps section string to subjects list
    def populate_section_to_subject(self):
        for section in self.sectionslist:
            self.section_to_subjects[section] = self.test_data[self.test_data.batchID==section].subjectID ;
            
    
        
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
        
                    
#     return type : None
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
                        
                    
                    selected_faculty = self.get_free_faculty_and_allot(self.test_data[self.test_data['subjectID']==selected_subject].facultyID1 , day= day , hour = hour) 
                    
                    allotment = allotment.append({'section' : section , 'day' : day , 'hour' : hour  , 'subjectid' : selected_subject , 'roomno' : selected_room , 'facultyid' : selected_faculty } , ignore_index=True)
                    
        self.non_lab_allotment = allotment ;
        
        
    
    def allot_slots_lab_class(self):
        
#         returns true if all batch to labsubs are empty meaning all batches are alloted with all labsubs
        def check_if_all_batch_to_labsubs_empty(batch_to_lablist):
            for labset in batch_to_lablist.values():
                if(labset):
                    return False
            return True ;
        
        
        non_lab_allotment_sec_day_hour_index = self.non_lab_allotment.set_index(['section' , 'day' , 'hour'])
        lab_allotment_only = pd.DataFrame(columns=['section' , 'batch', 'day' , 'hour'  , 'subjectid' ])
        
        for section in self.sectionslist:
            batchlist = self.section_to_batches.get(section) 
            labsubs = self.section_to_labsubjects.get(section)
            
            batch_to_lablist = {}
            
            selected_days_for_lab = set(random.sample(['mon' , 'tue' ,'wed' , 'thu' , 'fri'] , len(labsubs)))
            
            
            for batch in batchlist:
                batch_to_lablist.update({batch : copy.deepcopy(labsubs)})

                
#             while(selected_days_for_lab):
                
            while(check_if_all_batch_to_labsubs_empty(batch_to_lablist)):
                selected_day = random.choice(selected_days_for_lab);

                selected_days_for_lab.remove(selected_day) ; 

                # assuming duration of each lab is 3 hours                     
                selected_hour = random.choice([1 , 2 , 5 , 6])

                # map : batch string to its assigned subject for that day
                batch_to_assigned_lab_subject = {} # for that day

                #type : set 
                #reset this before starting iterating over batches
                labsubs_left_to_be_assigned = labsubs
                
                #map from batch to selected_lab for the current "day"
                batch_to_selected_lab = {}
                

                for batch in batchlist:
                    intersection = labsubs_left_to_be_assigned.intersection(batch_to_lablist.get(batch))
                    selected_lab = random.choice(list(intersection))
                    batch_to_selected_lab.update({batch : selected_lab})
                    
                    labsubs_left_to_be_assigned.remove(selected_lab)
                    batch_to_lablist.get(batch).remove(selected_lab)
                    
#               # unallot faculty slots for the lab timiming from selected_hour
                # assuming 3 hours duration for each lab
                for hour in range(selected_hour , selected_hour+3):
                    self.unallot_faculty_slot(day = selected_day , hour = hour , faculty_id  = non_lab_allotment_sec_day_hour_index.loc[(section , selected_day , hour)].facultyid)
                
                for batch in batchlist:
                    lab_allotment_only.append({'section' : section , 'batch' : batch , 'day' : selected_day , 'hour' : range(selected_hour , selected_hour+3 ) , 'subjectid' : batch_to_selected_lab.get(batch)}) ; 
                
            return lab_allotment_only ;
                    
                        
    def unallot_faculty_slot(self , day , hour , facultyid ):
        self.faculty_to_day_hour_slot_map[facultyid][day][hour] = copy.deepcopy({alloted : False }) 
    
    
    def create_faculty_objects(self):
        '''Create facultie objects using the data ''' 
        self.faculties = set() ;
        for i in range(self.faculty_data.count().facultyId):
            self.faculties.add(faculty(self.faculty_data.loc[i].facultyId , self.faculty_data.loc[i].facultyName , self.faculty_data.loc[i].facultyType))
                
        
                    
    
    def check_allotment_validity(self , allotment_dataframe = None ):
        '''checks if the allotment DataFrame satisfies the hard constraints '''
        if(not allotment_dataframe):
            allotment_dataframe = self.non_lab_allotment ; 
        
        df = allotment_dataframe ;
        print("Starting faculty duplicate check for each hour of some day ") ; 
        
        for day in ['mon' , 'tue' , 'wed' , 'thu' , 'fri' , 'sat']:
            for hour in range(1 , 9):
                temp = df[(df.hour==1) & (df.day==day)]
                temp = temp[temp.facultyid.apply(lambda x : True if x else False )].facultyid
                if(not (temp.nunique()==temp.count())):
                    print("Fails faculty non duplicate test : day , hour = " , day , hour) ; 
                    print("temp = " , temp) ;
                    print("returning .. ") ; 
                    return  False ;
        
        print("\nSUCCESS ^_^ ") ; 
            

obj = Timetable()


if(__name__=='__main__'):
    obj.allot_slots_normal_class() ; 
    print(obj.allot_slots_lab_class()) ;
    print(obj.non_lab_allotment)