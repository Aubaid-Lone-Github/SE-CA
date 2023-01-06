import unittest
import my_otp

class TestStringMethods(unittest.TestCase):

    def testcase1(self):
        Email = my_otp.validate_email('zainulkhan032@gmail.com')
        self.assertEquals(True,Email)

    def testcase2(self):
        size = 4
        OTP = my_otp.generate_otp()
        self.assertEqual(len(OTP), size)

    def testcase3(self):
        Email = my_otp.send_mail("8080")
        self.assertEquals(True,Email)

if __name__ == '__main__':
    unittest.main()