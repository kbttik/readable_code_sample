# var remove_one = function (array, value_to_remove) {
# var index_to_remove = null;
# for ( var i=0; i < array.length; i += 1) {
#   if(array[i] === value_to_remove) {
#     index_to_remove = i;
#     break;
#   }
# }
# if (index_to_remove !== null) {
#   array.splice(index_to_remove, 1);
# }
# };

#2021/03/13 Readable_code

def remove_one(array, value_to_remove):
    index_to_remove = None
    target = array[:]
    for idx, value in enumerate(target):
        if value == value_to_remove:
            index_to_remove = idx
            break
    
    if index_to_remove != None:
        target.pop(index_to_remove)
    
    return target

num_list = [1,2,3,4,5,6,7,8,9,10]  
str_list = ["I", "J", "M", "S"]
str_list_2 = ["I", "J", "M", "S", "M"]

# test1
new_num_list = remove_one(num_list, 5)
print(new_num_list)

# test2
print(remove_one(num_list, 11))

# test3
print(remove_one(str_list, "M"))

# test4
print(remove_one(str_list_2, "M"))