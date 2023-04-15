from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Student(models.Model):

    # Personal info
    student_image = models.ImageField(upload_to="pictures")
    qr_code = models.ImageField(upload_to='qr_code', blank=True)
    name = models.CharField(max_length=20)
    personal_email = models.EmailField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    current_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)

    # acadmeics info
    college_name = models.CharField(max_length=100)
    enrollment_year = models.IntegerField()
    course = models.CharField(max_length=20)
    branch = models.CharField(max_length=20, default="")
    roll_no = models.IntegerField()
    college_email = models.EmailField()
    current_cgpa = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        qr_name = "127.0.0.1:8000/student/"+str(self.roll_no)
        qrcode_img = qrcode.QRCode(border=3, box_size=8)
        qrcode_img.add_data(qr_name)
        qrcode_img.make(fit=True)
        img = qrcode_img.make_image(fill_color="green", back_color="white")
        file_name = f'qr_code-{self.roll_no}.png'
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.qr_code.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)
