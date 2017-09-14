from django.contrib import admin



from .models import farmer,retailer,crop,sell,qty,fcomplain,rcomplain,r_ad_details


admin.site.register(farmer)
admin.site.register(retailer)
admin.site.register(crop)
admin.site.register(sell)
admin.site.register(qty)
admin.site.register(fcomplain)
admin.site.register(rcomplain)
admin.site.register(r_ad_details)



