from database import db_query
class Members:
    def __init__(self,name,phone,city):
        self.__name = name    
        self.__phone = phone    
        self.__city = city    

    def add_member(self):
        try:
            db_query(f"""
                    INSERT INTO member(name,phone,city) VALUES(
                        '{self.__name}','{self.__phone}','{self.__city}')""")
            print("Now you are the member of library")
        except Exception as e:
            print(e)
    def remove_member(self,member_id):
        try:
            db_query(f"""DELECT * FROM member WHERE member_id  = {member_id}
                     """)
        except Exception as e:
            print(e)

"""add_member()

remove_member()

update_member()

display_members()

search_member()"""