
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.shortcuts import get_object_or_404
from django.forms import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


class ProcessParking(APIView):
    def post(self, request):
        address = request.data.get('address')
        duriation = request.data.get('duriation')
        parking_number = request.data.get('parking_number')
        price = request.data.get('price')
        print("ppppppppppppppppppppppppp", price)
        # account = Parking.objects.get(1)

        processed_parking = Parking(
            address=address,
            duriation=duriation,
            parking_status="Ongoing",
            parking_number=parking_number,
            price=int(price),
            account_bal=20- price
        )

        processed_parking.save()
        processed_parking_dict = model_to_dict(processed_parking)
        processed_parking_dict["entryTime"]= processed_parking.entry_time
        processed_parking_dict["exitTime"]=processed_parking.exit_time

        return Response([
                {"message": "Parking slot successifuly booked!"},
                {"response": processed_parking_dict}], 
                status=status.HTTP_201_CREATED
            )
    
        # else:
        #     return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    



        # if request.user.is_authenticated:
        #     processed_parking = Parking(
        #         address=address,
        #         duriation=duriation,
        #         parking_status="Ongoing",
        #         parking_number=parking_number,
        #         price=price,
        #         owner=request.user
        #     )

            # processed_parking.save()
            # processed_parking_dict = model_to_dict(processed_parking)
            # processed_parking_dict["entryTime"]= processed_parking.entryTime
            # processed_parking_dict["exitTime"]=processed_parking.exitTime
