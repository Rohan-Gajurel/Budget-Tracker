from django.shortcuts import render, HttpResponseRedirect
from budget_tracker_app.models import Transaction

# Create your views here.
def transaction_list(request):
    transactions=Transaction.objects.all()
    total_balance =0
    for t in transactions:
        if t.type=="Income":
            total_balance=t.amount+total_balance
        else:
            total_balance=total_balance-t.amount
        
    return render(
        request,
        "list_transaction.html", {"transactions":transactions,
         "total_balance":total_balance}

    )

def delete_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    transaction.delete()
    return HttpResponseRedirect("/")

def create_transaction(request):
    if request.method=="GET":
        return render(
        request,
        "create_transaction.html",
    )
    else:
        title=request.POST['title']
        amount=request.POST['amount']
        category=request.POST['category']
        type=request.POST['type']
        Transaction.objects.create(title=title,amount=amount, category=category,type=type)
        return HttpResponseRedirect("/")


def filter_transaction(request):
   
    if request.GET['search'] in ["Income", "income"]:
        transactions=Transaction.objects.filter(type="Income")
        total_balance =0
        for t in transactions:
            if t.type=="Income":
                total_balance=t.amount+total_balance
            else:
                total_balance=total_balance-t.amount
        return render(
        request,
        "list_transaction.html",
        {"transactions":transactions,
         "total_balance":total_balance}
    )

    elif request.GET['search'] in ["Expense","expense"]:
        transactions=Transaction.objects.filter(type="Expense")
        total_balance =0
        for t in transactions:
            if t.type=="Income":
                total_balance=t.amount+total_balance
            else:
                total_balance=total_balance-t.amount
        return render(
        request,
        "list_transaction.html",
        {"transactions":transactions,
         "total_balance":total_balance}
    )

    else:
        transaction_list()


    