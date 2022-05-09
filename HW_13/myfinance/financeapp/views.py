from django.shortcuts import render
from .models import Income, Outcome, Category
from .forms import CategoryForm, IncomeForm, OutcomeForm, DateSliceForm
from django.db import connection


def index(request):
    income = Income.objects.all()
    outcome = Outcome.objects.all()
    category = Category.objects.all()
    context = {'income': income,
               'outcome': outcome,
               'category': category,
               }
    return render(request, template_name='pages/index.html', context=context)


def add_income(request):
    if request.method == 'POST':
        sum = request.POST['sum']
        sum_to_db = Income(sum=sum)
        sum_to_db.save()
        form = IncomeForm
    else:
        form = IncomeForm
    return render(request, 'pages/add_income.html', {'form': form})


def add_outcome(request):
    if request.method == 'POST':
        sum = request.POST['sum']
        category = request.POST['category']
        outcome_to_db = Outcome(sum=sum, category_id=Category.objects.get(pk=int(category)))
        outcome_to_db.save()
        form = OutcomeForm
    else:
        form = OutcomeForm
    return render(request, 'pages/add_outcome.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        sum_to_db = Category(name=name)
        sum_to_db.save()
        form = CategoryForm
    else:
        form = CategoryForm
    return render(request, 'pages/add_category.html', {'form': form})


def show_detail(request):
    form = None
    context = {'form': form, }
    with connection.cursor() as cursor:
        sql = """
        select SUM(i.sum) - SUM(o.sum) as balance
        from financeapp_outcome o, financeapp_income i"""
        cursor.execute(sql)
        balance = cursor.fetchone()
        for item in balance:
            context.update({'balance': item})
    if request.method == 'POST':
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        context.update({'form': DateSliceForm})
        context.update({'date_from': date_from})
        context.update({'date_to': date_to})
        # qs = Outcome.objects.filter(created_at__lte=date_to, created_at__gte=date_from)
        
        with connection.cursor() as cursor:
            sql = """
            select SUM(o.sum), o.created_at
            from financeapp_outcome as o
            where created_at >= %s AND created_at <= %s
            group by o.created_at"""
            cursor.execute(sql, [date_from, date_to])
            outcome_in_period = cursor.fetchall()
            sum_list = []
            date_list = []
            for item in outcome_in_period:
                sum_list.append(item[0])
                date_list.append(item[1])
                context.update({'sum_outcome': sum_list})
                context.update({'date_outcome': date_list})
        
        with connection.cursor() as cursor:
            sql = """
            select SUM(o.sum), o.created_at
            from financeapp_income as o
            where created_at > %s AND created_at <= %s
            group by o.created_at"""
            cursor.execute(sql, [date_from, date_to])
            income_in_period = cursor.fetchall()
            sum_list = []
            date_list = []
            for item in income_in_period:
                sum_list.append(item[0])
                date_list.append(item[1])
                context.update({'sum_income': sum_list})
                context.update({'date_income': date_list})
        
        with connection.cursor() as cursor:
            sql = """
            select SUM(o.sum), fc.name
            from financeapp_outcome as o
            LEFT JOIN financeapp_category fc ON fc.id = o.category_id_id
            where created_at >= %s AND created_at <= %s
            group by fc.name
            """
            cursor.execute(sql, [date_from, date_to])
            category_sum_in_period = cursor.fetchall()
            sum_list = []
            name_list = []
            for item in category_sum_in_period:
                sum_list.append(item[0])
                name_list.append(item[1])
                context.update({'sum_category': sum_list})
                context.update({'category_name': name_list})
        
        with connection.cursor() as cursor:
            sql = """
            select SUM(o.sum)
            from financeapp_outcome o
            where created_at >= %s AND created_at <= %s"""
            cursor.execute(sql, [date_from, date_to])
            outcome_in_period = cursor.fetchone()
            for item in outcome_in_period:
                context.update({'outcome_in_period': item})
        
        with connection.cursor() as cursor:
            sql = """
            select SUM(i.sum)
            from financeapp_income i
            where created_at >= %s AND created_at <= %s"""
            cursor.execute(sql, [date_from, date_to])
            income_in_period = cursor.fetchone()
            for item in income_in_period:
                context.update({'income_in_period': item})
    else:
        context.update({'form': DateSliceForm})
    return render(request, 'pages/show_detail.html', context)
