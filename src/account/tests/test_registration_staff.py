from unittest.mock import Mock

from rest_framework import status
from ..account_status import AccountStatus
from ..account_type import AccountType, ACCOUNT_TYPE_CHOICES
from ..account_type import StaffGroupType
from account.models import StaffAccount, Account
from .test_registration import RegistrationTestCase


class StaffRegistrationTestCase(RegistrationTestCase):

    url = '/account/register/staff/'

    def __test_success(self, filename, staff_type):
        registration_data = self.read_test_data(filename)
        self.assertEquals(StaffAccount.objects.count(), 0)
        groups = Mock()
        groups.filter(name=StaffGroupType.STAFF_VERIFICATION.value).exists.return_value = True
        user = Mock()
        user.configure_mock(type=AccountType.STAFF.value, status=AccountStatus.VERIFIED.value,
                                         groups=groups, is_anonymous=False)
        self.client.force_authenticate(user=user)
        response = self.client.post(self.url, registration_data, format='json')

        self.assertEquals(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEquals(response.__dict__['data']['type'], dict(ACCOUNT_TYPE_CHOICES)[AccountType.STAFF.value])
        self.assertEquals(Account.objects.count(), 1)
        self.assertEquals(StaffAccount.objects.count(), 1)
        account = Account.objects.get()
        self.assertEquals(account.username, registration_data['username'])
        self.assertEquals(account.first_name, registration_data['first_name'])
        self.assertEquals(account.last_name, registration_data['last_name'])
        self.assertEquals(account.email, registration_data['email'])
        self.assertEquals(account.status, AccountStatus.VERIFIED.value)
        self.assertEquals(account.type, AccountType.STAFF.value)
        self.assertTrue(account.groups.filter(name=staff_type.value).exists())
        self.assertNotEquals(account.password, '')
        self.assertNotEquals(account.password, registration_data['password'])

    def test_registration_staff_jobs_success(self):
        self.__test_success('staff_jobs_success.json', StaffGroupType.STAFF_JOBS)

    def test_registration_staff_cv_success(self):
        self.__test_success('staff_cv_success.json', StaffGroupType.STAFF_CV)

    def test_registration_staff_verification_success(self):
        self.__test_success('staff_verification_success.json', StaffGroupType.STAFF_VERIFICATION)

    def test_registration_staff_no_group_provided(self):
        registration_data = self.read_test_data('staff_no_group_provided.json')
        self.assertEquals(StaffAccount.objects.count(), 0)
        groups = Mock()
        groups.filter(name=StaffGroupType.STAFF_VERIFICATION.value).exists.return_value = True
        user = Mock()
        user.configure_mock(type=AccountType.STAFF.value, status=AccountStatus.VERIFIED.value,
                                         groups=groups, is_anonymous=False)
        self.client.force_authenticate(user=user)
        response = self.client.post(self.url, registration_data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEquals(StaffAccount.objects.count(), 0)

