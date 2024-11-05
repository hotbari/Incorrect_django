from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer



# 사용자 목록을 처리하는 APIView 클래스
class UserList(APIView):
    # get 요청을 처리하는 메서드
    def get(self, request):
        # 모든 User 객체를 조회
        users = User.objects.all()
        # UserSerializer 를 사용해 사용자 데이터를 직렬화.
        serializer = UserSerializer(users, many=True)
        # 직렬화된 사용자 데이터를 응답으로 반환
        return Response(serializer.data)

    # post 요청을 처리하는 메서드
    def post(self, request):
        # data를 기반으로 UserSerializer 인스턴스 생성
        serializer = UserSerializer(data=request.data)
        # 데이터가 유효한지 확인
        if serializer.is_valid():
            # 유효하면 저장
            serializer.save()
            # 시리얼라이즈된 데이타로 응답해 반환하고, 201 Created 상태 코드 설정
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효하지 않은 경우에 에러 메시지를 포함해 반환하고, 400 Bad Request 상태 코드 설정
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 유저 디테일을 처리하는 APIView 클래스
class UserDetail(APIView):
    # primary key를 통해 오브젝트(객체)를 가져온다
    def get_object(self, pk):
        try:
            # pk로 사용자 객체를 조회
            return User.objects.get(pk=pk)
        # 사용자가 존재하지 않은 경우
        except User.DoesNotExist:
            # None 을 반환
            return None

    # GET 요청을 처리하는 메서드
    def get(self, request, pk):
        # 주어진 pk로 사용자 객체를 가져온다.
        user = self.get_object(pk)
        # 사용자가 None(존재 x) 이면?
        if user is None:
            # 404 Not Found 상태 코드를 반환
            return Response(status=status.HTTP_404_NOT_FOUND)
        # UserSerializer를 사용해 user 데이터를 직렬화 한다
        serializer = UserSerializer(user)
        # 직렬화된 serializer 데이터를 응답
        return Response(serializer.data)

    # PUT 요청을 처리하는 메서드
    def put(self, request, pk):
        # 주어진 pk로 사용자 객체를 가져온다.
        user = self.get_object(pk)
        # 존재하지 않으면
        if user is None:
            # 404 Not Found 상태 코드를 반환
            return Response(status=status.HTTP_404_NOT_FOUND)
        # user 데이터와 요청 data를 기반으로 UserSerializer 인스턴스 생성
        serializer = UserSerializer(user, data=request.data)
        # 직렬화된 데이터 유효한지 확인
        if serializer.is_valid():
            # 유효하면 저장
            serializer.save()
            # 저장된 직렬화된 데이터를 응답 반환
            return Response(serializer.data)
        # 유효하지 않으면 에러 메시지를 포함한 응답을 반환, 400 Bad ReQuest 상태 코드를 설정
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # DELETE 요청을 처리하는 메서드
    def delete(self, request, pk):
        # 주어진 pk로 user 객체 가져옴
        user = self.get_object(pk)
        # user 가 none 이면
        if user is None:
            # 404 Not Found 응답을 반환
            return Response(status=status.HTTP_404_NOT_FOUND)
        # user 삭제
        user.delete()
        # 204 No Content 응답을 반환하여 삭제가 완료되었음을 나타낸다.
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserList(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return ResPonse(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
