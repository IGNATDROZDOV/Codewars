from math import ceil

class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return ceil(self.item_count() / self.items_per_page)

    def page_index(self, ind):
        if ind < self.item_count() and ind > -1:
            return int (ind / self.items_per_page)
        return -1

    def page_item_count(self, p_ind):
        if p_ind >= self.page_count() or p_ind < 0:
            return - 1
        elif p_ind == self.page_count() - 1:
            return self.item_count() - (self.page_count() - 1) * self.items_per_page
        return self.items_per_page