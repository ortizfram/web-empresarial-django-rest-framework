from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status

# To send mails, having an account in https://www.activecampaign.com
# is a must. also get credentials: /app/settings/developer
from django.conf import settings
import requests
activecampaign_url = settings.ACTIVE_CAMPAIGN_URL
activecampaign_key = settings.ACTIVE_CAMPAIGN_KEY

class ContactCreateView(APIView):
    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        phone = data['phone']
        budget = data['budget']

# *** Send Email
        try:
            
            send_mail(
                subject,
                'Name '
                + name
                + '\nEmail: '
                + email
                + '\n\nMessage:\n'
                + message
                + '\nPhone: '
                + phone
                + '\n\nBudget: '
                + budget,
                'ortizfranco48@yahoo.com',
                ['ortizfranco48@yahoo.com'],
                fail_silently=False
            )
            

# *** CREATE CONTACT
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                phone=phone,
                message=message,
                budget=budget,
            )

# *** CREATE ACTIVE CAMPAIGN CONTACT
            url = activecampaign_url + '/api/3/contact/sync'
            data = {
                "contact":{
                    "email": email,
                    "firstName": name,
                    "phone": phone,
                }
            }

            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Api-Token': activecampaign_key
            }

            response = requests.post(url, json=data, headers=headers)
            if response.status_code != 201 and response.status_code != 200:
                return Response(
                    {'error': 'Something went wrong when creating contact'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            contact = response.json()

            try:
                contact_id = str(contact['contact']['id'])
            except:
                return Response(
                    {'error': 'Something went wrong when getting contact ID'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
# *** Add to TAGs (ACTIVE CAMPAIGN)
            url = activecampaign_url + '/api/3/contactTags'
            data = {
                'contactTag': {
                    'contact': contact_id,
                    'tag': '2'
                }
            }
            response = requests.post(url, json=data, headers=headers)
            if response.status_code != 201 and response.status_code != 200:
                return Response(
                    {'error': 'Something went wrong when adding tag to contact'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

# *** Add to list (ACTIVE CAMPAIGN)
            url = activecampaign_url + '/api/3/contactLists'
            data = {
                'contactList': {
                    'list': '1',
                    'contact': contact_id,
                    'status': '1'
                }
            }

            response = requests.post(url, json=data, headers=headers)

            if response.status_code != 201 and response.status_code != 200:
                return Response(
                    {'error': 'Something went wrong when adding contact to master list'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response({'success': 'Message sent successfully'})
        except:
            return Response({'error': 'Message failed to be sent'})
       