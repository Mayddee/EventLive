from django.http import JsonResponse
import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Booking
from django.core.serializers import serialize

from .serializers import EventSerializer, BookingSerializer
from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
from django.utils import timezone
from django.contrib import messages
from .models import Event, Booking
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def event_list(request):
    events = Event.objects.all()

    if request.method == 'GET':
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(["GET", "POST"])
def booking_list(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk):
    event = get_object_or_404(Event, id=pk)
    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
@api_view(['GET'])
def event_list_by_category(request, c):
    if request.method == 'GET':
        events = Event.objects.filter(category=c)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data) 
    else:
        return Response({'error': 'Method not allowed'}, status=405)
    

@api_view(['GET'])
def category_list(request):
    event_categories = Event.EVENT_CATEGORIES
    serialized_data = json.dumps([{'code': code, 'name': name} for code, name in event_categories])
    return JsonResponse(serialized_data, safe=False)

@login_required
@api_view(['GET', 'POST', 'PUT'])
def user_bookings(request):
    if not request.user.is_authenticated:
        return Response({'error': 'First register to book the event.'})
    bookings = Booking.objects.filter(participant=request.user)

    if request.method == 'GET':
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(participant=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        try: 
            booking_id = request.data.get('id')
            booking = Booking.objects.get(id=booking_id, participant=request.user)
            serializer = BookingSerializer(booking, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def user_booking(request, pk):
    if not request.user.is_authenticated:
        return Response({'error': 'First register to book the event.'})
    
    booking = Booking.objects.get(id=pk, participant=request.user)
   
    if request.method == 'GET':
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        booking.delete()
        return Response({'message': 'Booking deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@login_required
@api_view(['POST'])
def book_event(request, pk):
    if not request.user.is_authenticated:
        return Response({'error': 'You must be logged in to book an event.'}, status=status.HTTP_403_FORBIDDEN)
    
    event = get_object_or_404(Event, id=pk)
    
    if Booking.objects.filter(participant=request.user, event=event).exists():
        return Response({'error': 'You have already booked for this event.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if event.available_seats <= 0:
        return Response({'error': 'No available seats for this event.'}, status=status.HTTP_400_BAD_REQUEST)
    
    booking = Booking(participant=request.user, event=event)
    booking.save()
    event.available_seats -= 1
    event.participants.add(request.user)  
    event.save()
    
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return redirect('booking_success')

#  @api_view(['GET'])
# def actor_list(request):
#     actors = Actor.objects.all()
#     serializer = ActorSerializer(actors, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def actor_movies(request, actor_id):
#     actor = get_object_or_404(Actor, pk=actor_id)
#     movies = Movie.objects.filter(actors=actor)
#     tv_series = TVSeries.objects.filter(actors=actor)
#     movie_serializer = MovieSerializer(movies, many=True)
#     tv_series_serializer = TVSeriesSerializer(tv_series, many=True)
#     data = {
#         'movies': movie_serializer.data,
#         'tv_series': tv_series_serializer.data
#     }
#     return Response(data)

# @login_required
# class EventListView(APIView):
#     def get(self, request, format=None):
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @login_required
# def book_event(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     if request.method == 'POST':
#         booking = Booking.objects.create(
#             participant=request.user,
#             event=event
#         )
#         return redirect('booking_success')
#     else:
#         return render(request, 'book_event.html', {'event': event})

@login_required
def booking_success(request):
    return render(request, 'booking_success.html')

def create_event(request):
    if request.method == 'POST':
        event = Event.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            ticket_cost=request.POST.get('ticket_cost'),
            date=request.POST.get('date')
        )
        return redirect('event_list')
    return render(request, 'create_event.html')

@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        event.location = request.POST.get('location')
        event.ticket_cost = request.POST.get('ticket_cost')
        event.date = request.POST.get('date')
        event.save()
        return redirect('event_list')
        
    return render(request, 'update_event.html', {'event': event})

