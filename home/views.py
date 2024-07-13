from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, Order, Subscriber
from datetime import datetime
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    # Render the index.html template with the context dictionary
    return render(request, "index.html")
    # return HttpResponse("this is homepage")

def about(request):
    # Render the about.html template
    return render(request, "about.html")
    # return HttpResponse("this is about page")

def cake(request):
    # Render the cake.html template
    return render(request, "cake.html")
    # return HttpResponse("this is services page")

def chocolate(request):
    # Render the chocolate.html template
    return render(request, "chocolate.html")
    # return HttpResponse("this is services page")

def icecream(request):
    # Render the icecream.html template
    return render(request, "icecream.html")
    # return HttpResponse("this is services page")

def privacy(request):
    # Render the privacy.html template
    return render(request, "privacy.html")

def terms(request):
    # Render the terms.html template
    return render(request, "terms.html")

def contact(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Get the form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Check if all fields are filled
        if name and email and message:
            # Create a new Contact object and save it to the database
            contact = Contact(name=name, email=email, message=message, timestamp=datetime.today())
            contact.save()
            # Add a success message
            messages.success(request, 'Your message has been sent successfully!')
        else:
            # Add an error message if any field is missing
            messages.error(request, 'Please fill out all fields.') 
      
    # Render the contact.html template
    return render(request, "contact.html")
    # return HttpResponse("this is contact page")

def order_confirmation(request):
    # Get the item details from the query parameters
    item = request.GET.get('item')
    price = float(request.GET.get('price', 0))
    image_url = request.GET.get('image_url')
    
    # Get the quantity from POST request or default to 1
    quantity = int(request.POST.get('quantity', 1)) if request.method == 'POST' else 1
    total_price = price * quantity
    
    # Context dictionary to pass to the template
    context = {
        'item': item,
        'price': price,
        'image_url': image_url,
        'quantity': quantity,
        'total_price': total_price
    }
    
    # Render the order_confirmation.html template with the context dictionary
    return render(request, 'order_confirmation.html', context) 

def order_summary(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the form data from the request
        item = request.POST.get('item')
        price = float(request.POST.get('price', 0))
        image_url = request.POST.get('image_url')
        quantity = int(request.POST.get('quantity', 1))
        total_price = price * quantity
        
        # Get the customer details from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')

        # Check if the 'confirm' button was pressed
        if 'confirm' in request.POST:
            # Save the order to the database
            order = Order(
                item=item, price=price, quantity=quantity, total_price=total_price,
                name=name, email=email, phone=phone, street=street, city=city,
                state=state, postal_code=postal_code, country=country
            )
            order.save()
            # Add a success message and redirect to home page
            messages.success(request, 'Your order has been successfully placed!')
            return redirect('home')
        
        # Context dictionary to pass to the template
        context = {
            'item': item,
            'price': price,
            'image_url': image_url,
            'quantity': quantity,
            'total_price': total_price,
            'name': name,
            'email': email,
            'phone': phone,
            'street': street,
            'city': city,
            'state': state,
            'postal_code': postal_code,
            'country': country
        }
        # Render the order_summary.html template with the context dictionary
        return render(request, 'order_summary.html', context)
    else:
        # Redirect to order_confirmation if not a POST request
        return redirect('order_confirmation') 
    
@csrf_exempt
def subscribe(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the email from the request
        email = request.POST.get('email')
        
        if email:
            # Check if the email already exists in the database
            if not Subscriber.objects.filter(email=email).exists():
                # Save the new subscriber to the database
                subscriber = Subscriber(email=email)
                subscriber.save()
                # Add a success message
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                # Add an info message if the email is already subscribed
                messages.info(request, 'You are already subscribed to our newsletter.')
        else:
            # Add an error message if the email is not valid
            messages.error(request, 'Please enter a valid email address.')
    
    # Redirect to the home page
    return redirect('home')   

def search_results(request):
    # Get the search query from the request
    query = request.GET.get('query', None)

    # Check if a query was provided
    if query:
        # Convert query to lowercase for case-insensitive comparison
        query_lower = query.lower()

        # Define base URL for images stored in static folder
        base_img_url = '/static/img/'

        # Check for specific search terms and redirect to order confirmation with appropriate item details
        # Check for specific search terms related to cakes
        if 'cake' in query_lower:
            if 'chocolate' in query_lower:
                # Redirect to order confirmation page with Chocolate Cake details
                return redirect(reverse('order_confirmation') + f'?item=Chocolate%20Cake&price=25&image_url={base_img_url}cake-Chocolate%20Cake')
            elif 'vanilla' in query_lower:
                # Redirect to order confirmation page with Vanilla Cake details
                return redirect(reverse('order_confirmation') + f'?item=Vanilla%20Cake&price=20&image_url={base_img_url}cake-Vanilla%20Cake')
            elif 'red velvet' in query_lower:
                # Redirect to order confirmation page with Red Velvet Cake details
                return redirect(reverse('order_confirmation') + f'?item=Red%20Velvet%20Cake&price=30&image_url={base_img_url}cake-Red%20Velvet%20Cake')
            elif 'fruit' in query_lower:
                # Redirect to order confirmation page with Fruit Cake details
                return redirect(reverse('order_confirmation') + f'?item=Fruit%20Cake&price=28&image_url={base_img_url}cake-Fruit%20Cake')
            elif 'cheesecake' in query_lower:
                # Redirect to order confirmation page with Cheesecake details
                return redirect(reverse('order_confirmation') + f'?item=Cheesecake&price=35&image_url={base_img_url}cake-Cheesecake')
            elif 'cupcake' in query_lower:
                # Redirect to order confirmation page with Cupcake details
                return redirect(reverse('order_confirmation') + f'?item=Cupcake&price=15&image_url={base_img_url}cake-Cupcake')
            else:
                # Display an error message and redirect to home page if no specific item found
                messages.error(request, 'Item not found. Please try again.')
                return redirect('home')

        elif 'mint chocolate chip' in query_lower: # Check for specific query first
            # Redirect to order confirmation page with Mint Chocolate Chip Ice Cream details
            return redirect(reverse('order_confirmation') + f'?item=Mint%20Chocolate%20Chip%20Ice%20Cream&price=6&image_url={base_img_url}ice%20cream-Mint%20Chocolate%20Chip')          
        elif 'chocolate' in query_lower: # Check for specific query first
            # Redirect to order confirmation page with Chocolate Ice Cream details
            return redirect(reverse('order_confirmation') + f'?item=Chocolate%20Ice%20Cream&price=6&image_url={base_img_url}ice%20cream-Chocolate%20Ice%20Cream')          
        
        # Check for specific search terms related to chocolates
        elif 'chocolate' in query_lower:
            if 'dark' in query_lower:
                # Redirect to order confirmation page with Dark Chocolate details
                return redirect(reverse('order_confirmation') + f'?item=Dark%20Chocolate&price=10&image_url={base_img_url}chocolate-Dark%20Chocolate')
            elif 'milk' in query_lower:
                # Redirect to order confirmation page with Milk Chocolate details
                return redirect(reverse('order_confirmation') + f'?item=Milk%20Chocolate&price=8&image_url={base_img_url}chocolate-Milk%20Chocolate')
            elif 'white' in query_lower:
                # Redirect to order confirmation page with White Chocolate details
                return redirect(reverse('order_confirmation') + f'?item=White%20Chocolate&price=9&image_url={base_img_url}chocolate-White%20Chocolate')
            elif 'assorted' in query_lower:
                # Redirect to order confirmation page with Assorted Chocolates details
                return redirect(reverse('order_confirmation') + f'?item=Assorted%20Chocolates&price=15&image_url={base_img_url}chocolate-Assorted%20Chocolates')
            elif 'truffles' in query_lower:
                # Redirect to order confirmation page with Chocolate Truffles details
                return redirect(reverse('order_confirmation') + f'?item=Chocolate%20Truffles&price=12&image_url={base_img_url}chocolate-Chocolate%20Truffles')
            elif 'bars' in query_lower:
                # Redirect to order confirmation page with Chocolate Bars details
                return redirect(reverse('order_confirmation') + f'?item=Chocolate%20Bars&price=7&image_url={base_img_url}chocolate-Chocolate%20Bars')
            else:
                # Display an error message and redirect to home page if no specific item found
                messages.error(request, 'Item not found. Please try again.')
                return redirect('home')

        # Check for specific search terms related to Ice Creams
        elif 'ice cream' in query_lower:
            if 'vanilla' in query_lower:
                # Redirect to order confirmation page with Vanilla Ice Cream details
                return redirect(reverse('order_confirmation') + f'?item=Vanilla%20Ice%20Cream&price=5&image_url={base_img_url}ice%20cream-Vanilla%20Ice%20Cream')          
            elif 'strawberry' in query_lower:
                # Redirect to order confirmation page with Strawberry Ice Cream details
                return redirect(reverse('order_confirmation') + f'?item=Strawberry%20Ice%20Cream&price=5&image_url={base_img_url}ice%20cream-Strawberry%20Ice%20Cream')
            elif 'cookies and cream' in query_lower:
                # Redirect to order confirmation page with Cookies and Cream Ice Cream details
                return redirect(reverse('order_confirmation') + f'?item=Cookies%20and%20Cream%20Ice%20Cream&price=7&image_url={base_img_url}ice%20cream-Cookies%20and%20Cream')
            elif 'pistachio' in query_lower:
                # Redirect to order confirmation page with Pistachio Ice Cream details
                return redirect(reverse('order_confirmation') + f'?item=Pistachio%20Ice%20Cream&price=8&image_url={base_img_url}ice%20cream-Pistachio%20Ice%20Cream')
            else:
                # Display an error message and redirect to home page if no specific item found
                messages.error(request, 'Item not found. Please try again.')
                return redirect('home')
        else:
            # Display an error message and redirect to home page if no query was provided
            messages.error(request, 'Item not found. Please try again.')
            return redirect('home')
    else:
        # Display an error message and redirect to home page if no query was provided
        messages.error(request, 'Please enter a search query.')
        return redirect('home')
