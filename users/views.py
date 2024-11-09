from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
#userlist라는 클래스 만듦(apiview)를 상속 받음 / apiview는 ? 프레임워크.views에있는 기능
#데이터베이스에 저장된 모든 user를 가져와서 users에 할
#유저시리얼라이저는 json형식으로 변환해주 역할임 / users에서 가져온 데이터를 저장 / many true는 여러객체를 한번에 처리해줌
#response(seralizer.date)라는 값을 리턴함 / 데이터를 json형식으로 반환 후 변환한 데이터를 담은 리스폰스 객체를 만듦

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#post 함수 정의 / http 메서드는 Post / self 인스턴스 본인 / httprequest객체
# 데이터를 json형태로 변환하는 클래스(request.date를 전달해서 검증/어디?시리얼라이저에)
#만약 검증된 데이터가 유효하지 않다면 false
#유효하다면 저장 후 생성
#생성된 데이터를 json형태로 반환 후 http코드는 201로 설정. created라는 상태 나타냄
#유효하지 않은 데이터면 http 코드 400. nbad_request상태 나타냄

class UserDetail(APIView):
    def get_object(self, pk):   #pk로 조회해서 사용자 객체를 데이터베이스에서 가져옴
        try:
            return User.objects.get(pk=pk)  #pk로 user모델에서 해당하는 객체 가져옴
        except User.DoesNotExist:   #없는 경우? none반환
            return None

    def get(self, request, pk): #pk에 맞는 유저 정보 조회
        user = self.get_object(pk)  #사용자 객체 가져옴
        if user is None:    #존재하지 않으면
            return Response(status=status.HTTP_404_NOT_FOUND)   #404에러
        serializer = UserSerializer(user)   #존재하면 json형태로 변환
        return Response(serializer.data)    #그리고반환

    def put(self, request, pk): #정보 수정
        user = self.get_object(pk)#사용자 객체 가져옴
        if user is None:    #존재하지 않으면?
            return Response(status=status.HTTP_404_NOT_FOUND)#404
        serializer = UserSerializer(user, data=request.data)  #존재하면 유효성검사함
        if serializer.is_valid():#만약 유효성 검사 성공하면
            serializer.save()   #변경 사항 저장
            return Response(serializer.data)    #그리고 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #실패시 400 에러

    def delete(self, request, pk):  #사용자 삭제
        user = self.get_object(pk)  #사용자 객체 가져옴
        if user is None:    #존재하지 않는다면
            return Response(status=status.HTTP_404_NOT_FOUND) #404에러
        user.delete()#존재하면 삭제
        return Response(status=status.HTTP_204_NO_CONTENT)#삭제완료시 204코드
