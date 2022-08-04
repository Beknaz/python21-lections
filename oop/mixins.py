"===============Миксины=============="
# Миксин - класс, который будет использоваться для наследования, от миксинов не создаются обьекты.
class Createmixin:
    def product_create(self, title, price):
        model = self.__class__
        _id = model._id
        self.title = title
        self.price = price
        self.id = _id
        model.objects[_id] = self
        model._id += 1
class ReadMixin:
    def product_detail(self, p_id):
        from pprint import pprint
        model = self.__class__
        obj = model.objects.get(p_id)
        print({"id":self.id, "title":self.title, "price":self.price})
class UpdateMixin:
    ...
class DeleteMixin:
    def delete_product(self, p_id):
        model = self.__class__
        model.objects.pop(p_id)

class ProductCRUD(Createmixin, ReadMixin, UpdateMixin, DeleteMixin):
    objects = {}
    _id = 1
    
crud = ProductCRUD()
crud.product_create("obj1", 4)
crud.product_create("obj2", 46)
crud.product_detail(1)
crud.product_detail(1)
crud.delete_product(2)
print(crud.objects)

