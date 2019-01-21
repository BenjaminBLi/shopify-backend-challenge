import graphene
from graphene_django import DjangoObjectType

from .models import Item, Purchase

class ItemType(DjangoObjectType):
    class Meta:
        model = Item

class PurchaseType(DjangoObjectType):
    class Meta:
        model = Purchase

class Query(graphene.ObjectType):
    items = graphene.List(ItemType)#, ignore_empty=graphene.Boolean(default_value=False))
    items_ignore_empty = graphene.List(ItemType)#, ignore_empty=graphene.Boolean(default_value=False))
    purchases = graphene.List(PurchaseType)#, ignore_empty=graphene.Boolean(default_value=False))


    def resolve_items(self, info):
        return Item.objects.all()

    def resolve_items_ignore_empty(self, info):
        return Item.objects.all().filter(inventory_count__gt=0)

    def resolve_purchases(self, info):
        return Purchase.objects.all()

class CreateItem(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    price = graphene.Int()
    inventory_count = graphene.Int()
    genre = graphene.String()

    class Arguments:
        title = graphene.String()
        price = graphene.Int() #representing graphene as an int, where the last two digits are the cents value
        inventory_count = graphene.Int()
        genre = graphene.String()

    def mutate(self, info, title, price, inventory_count, genre):
        item = Item(
            title=title,
            price=price,
            inventory_count=inventory_count,
            genre=genre,
        )

        item.save()

        return CreateItem(
            title=item.title,
            price=item.price,
            inventory_count=item.inventory_count,
            genre=item.genre,
        )


class CreatePurchase(graphene.Mutation):
    item = graphene.Field(ItemType)

    class Arguments:
        item_title = graphene.String()

    def mutate(self, info, item_title):
        valid_items = Item.objects.all().filter(title=item_title)
        all_purchases = Purchase.objects.all()

        count = 0

        for purchase in all_purchases:
            if purchase.item in valid_items:
                count += 1

        total_inventory = 0

        for i in range(valid_items.count()):
            item = valid_items[i]
            total_inventory += item.inventory_count

            if total_inventory > count:
                item.inventory_count -= 1
                item.save()

                purchase = Purchase(i)
                purchase.save()
                return CreatePurchase(item)

        raise Exception("out of inventory")



class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
    create_purchase = CreatePurchase.Field()

