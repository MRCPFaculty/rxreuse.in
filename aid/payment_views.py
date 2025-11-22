import razorpay
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from aid.models import AidApplication

# Initialize Razorpay Client
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required
def initiate_shipping_payment(request, application_id):
    application = get_object_or_404(AidApplication, id=application_id, beneficiary=request.user)
    
    if application.status != AidApplication.Status.APPROVED:
        return redirect('aid_dashboard')

    # Calculate amount (e.g., fixed shipping fee of ₹100 for now)
    amount = 10000  # Amount in paise (₹100)
    currency = 'INR'

    # Create Razorpay Order
    data = { "amount": amount, "currency": currency, "receipt": str(application.id) }
    payment = client.order.create(data=data)

    application.razorpay_order_id = payment['id']
    application.shipping_fee = amount / 100
    application.save()

    context = {
        'payment': payment,
        'key_id': settings.RAZORPAY_KEY_ID,
        'application': application
    }
    return render(request, 'aid/payment_page.html', context)

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id', '')
        order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')

        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            
            # Update Application Status
            application = AidApplication.objects.get(razorpay_order_id=order_id)
            application.razorpay_payment_id = payment_id
            application.status = AidApplication.Status.PAID
            application.save()
            
            return render(request, 'aid/payment_success.html')
        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Payment Verification Failed")
    return redirect('aid_dashboard')
