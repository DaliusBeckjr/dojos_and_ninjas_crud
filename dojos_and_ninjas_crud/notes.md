schema:

1.) create a new model erd
2.) Name the shema dojos_and_ninjas_schema

Dojos table:
3.) Create a table called dojos
4.) Add the following fields to the dojos table: id, name, created_at and updated_at

Ninjas table:
5.) Create a table called ninjas
6.) Add the following fields to the ninjas table: id, first_name, last_name, age, created_at, updated_at

7.) create an one to many relationship to the dojos table

8.) Change the name of the relationship field to the singular pronoun. ie dojo_id
9.) Save your ERD as a .mwb file and submit it to the platform

flask + mySQL:

1.) Create a new flask project
2.) Use dojos and ninjas schema created in the mySQL course
3.) Dojo` page to add a new Dojo and display all Dojos
4.) The dojo links on the `Dojo` page should redirect the `Dojo Show` page

5.) `Ninja` page to add a new Ninja
6.) `Ninja` page should include a drop down menu will all of the dojos in the database

7.) Redirect to the `Dojo Show` page of the dojo selected after creating a ninja

8.) `Dojo Show` page should display all the Ninjas who are added to the Dojo

9.) All Home links should redirect to `localhost:5000/dojos`