import dog

my_dog = dog.Dog("CJ", "Puppy")
print(my_dog)
print(my_dog.name)

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)

""" Adding Properties """
# Adding the "breed" property on the fly
my_dog.breed = "SuperDog"
# will print "SuperDog"
print(my_dog.breed)

my_dog.bark()