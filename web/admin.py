from django.contrib import admin
from .models import MainPageInfo
from .models import Demand
from .models import Navigation
from .models import Geography

admin.site.register(MainPageInfo)
admin.site.register(Demand)
admin.site.register(Navigation)
admin.site.register(Geography)