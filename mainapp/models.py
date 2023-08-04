from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)    #Foreignkey for many:1 relation, CASCADE for if List is deleted,the associated Item should be aswell
    text=models.CharField(max_length=300)
    complete=models.BooleanField()

# the default reverse name will be the name of the child class followed by '_set',in this case item_set
#he reverse name for the m2m field would be childa_set in the ChildA case and childb_set for the ChildB field.
#item_set for Item class in this case
    
    def __str__(self) -> str:
        return self.text


