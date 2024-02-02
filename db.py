# from termcolor import colored
# print(colored('hello', 'red',attrs=[""]), colored('world', 'green'))



#  # collection_name = dbname["user_1_items"]
#     # item_1 = {
#     # "_id" : "U1IT00004",
#     # "item_name" : "Blender",
#     # "max_discount" : "10%",
#     # "batch_number" : "RR450020FRG",
#     # "price" : 340,
#     # "category" : "kitchen appliance"
#     # }

#     # item_2 = {
#     # "_id" : "U1IT00003",
#     # "item_name" : "Egg",
#     # "category" : "food",
#     # "quantity" : 12,
#     # "price" : 36,
#     # "item_description" : "brown country eggs"
#     # }
#     # collection_name.insert_many([item_1,item_2])
    
    
#     # Retrieve a collection named "user_1_items" from database
#     collection_name = dbname["user_1_items"]
    
#     item_details = collection_name.find({"category" : "food"})
#     for item in item_details:
#         print(item)