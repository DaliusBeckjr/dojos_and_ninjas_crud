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

dojos and ninjas part 2:

1.) Add a column to the ninjas table on the dojo details page that includes a delete and edit link for each ninja 

2.) Add delete functionality to your Ninja model to be able to delete a record in the ninjas table.

3.) Add a route in your server that will process deleting a ninja and redirect to that same dojo details page e.g. "dojos/1" 

4.) Create a template for editing a ninja
5.) Add edit functionality to your Dojo model to be able to update a record in the dojos table

6.) Add a route to your server that will render the edit page with that particular dojo's info. Be sure to include 1.) pre-populated fields in the form and 2.) a link that goes back to that ninja's respective dojo's details page. 

7.) Add an update POST route to process the user input from the edit form.

8.) Be sure to redirect to the dojo details page after processing the update.