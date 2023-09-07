from rest_framework.test import APITestCase
from rest_framework import status

from habit.models import Habit
from users.models import User, UserRoles


class HabitsTestCase(APITestCase):
    """Тестирование кода"""

    def setUp(self) -> None:
        """Базовый сетап"""
        self.user = User.objects.create(
            email='tester@test1.com',
            role=UserRoles.MODERATOR,
            is_active=True,
            is_superuser=True,
            is_staff=True
        )
        self.user.set_password('qwerty')
        self.user.save()
        response = self.client.post('/users/token/', {"email": "tester@test1.com", "password": "qwerty"})
        # print(response.json())
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    @staticmethod
    def create_test_habit(user):
        """Метод создающий объект для тестирования"""
        test_habit = Habit.objects.create(
            created_by=user,
            name='test_habit',
            place='test_habit_place',
            time='15:00',
            action='test_habit_action',
            is_pleasant=True,
            bound_habit=None,
            periodic=2,
            reward=None,
            time_for_execution='00:59',
            public=True
        )
        return test_habit

    def test_habit_create(self):
        """Тест создания привычки (с корректными данными и с заведомо неверными данными)"""
        data = {
            'created_by': 1,
            'name': 'test_habit_create',
            'place': 'test_habit_place',
            'time': '15:00',
            'action': 'test_habit_action',
            'is_pleasant': True,
            # 'bound_habit': 'None',
            'periodic': 2,
            'reward': 'None',
            'time_for_execution': '00:00:59',
            'public': True

        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('test_habit_create', 'test_habit_create')
        bad_data = {
            'created_by': 1,
            'name': 'test_habit_create',
            'place': 'test_habit_place',
            'time': '15:00',
            'action': 'test_habit_action',
            'is_pleasant': True,
            # 'bound_habit': 'None',
            'periodic': 2,
            'reward': 'None',
            'time_for_execution': '00:05:00',
            'public': True

        }
        bad_response = self.client.post('/habits/', data=bad_data)
        self.assertEqual(bad_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habits_list(self):
        """Тестирование получения списка привычек"""
        self.create_test_habit(self.user)
        response = self.client.get('/habits/')
        habit_list = response.json()
        # print(habit_list['results'][0]['name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(habit_list['results'][0]['name'], 'test_habit')

    def test_habits_is_public(self):
        """Тестирование получения списка привычек со статусом is_public=True"""
        self.create_test_habit(self.user)
        response = self.client.get('/habits_public/')
        habit_public = response.json()
        # print(habit_public)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(habit_public['results'][0]['name'], 'test_habit')
