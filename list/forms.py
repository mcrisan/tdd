from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from list.models import Item, List

User = get_user_model()
EMPTY_LIST_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"
EMAIL_NOT_VALID_ERROR = "Enter a valid email address."
USER_NOT_VALID_ERROR = "User does not exist"


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }
    

class NewListForm(ItemForm):
        
    def save(self, owner):
        if owner.is_authenticated():
            return List.create_new(first_item_text=self.cleaned_data['text'], owner=owner)
        else:
            return List.create_new(first_item_text=self.cleaned_data['text'])
  
    
class ExistingListItemForm(ItemForm):
    def __init__(self, for_list, *args, **kwargs):
        super(ExistingListItemForm, self).__init__(*args, **kwargs)
        self.instance.list = for_list
        
    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)
            
class ShareWithForm(forms.Form):
    email = forms.EmailField()
    
    def clean_email(self):
        email=self.data['email']
        try:
            User.objects.get(email=self.data['email'])
        except User.DoesNotExist:
            raise ValidationError(USER_NOT_VALID_ERROR)
        return email
    

            
            