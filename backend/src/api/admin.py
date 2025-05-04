from django.contrib import admin
from api.models import Company, FeedBacks, User
from marketplace.models import Transaction, Offert


admin.site.register(User)
admin.site.register(Company)
admin.site.register(FeedBacks)
admin.site.register(Transaction)
admin.site.register(Offert)

