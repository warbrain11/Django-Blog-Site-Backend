from django.shortcuts import render
from django.http import JsonResponse
from blog_site.models import *
from blog_site.serializers import *
from rest_framework.decorators import api_view
from datetime import datetime

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

import json
import os


@api_view(['POST'])
def Create_Blog_Post(request):
    #Get the token header
    authToken = request.headers.get('Authorization')[6:] if request.headers.get('Authorization') else ''
    user = Token.objects.filter(key = authToken)
    
    if(user.count() > 0):
        data = request.data
        images = []

        data['date'] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")

        blog_post = Blog_Post(
            post_title = data['post_title'], 
            author = data['author'],
            post_content = data['post_content'],
            date = data['date']
            )

        blog_post.save()

        #Sift through images in data and create a blog post image for each 
        for key in data.keys():
            if(key[0:5] == 'image'):
                img = Blog_Post_Image(blog_post = blog_post, image = data[key])
                img.save()

        return JsonResponse(Blog_Post_Ser(blog_post, many = False).data, safe = False)
    else:
        data = request.data
        data._mutable = True

        if('post_content' not in data.keys()):
            return JsonResponse("Must include post_content in body", safe = False)
        
        if('post_title' not in data.keys()):
            return JsonResponse("Must include post_title in body", safe = False)

        if('author' not in data.keys()):
            data['author'] = 'anonymous'

        date = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")

        blog_post = Blog_Post(
            post_title = data['post_title'], 
            author = data['author'],
            post_content = data['post_content'],
            date = date,
            isMainPost = False,
            isVisible = False,
            )

        blog_post.save()

        return JsonResponse(Blog_Post_Ser(blog_post, many = False).data, safe = False)

    return JsonResponse("Login first", safe = False)

@api_view(['POST'])
def UpdateBlogPostVisibility(request):
    data = request.data

    if('id' in data.keys()):
        try:
            blog_post = Blog_Post.objects.get(id = int(request.data['id']), isMainPost = False)
            blog_post.isVisible = not blog_post.isVisible
            blog_post.save(update_fields=['isVisible'])

            return JsonResponse('Successfully Updated Post Visibility', safe = False)
        except Blog_Post.DoesNotExist:
            return JsonResponse('No Posts Found')


    return JsonResponse('Must include id in body')

@api_view(['POST'])
def AdminLogin(request):
    if('username' in request.data.keys() and 'password' in request.data.keys()):
        user = authenticate(username = request.data['username'], 
                            password = request.data['password'])

        if(user is not None):
            token = Token.objects.get(user = user).key

            return JsonResponse( {
                'username': user.username,
                'token': token
            }, safe = False)
        else:
            return JsonResponse("Invalid Credentials", safe = False, status = 401)

    return JsonResponse("Must Input Username and Password!", safe = False)
    
@api_view(['POST'])
def DeletePost(request):
    try:
        if('id' not in request.data.keys()):
            return JsonResponse("Invalid Credentials", safe = False)
        
        Blog_Post.objects.get(id = request.data['id']).delete()

        return JsonResponse("Successfully Deleted Post", safe = False)
    except Blog_Post.DoesNotExist:
        return JsonResponse("Invalid ID", safe = False)


        