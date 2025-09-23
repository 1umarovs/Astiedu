from django import forms
from apps.cauth.models import User, residential_address, GraduatedEducation


class BaseStyledForm(forms.ModelForm):
    """
    Barcha fieldlarga avtomatik 'form-control' class beruvchi base class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            css_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{css_class} form-control".strip()


class UserForm(BaseStyledForm):
    class Meta:
        model = User
        fields = ["fullname", "image", "phone", "passport_number", "brithday", "gender"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["fullname"].widget.attrs.update({
            "id": "id_fullname",
            "placeholder": "F.I.O kiriting"
        })

        self.fields["phone"].widget.attrs.update({
            "id": "id_phone",
            "type": "tel",
            "placeholder": "+998901234567",
            "class": "phone-input form-control"
        })

        self.fields["brithday"].widget.attrs.update({
            "id": "id_brithday",
            "type": "date",
            "class": "date-input form-control"
        })

        self.fields["passport_number"].widget.attrs.update({
            "id": "id_passport",
            "placeholder": "AA1234567",
            "class": "passport-input form-control"
        })


class EducationForm(BaseStyledForm):
    class Meta:
        model = GraduatedEducation
        fields = [
            "country",
            "region",
            "institution",
            "education_type",
            "speciality",
            "graduation_date",
            "diploma_number",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Diplom tugash sanasi
        self.fields["graduation_date"].widget.attrs.update({
            "type": "date",
            "placeholder": "YYYY-MM-DD",
            "max": "2025-01-01",
        })


class AddressForm(BaseStyledForm):
    class Meta:
        model = residential_address
        fields = ["country", "region", "citizenship", "address", "index"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Pochta indeksi: faqat 6 ta raqam
        self.fields["index"].widget.attrs.update({
            "placeholder": "100123",
            "pattern": "^[0-9]{6}$",
            "title": "6 xonali pochta indeksi"
        })
