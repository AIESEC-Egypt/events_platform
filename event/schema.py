import graphene
from graphene_django import DjangoObjectType
from .models import *
from .expa import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import get_token as create_jwt_token
import graphql_jwt


# class UserType(DjangoObjectType):
#     class Meta:
#         model = get_user_model()


# class ProfileType(DjangoObjectType):
#     class Meta:
#         model = Profile


# class LocalConferenceDelegateType(DjangoObjectType):
#     class Meta:
#         model = LocalConferenceDelegate
#         fields = ("name", "gender", "phone_number", "email", "cv", "indemnity_form",
#                   "id_front", "id_back", "time_stamp", "role", "function", "event", "lc")


# class NationalConferenceDelegateType(DjangoObjectType):
#     class Meta:
#         model = NationalConferenceDelegate
#         fields = ("name", "gender", "phone_number", "email", "cv", "indemnity_form",
#                   "id_front", "id_back", "time_stamp", "role", "function", "event", "lc")


# class EwaDelegateType(DjangoObjectType):
#     class Meta:
#         model = EwaDelegate
#         fields = ("name", "gender", "phone_number", "email", "cv", "indemnity_form",
#                   "id_front", "id_back", "time_stamp", "role", "aiesecer", "function", "event", "lc")


# class ExpaLogin(graphene.Mutation):
#     user = graphene.Field(UserType)
#     token = graphene.Field(graphene.String)

#     class Arguments:
#         code_token = graphene.String(required=True)
#         type = graphene.String(required=True)

#     def mutate(self, info, code_token, type):
#         password = "magicLand"
#         try:
#             mytoken = expa_sign_in_new(code_token)
#         except:
#             raise Exception('Failed to authenticate your account.')
#         # Load User data and save it
#         # print(mytoken)
#         try:
#             ep_data = get_ep_info(mytoken)
#             print(ep_data['email'])
#             print(ep_data['first_name'])
#             print(ep_data['last_name'])
#         except:
#             raise Exception('Failed to retrieve your data')
#         user_email = ep_data['email']
#         # Check If EP has active Role and is in Egypt!
#         my_user = authenticate(username=user_email, password=password)
#         if my_user is not None:
#             alpha_token = create_jwt_token(my_user)
#             print(my_user.profile.gender)
#             print("successful old auth")
#             return ExpaLogin(user=my_user, token=alpha_token)

#         my_user = get_user_model()(
#             username=user_email,
#             email=user_email,
#         )
#         my_user.set_password(password)
#         my_user.first_name = ep_data['first_name']
#         my_user.last_name = ep_data['last_name']
#         my_user.save()
#         profile = Profile(user=my_user)
#         profile.expa_id = ep_data['id']
#         print(profile.expa_id)
#         profile.first_name = ep_data['first_name']
#         profile.last_name = ep_data['last_name']
#         profile.full_name = ep_data['full_name']
#         print(profile.full_name)
#         profile.gender = ep_data['gender']
#         profile.status = ep_data['status']
#         profile.joined_at = returndate(ep_data['created_at'])
#         profile.access = mytoken
#         profile.applications_count = ep_data['opportunity_applications_count']
#         profile.email = ep_data['email']
#         profile.phone = ep_data['contact_detail']['phone']
#         profile.facebook = ep_data['contact_detail']['facebook']
#         profile.instagram = ep_data['contact_detail']['instagram']
#         if type == "ICX":
#             profile.is_icx = True
#         elif type == "OGX":
#             profile.is_ogx = True
#         profile.home_lc = ep_data['home_lc']['name']
#         for item in ep_data['member_positions']:
#             if item['status'] == "active":
#                 profile.role = item['role']['name']
#         profile.save()
#         print(ep_data['home_lc'])
#         print('successful profile save')
#         alpha_token = create_jwt_token(my_user)
#         print("successful new auth")
#         return ExpaLogin(user=my_user, token=alpha_token)


# class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
#     user = graphene.Field(UserType)

#     class Arguments:
#         expa_pwd = graphene.String(required=True)

#     @classmethod
#     def resolve(cls, root, info, expa_pwd, **kwargs):
#         return cls(user=info.context.user)


# class Query(graphene.ObjectType):
#     all_LocalConferenceDelegate = graphene.List(
#         LocalConferenceDelegateType, event=graphene.Int())
#     all_NationalConferenceDelegate = graphene.List(
#         NationalConferenceDelegateType, event=graphene.Int())
#     all_EwaDelegate = graphene.List(EwaDelegateType, event=graphene.Int())
#     currentuser = graphene.Field(UserType)

#     def resolve_currentuser(self, info):
#         user = info.context.user
#         return user

#     def resolve_all_LocalConferenceDelegate(root, info, event):
#         if info.context.user.is_staff:
#             return LocalConferenceDelegate.objects.filter(event=event)
#         else:
#             return None

#     def resolve_all_NationalConferenceDelegate(root, info, event):
#         if info.context.user.is_staff:
#             return NationalConferenceDelegate.objects.filter(event=event)
#         else:
#             return None

#     def resolve_all_EwaDelegate(root, info, event):
#         if info.context.user.is_staff:
#             return EwaDelegate.objects.filter(event=event)
#         else:
#             return None


# class Mutation(graphene.ObjectType):
#     expa_login = ExpaLogin.Field()
#     token_auth = ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)


