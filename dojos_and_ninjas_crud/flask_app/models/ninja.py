from flask_app.config.mysqlconnection import connectToMySQL

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
    
    
# crud method: create
    @classmethod 
    def save_ninjas(cls, data):
        query = """ 
            INSERT INTO ninjas
            (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)



# crud method: read
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
    