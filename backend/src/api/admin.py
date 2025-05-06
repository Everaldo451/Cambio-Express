from django.contrib import admin
from api.models import Company, FeedBack, User
from marketplace.models import Transaction, Offert


admin.site.register(User)
admin.site.register(Company)
admin.site.register(FeedBack)
admin.site.register(Transaction)
admin.site.register(Offert)

