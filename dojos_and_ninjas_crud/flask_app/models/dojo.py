from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# created a list so later we can add all the ninjas that are associated 
# with each dojo
        self.ninjas = []
        
# crud method: create
    @classmethod
    def save_dojos(cls, data):
        query = """ 
            INSERT INTO dojos
            (name)
            VALUES (%(name)s);
        """
        return connectToMySQL(cls.db).query_db(query,data)
    
    
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

#  get one dojo with ninjas
    @classmethod 
    def get_ninjas_with_dojo(cls, data):
        query = """ 
            SELECT * FROM dojos
            JOIN ninjas ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        
        # one_dojo = cls( results[0] )
        dojo =  cls( results[0] )
        
        for row in results:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id': row['dojo_id']
            }
            dojo.ninjas.append(ninja.Ninja( ninja_data ) )
            return dojo

# read: get one
    @classmethod 
    def show_one_dojo(cls, data):
        query = """ 
            SELECT * FROM dojos
            WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
