from django.contrib import admin
from .models import Flow, UpdateLog
from datetime import datetime
import requests


def update_levels():
    # for flowtype in ['00060', '00065']:
        site_ids = Flow.objects.all().values_list('site_id', flat=True)

        r = requests.get("http://waterservices.usgs.gov/nwis/iv", {
            "sites": ','.join(map(str, site_ids)),
            "parameterCd": "00060,00065,00010",
            "format": "json,1.1",
            "period": 'PT4H'
        })

        if r.status_code == requests.codes.ok:
            response = r.json()

            for item in response['value']['timeSeries']:
                site_id = item['sourceInfo']['siteCode'][0]['value']
                parameter = item['variable']['variableCode'][0]['value']

                num_of_elements = item['values'][0]['value'].__len__()
                latest = float(item['values'][0]['value'][num_of_elements - 1]['value'])
                old = float(item['values'][0]['value'][num_of_elements - 5]['value'])
                change = latest - old

                if parameter == '00060':
                    Flow.objects.filter(
                            site_id=site_id
                    ).update(latest_flow=latest, flow_change=change)
                elif parameter == '00065':
                    Flow.objects.filter(
                            site_id=site_id
                    ).update(latest_height=latest, height_change=change)
                elif parameter == '00010':
                    Flow.objects.filter(
                            site_id=site_id
                    ).update(temperature=latest)
            # disable logging to prevent filling up hobby database for now
            # UpdateLog.objects.create(success=True)

        else:
            pass
            # UpdateLog.objects.create(success=False)


def update(self, request, queryset):
    update_levels()

    return request


update.short_description = "Update Flows"


class FlowAdmin(admin.ModelAdmin):
    readonly_fields = ('latest_height', 'latest_flow', 'height_change', 'flow_change')

    list_display = ('name', 'latest_height', 'height_change', 'latest_flow', 'flow_change', 'temperature')

    actions = [update]

    # change_list_template = 'usgsflows/templates/admin/change_list.html'

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'update':
            post = request.POST.copy()
            for u in Flow.objects.all():
                post.update({admin.ACTION_CHECKBOX_NAME: str(u.id)})
            request._set_post(post)

        return super(FlowAdmin, self).changelist_view(request, extra_context)

    class Media:
        js = ('admin/js/jquery-1.12.0.min.js',
              'admin/js/jquery.countdown.min.js')

admin.site.register(Flow, FlowAdmin)
