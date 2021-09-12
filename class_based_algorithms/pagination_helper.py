class PaginationHelper:
    
    def __init__(self, collection, items_per_page): 
        
        self.collection = collection
        self.items_per_page = items_per_page
        
    def item_count(self):
        return len(self.collection)

    def page_count(self):
        item_length = len(self.collection)
        page_number, page_remainder = divmod(item_length, self.items_per_page)      
        if page_remainder != 0:
            page_count = page_number + 1 
        else:
            page_count = page_number  
            
        return page_count

    def page_seperator(self):
        page_container_arr =[ self.collection[i:i+self.items_per_page] for i in range(0,len(self.collection),self.items_per_page)]
        checker = [page_container_arr.index(arr) for arr in page_container_arr]
        return page_container_arr, checker

    def page_item_count(self,page_index):
        
        page_container_arr, checker = self.page_seperator()

        if page_index not in checker:
            return -1
        else:
            return len(page_container_arr[page_index])
        
            
    
    def page_index(self,item_index):

        list_index = [ self.collection.index(self.collection[i]) for i in range(len(self.collection))]

        if item_index in list_index:
            element = self.collection[item_index] 
            page_container_arr,_ = self.page_seperator()
            page_index = [page_container_arr.index(page_container_arr[i]) for i in range(len(page_container_arr)) if element in page_container_arr[i]]
            return page_index[0]

        else:
            return -1

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.page_count()) # should == 2
print(helper.item_count()) # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid