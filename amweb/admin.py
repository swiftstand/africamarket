from django.contrib import admin
from users.models import User, SellerProfile, AdminProfile, BuyerProfile,ShelfFlags
from inventory.models import ShelfOne,ShelfTwo,ShelfThree,ShelfFour,ShelfFive
from inventory.models import (ItemShelfOne,ItemShelfTwo,ItemShelfThree,ItemShelfFour,ItemShelfFive)
from amweb.models import AdminPost
# Register your models here.
admin.site.register(User)
admin.site.register(AdminPost)
admin.site.register(AdminProfile)
admin.site.register(ShelfOne)
admin.site.register(ShelfTwo)
admin.site.register(ShelfThree)
admin.site.register(ShelfFour)
admin.site.register(ShelfFive)
admin.site.register(ItemShelfOne)
admin.site.register(ItemShelfTwo)
admin.site.register(ItemShelfThree)
admin.site.register(ItemShelfFour)
admin.site.register(ItemShelfFive)
admin.site.register(SellerProfile)
admin.site.register(BuyerProfile)
admin.site.register(ShelfFlags)
