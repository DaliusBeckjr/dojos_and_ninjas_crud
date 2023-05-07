from mysqlconnection import connectToMySQL

class Ninja:
    db = "dojos_and_ninjas_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod 
    def get_all_ninjas(cls):
        query = """ 
            SELECT * FROM ninjas;
        """
        results = connectToMySQL(cls.db).query_db(query)
        
        all_ninjas = []
        
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas
    