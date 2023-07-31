from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


@api_view(['GET', 'POST'])
def transaction_list(request):
    """
    List all transactions or create a new transaction
    """

    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['order_price'] = round(float(request.data['price']) * float(request.data['quantity']), 2)
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def transaction_detail(request, pk):
    """
    Retrieve, update, or delete a transaction
    """
    try:
        transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

