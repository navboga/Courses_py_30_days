class warehouse(object):
    def __init__(self,adress,counf_of_places):
        self.adress=adress
        self.count_of_places=counf_of_places
    def try_insert_prodact(self,prodact,reserv_warehouse=None):
        if self.count_of_places - prodact.size >=0:
            print('Accepted')
            self.count_of_places-=prodact.size
        else:
            print('no space left')
            if not reserv_warehouse:
                return

            other_reserv_warehouse = None
            for p in reserv_warehouse:
                if p.count_of_places - prodact.size >=0:
                    other_reserv_warehouse = p
                    break

