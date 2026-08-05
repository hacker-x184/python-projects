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
                        '{self.__name}','{self.__phone}','{self.__city}');""")
            print("Now you are the member of library")
        except Exception as e:
            print(e)
    def remove_member(self,member_id):
        try:
            db_query(f"""DELECT FROM member WHERE member_id  = {member_id};
                     """)
        except Exception as e:
            print(e)
    def update_member(self,member_id,name):
        try:
            temp = db_query(f"""SELECT member_id FROM member WHERE member_id = {member_id};""")
            if temp:
                db_query(f"""UPDATE member
                SET name = '{name}'
                WHERE member_id = {member_id};""")
            else:
                print("Your member_id not available in data :-)")
        except Exception as e:
            print(e)
    def display_member(self):
            try:
                member_data = db_query(f"""SELECT * FROM member;""")
                print(f"Here are the list of the members:-")
                for member in member_data:
                    print(member)                   

            except Exception as e:
                print(e)
    def search_member(self,member_id):
        try:
            temp = db_query(f"SELECT * FROM member WHERE member_id = {member_id};")
            if temp:
                print("member are avaiable in List\nHere is your data")
                print(temp)
            else:
                print("Your member_id not available in data :-)")
        except Exception as e:
            print(e)
"""add_member()

remove_member()

update_member()

display_members()

search_member()"""