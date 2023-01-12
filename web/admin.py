from django.contrib import admin
from .models import MainPageInfo
from .models import Demand
from .models import Navigation
from .models import Geography
from .models import Skills
from .models import LastVacancies

admin.site.register(MainPageInfo)
admin.site.register(Demand)
admin.site.register(Navigation)
admin.site.register(Geography)
admin.site.register(Skills)
admin.site.register(LastVacancies)
