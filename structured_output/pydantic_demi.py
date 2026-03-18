from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):    # it always inherits from BaseModel
    
    name: str='jaya'
    age: Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10)  # gt means greater than and lt means less than
    

# make the dic
new_student = {"name":32,"email":"bhc@gmail.com"}
student= Student(**new_student)

print(student)