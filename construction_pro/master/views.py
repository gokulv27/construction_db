from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmployeeRole, EmployeeType, VendorType, Brand
from .forms import EmployeeRoleForm, EmployeeTypeForm, VendorTypeForm, BrandForm
import json

def master_list(request):
    return render(request, 'master_dashboard.html')

@csrf_exempt
def api_items(request, item_type=None, pk=None):
    if request.method == 'GET':
        items = []
        items.extend([{'id': item.id, 'name': item.name, 'type': 'employee_role'} for item in EmployeeRole.objects.all()])
        items.extend([{'id': item.id, 'name': item.name, 'type': 'employee_type'} for item in EmployeeType.objects.all()])
        items.extend([{'id': item.id, 'name': item.name, 'type': 'vendor_type'} for item in VendorType.objects.all()])
        items.extend([{'id': item.id, 'name': item.name, 'type': 'brand'} for item in Brand.objects.all()])
        return JsonResponse(items, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        
        if item_type == 'employee_role':
            form = EmployeeRoleForm(data)
            model = EmployeeRole
        elif item_type == 'employee_type':
            form = EmployeeTypeForm(data)
            model = EmployeeType
        elif item_type == 'vendor_type':
            form = VendorTypeForm(data)
            model = VendorType
        elif item_type == 'brand':
            form = BrandForm(data)
            model = Brand
        else:
            return JsonResponse({'error': 'Invalid item type'}, status=400)

        if form.is_valid():
            if pk:
                item = model.objects.get(pk=pk)
                item.name = name
                item.save()
            else:
                item = form.save()
            return JsonResponse({'id': item.id, 'name': item.name, 'type': item_type})
        else:
            return JsonResponse({'error': form.errors}, status=400)

    elif request.method == 'DELETE':
        if item_type == 'employee_role':
            model = EmployeeRole
        elif item_type == 'employee_type':
            model = EmployeeType
        elif item_type == 'vendor_type':
            model = VendorType
        elif item_type == 'brand':
            model = Brand
        else:
            return JsonResponse({'error': 'Invalid item type'}, status=400)

        try:
            item = model.objects.get(pk=pk)
            item.delete()
            return JsonResponse({'success': True})
        except model.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=405)