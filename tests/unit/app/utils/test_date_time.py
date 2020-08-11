from unittest import TestCase
from unittest.mock import patch, call

from app.utils.date_time import generate_datetime_now


class TestDateTime(TestCase):

    @patch('app.utils.date_time.timezone')
    @patch('app.utils.date_time.datetime')
    def test_generate_date_time_must_call_datetime_now(
            self,
            datetime_mock,
            timezone_mock,
    ):
        # Arrange
        datetime_mock.now.return_value = 'datetime.now'

        # Action
        datetime_response = generate_datetime_now()

        # Assertion
        self.assertEqual(datetime_response, 'datetime.now')

        datetime_mock_calls = datetime_mock.mock_calls
        self.assertEqual(1, len(datetime_mock_calls))
        datetime_mock.assert_has_calls([
            call.now(tz=timezone_mock.utc)
        ])
