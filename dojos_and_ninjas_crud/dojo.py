from mysqlconnection import connectToMySQL

class Dojo:
    db = "dojos_and_ninjas_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
# crud method: create
    @classmethod
    def save(cls, data):
        query = """ 
            INSERT INTO dojos 
            (name)
            VALUES(%(name)s);
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
# crud method: read
    @classmethod 
    def get_all_dojos(cls):
        query = """ 
            SELECT * FROM dojos;
        """
        
        results = connectToMySQL(cls.db).query_db(query)
        
        all_dojos = []
        
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos