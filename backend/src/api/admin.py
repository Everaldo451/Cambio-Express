from django.contrib import admin
from api.models import Company, FeedBack, User, Transaction, Offert, Account


admin.site.register(User)
admin.site.register(Company)
admin.site.register(FeedBack)
admin.site.register(Transaction)
admin.site.register(Offert)
admin.site.register(Account)

