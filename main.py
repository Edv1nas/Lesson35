# from typing import List


# class MyList:
#     def __init__(self, items: list) -> None:
#         self.items = items


# my_list = MyList(items=[1, 2, 3])

# print(bool(my_list))

# my_list = [1, 2, 3, 4, 5]

# print(len(my_list))

"""Create a class called Product that takes a name and price as parameters and has __str__ and __repr__ methods defined.

The __str__ method should return a string in the format "Product: name, Price: price"
The __repr__ method should return a string in the format "Product('name', price)"""


# class Product:
#     def __init__(self, name: str, price: float) -> None:
#         self.name = name
#         self.price = price

#     def __str__(self) -> str:
#         return f"Product: {self.name}, Price: {self.price}"

#     def __repr__(self) -> str:
#         return f"Product: {self.name},{self.price}"


# product = Product(name="obuolis", price="1.2")
# print(product)
# print(repr(product))


"""Task Nr.2:

Create a class called MyQueue that has __bool__, __repr__ and __len__ methods defined.

The __bool__ method should return True if the queue has any items and False if it is empty.
The __repr__ method should return a string in the format MyQueue(items) where items is the list of items in the queue.
The __len__ method should return the number of items in the queue."""


# from typing import List, Optional


# class MyQueue:
#     def __init__(self) -> None:
#         self.items: List[Optional[int]] = []

#     def __bool__(self) -> bool:
#         return bool(self.items)

#     def __repr__(self) -> str:
#         return f"MyQueue:({self.items})"

#     def __len__(self) -> int:
#         return len(self.items)


# myqueue = MyQueue()
# print(bool(myqueue))

# myqueue.items.append(1)
# print(bool(myqueue))
# print(repr(myqueue))
# print(len(myqueue))

""""Task Nr.4:

Create three different task with real world scenario what would include all magic methods we covered today and plus 3 others from the provided list."""




from typing import List, Optional
class ShoppingCart:
    def __init__(self):
        self.items: List[Optional[str]] = []

    def __str__(self) -> List[Optional[str]]:
        return f"Shopping cart with {(self.items)} items"

    def __repr__(self) -> List[Optional[str]]:
        return f"ShoppingCart: ({self.items})"

    def __add__(self, item) -> list:
        new_cart = ShoppingCart()
        new_cart.items = self.items + [item]
        return new_cart

    def __len__(self) -> int:
        return len(self.items)

    def __bool__(self) -> bool:
        return bool(self.items)

    def __getitem__(self, index) -> str:
        return self.items[index]

    def __delitem__(self, index) -> str:
        del self.items[index]

    def __contains__(self, item) -> bool:
        return item in self.items


shoppingcart = ShoppingCart()
print(bool(shoppingcart))

shoppingcart.items.append("apple")
shoppingcart.items.append("lemon")
shoppingcart.items.append("orange")
shoppingcart.items.append("dumpling")

print(shoppingcart[3])

print(bool(shoppingcart))
del shoppingcart[0]

print(len(shoppingcart))
print(shoppingcart)
print(repr(shoppingcart))

new_cart = shoppingcart + "grikiai"
print(f"New shopping cart: {new_cart.items}")

print("lemon" in shoppingcart)
